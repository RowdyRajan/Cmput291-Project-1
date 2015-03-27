# Driver Licence Registration
"""
Driver Licence Registration

This component is used to record the information needed to issuing a drive licence, 
including the personal information and a picture for the driver. 
You may assume that all the image files are stored in a local disk system.

CREATE TABLE drive_licence (
  licence_no      CHAR(15),
  sin             char(15),
  class           VARCHAR(10),
  photo           BLOB,
  issuing_date    DATE,
  expiring_date   DATE,
  PRIMARY KEY (licence_no),
  UNIQUE (sin),
  FOREIGN KEY (sin) REFERENCES people
        ON DELETE CASCADE

"""

from helpers import *

def License():
	print("Welcome to the driver's licence licensing agency. Here you can add a new drivers licence to the system")
	while(1):
		print("1: Enter New Licence")
		print("2: Return to Main Menu.")
		try:
			select = int(input())
		except:
			print('Invalid option. Try again.')
			continue

		if(select == 1):
			InsertData()
		if(select == 2):
			return


def getInfo():

	licNo = None
	SIN = None
	licClass = None
	photo = None
	issuingDate = None
	expireDate = None

	while True:
		if(licNo == None):
			licNo = input("Enter licence number: ")
			if( (licNo) == False):
				print("No record of licNo in Database.")
				if(tryAgain()):
					licNo = None
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

	# get licence_no (unique)
		# check if already in database

	# get sin
		# must already exist



if __name__ == '__main__':
	Licence()

