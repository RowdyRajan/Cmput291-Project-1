import datetime
import helpers

class voilationRecord():
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

	def insertTicket(ticket_no, violator_no, vehicle_no, office_no, vtype, vdate, place, descriptions):
		# Method that actually adds the new row to the database
		cursor = connection.cursor()
		statement = "INSERT INTO ticket VALUES(%s, %s, %s, %s, %s, %s, %s, %s") % \
		(ticket_no, violator_no, vehicle_no, office_no, vtype, vdate, place, descriptions)

		# Error check

		cursor.execute(statement)
		connection.commit()
		cursor.close()


	def nextID():
		# Generates the next ticket ID by incrimenting the highest current ID by one
		statement = "SELECT max(ticket_no) from ticket"
		rows = ReturnData(statement)
		ID = rows[0] + 1
		return ID

	def ticketInput:

		officer = None
		violator = None
		vehicle = None
		vtype = None
		description = ""

		# Prompt user to enter data for a new ticket entry
		while(1){

			if(!officer){
				officer = raw_input("SIN of issuing officer:\n\r")
				if( !InDB( sinExists(officer) ) ) {
					print("No record of officer in Database, please try again.\n\r")
					continue
				}
			}

			if(!violator){
				violator = raw_input("SIN of violating person:\n\r")
				if( !InDB( sinExists(violator) ) ) {
					print("No record of person in Database, please try again.\n\r")
					continue
				}
			}

			if(!vehicle){
				vehicle = raw_input("Serial Number vehicle:\n\r")
				if( !InDB( VINisIn(vehicle) ) ) {
					print("No record of vehicle in Database, please try again.\n\r")
					continue
				}
			}

			if(!vtype){
				vtype = raw_input("Type of violation:\n\r")
				statement = "SELECT v.vtype FROM ticket_type v WHERE (v.vtype) = ('%s')" % (vtype)
				if( !InDB(statement) ) {
					print("Invalid violation type, please re-enter.\n\r")
					continue
				}
			}			

			vdate = raw_input("Date:\n\r")

			place = raw_input("Location:\n\r")

			description = raw_input("Further comments or descriptions (optional):\n\r")

			insertTicket(nextID(), violator, vehicle, officer, vtype, vdate, place, description)
		}

	def inputExists_ta():
		# Possible helper function to repeat input attempt
		if( InDB( sinExists(officer) ) ) {
			
		} else {
			print("No record in Database, try again (Y/N).\n\r")
			# string parsing and some loop stuff...

		}
		
			
			




