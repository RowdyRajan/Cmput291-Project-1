
"""
Allows a traffic violation to be put into the system by an Officer.
Things recorded (manditory):
	violation type [vtype], ticket_no, violator_no, 
	vehicle_id, officer_no, vtype, vdate, place

Things recorded (optional):
	descriptions

Assignment Tables:
	people( sin, name, height,weight,eyecolor, haircolor,addr,gender,birthday )
	drive_licence( licence_no,sin,class,photo,issuing_date,expiring_date)
	driving_condition( c_id, description )
	restriction( licence_no, r_id )
	vehicle_type( type_id, type )
	vehicle( serial_no, maker, model, year, color, type_id )
	owner(owner_id, vehicle_id, is_primary_owner)
	auto_sale( transaction_id,seller_id, buyer_id, vehicle_id, s_date, price )
	ticket_type( vtype, fine )
	ticket( ticket_no, violator_no, vehicle_no, office_no, vtype, vdate, place, *descriptions )	

"""

import datetime
from helpers import *

def VR_Start():
	print("Welcome to the violation registration service. From here you can add a ticket \
		for a traffic violation to the database\n")
	while(1):
		print("1: Add Violation.")
		print("2: Return to Main Menu.")
		try:
			select = int(input())
		except:
			print('Invalid option. Try again.')
			continue

		if(select == 1):
			ticketInput()
			
		if(select == 2):
			return


def nextID():
	# Generates the next ticket ID by incrimenting the highest current ID by one
	statement = "SELECT max(ticket_no) from ticket"
	rows = ReturnData(statement)
	ID = rows + 1
	return ID

def ticketInput():

	officer = None
	violator = None
	vehicle = None
	vtype = None
	place = None
	vdate = None
	description = ""

	# Prompt user to enter data for a new ticket entry
	while True:
		if(officer == None):
			officer = input("SIN of issuing officer: ")
			if( sinExists(officer) == False):
				print("No record of officer in Database.")
				if(tryAgain()):
					officer = None
					continue
				else:
					return None
			
		if(violator == None):
			violator = input("SIN of violating person: ")
			if( sinExists(violator) == False):
				print("No record of person in Database, please try again.")
				if(tryAgain()):
					violator = None
					continue
				else:
					return None
			

		if(vehicle == None):
			vehicle = input("Serial Number vehicle: ")
			if( VINExists(vehicle) == False ):
				print("No record of vehicle in Database, please try again.")
				if(tryAgain()):
					vehicle = None
					continue
				else:
					return None
			
		if(vtype == None):
			vtype = input("Type of violation: ")
			statement = "SELECT v.vtype FROM ticket_type v WHERE (v.vtype) = ('%s')" % (vtype)
			if( InDB(statement) == False ):
				print("Invalid violation type, please re-enter.")
				if(tryAgain()):
					vtype = None
					continue
				else:
					return None
								
		if(vdate == None):
			vdate = input("Date of violation (eg. yyyy/mm/dd): ").strip()
			vdate = dateChecker(vdate)

		if(place == None):
			place = input("Location (20 characters): ").strip()
			if( len(place) > 20 ):
				print("Entry too long, please re-enter.")
				if(tryAgain()):
					place = None
					continue
				else:
					return None

		if(description == ""): # Optional
			description = input("Further comments or descriptions (max 1000 characters): ")

			if( len(description) > 1024 ):
				print("Entry too long.")
				if(tryAgain()):
					description = ""
					continue
				else:
					return None

		ticket = insertTicket(nextID(), violator, vehicle, officer, vtype, vdate, place, description)
		return ticket

def tryAgain():
	# Possible helper function to repeat input attempt			
	print("Try again? (Y/N):\n\r")
	while(1):
		ans = input().strip().lower()
		if ans in ("yes", "y"):
			return True
		if ans in ("no", "n"):
			return False

		
if __name__ == '__main__':
	connect()
	VR_Start()			
			




