import cx_Oracle
import getpass
import string
import datetime
import re


def connect():
	user = input("Username [%s]: " % getpass.getuser())
	if not user:
		user = getpass.getuser()
	pw = getpass.getpass()
	conString=''+user+'/' + pw +'@gwynne.cs.ualberta.ca:1521/CRS'
	global connection
	connection = cx_Oracle.connect(conString)

def searchDB(query):
	cursor = connection.cursor()
	cursor.execute(query)
	table = cursor.fetchall()
	cursor.close()
	return table

def ReturnData(statement):
	# helper function for getX
	global connection
	cursor = connection.cursor()
	cursor.execute(statement)
	rows = cursor.fetchall()
	cursor.close()
	return rows[0][0]

def InDB(statement):
	# helper function to see if something exists in 
	global connection
	cursor = connection.cursor()
	cursor.execute(statement)
	rows = cursor.fetchall()
	if len(rows) > 0:
		cursor.close()
		return True
	cursor.close()
	return False


def InsertData(statement):
	# helper function to insert a file
	global connection
	cursor = connection.cursor()
	cursor.execute(statement)
	cursor.close()
	return

def getName(SIN):
	# Returns SIN's name
	statement = "select p.name from people p where (p.sin) = ('%s')" % (SIN)
	return(ReturnData(statement))
		
def getHeight(SIN):
	# Returns SIN's height
	statement = "select p.height from people p where (p.sin) = ('%s')" % (SIN)
	return(ReturnData(statement))
		
def getWeight(SIN):
	# Returns SIN's weight
	statement = "select p.weight from people p where (p.sin) = ('%s')" % (SIN)
	return(ReturnData(statement))

def getEyeColor(SIN):
	# Returns  at SIN's eye Color
	statement = "select p.eyecolor from people p where (p.sin) = ('%s')" % (SIN)
	return(ReturnData(statement))

def getHairColor(SIN):
	# Returns SIN's hair Color
	statement = "select p.haircolor from people p where (p.sin) = ('%s')" % (SIN)
	return(ReturnData(statement))

def getAddress(SIN):
	# Returns SIN's address
	statement = "select p.addr from people p where (p.sin) = ('%s')" % (SIN)
	return(ReturnData(statement))
		
def getGender(SIN):
	# Returns SIN's gender
	statement = "select p.gender from people p where (p.sin) = ('%s')" % (SIN)
	return(ReturnData(statement))

def getBirthday(SIN):
	# Returns SIN's birthday
	statement = "select p.birthday from people p where (p.sin) = ('%s')" % (SIN)
	return(ReturnData(statement))
		
def getVehicleModel(VIN):
	# Returns the model of vehicle at VIN
	statement = "SELECT v.model from vehicle v where (v.serial_no) = ('%s')" % (VIN)
	return(ReturnData(statement))

def getVehicleYear(VIN):
	# Returns the year of the vehicle at VIN
	statement = "SELECT v.year from vehicle v where (v.serial_no) = ('%s')" % (VIN)
	return(ReturnData(statement))

def getVehicleColor(VIN):
	# Returns the color of the vehicle at VIN
	statement = "SELECT v.color from vehicle v where (v.serial_no) = ('%s')" % (VIN)
	return(ReturnData(statement))
		
def ticketIDinDB(input):
	statement = "select t.ticket_no from ticket t where (t.ticket_no) = ('%s')" % idNum
	return(ReturnData(statement))
				
def VINExists(VIN):
	# Returns true if the given VIN is on the database
	statement = "select v.serial_no from vehicle v where v.serial_no = ('" + str(VIN) + "')"
	return(InDB(statement))

def sinExists(SIN):
	# Returns if SIN exists
	statement = "select p.sin from people p where (p.sin) = ('" + str(SIN) + "')"
	return(InDB(statement))

def licenceExists(SIN):
	# License for Inputted SIN exists?
	statement = "select l.sin from drive_licence l where (l.sin) = ('%s')" % (SIN)
	return InDB(statement)

def typeIDExists(type_id):
	#Checks to see if a vehicle type id exits 
	statement = "select vt.type_id from vehicle_type vt where (vt.type_id) = %s" % (type_id)
	return InDB(statement)

def insertTicket(ticket_no, violator_no, vehicle_no, office_no, vtype, vdate, place, descriptions):
	# Method that actually adds the new row to the database
	statement = "INSERT INTO ticket VALUES('%s', '%s', '%s', '%s', '%s', to_date('%s', 'yyyy/mm/dd'),'%s', '%s')" % \
	(ticket_no, violator_no, vehicle_no, office_no, vtype, vdate, place, descriptions)
	return InsertData(statement)

def insertVehicle(serial_no, maker, model, year,color,type_id):
	statement = "insert into vehicle values ('%s' , '%s' , '%s' , %s , '%s' ,%s)" % (serial_no, maker, model, year,color,type_id)
	return InsertData(statement)

def insertPerson(SIN, name, height, weight, eyecolor , haircolor,addr, gender, birthday):
	statement = "insert into people values ('%s' , '%s' , %s , %s , '%s' ,'%s', '%s', '%s', to_date('%s', 'yyyy/mm/dd'))" % (SIN,name,height,weight,eyecolor,haircolor,addr, gender,birthday)
	return InsertData(statement)

def dateChecker(answer):
    #checks if answer is a valid date
    #asks with askString untill valid date is given 
    #returns a strng of valid date 
	
	matches = re.findall(r'(^\s*\d{4}/\d{2}/\d{2}){1}\s*$',answer)
	while len(matches) == 0 or not validDate(answer.strip()):
		if len(matches) == 0:
			answer = input("Invalid format. Input in the format yyyy/mm/dd")
		else:
			answer = input("Invalid date. Please enter an actual date")
		matches = re.findall(r'(^\s*\d{4}/\d{2}/\d{2}){1}\s*$',answer)
	return answer.strip()

def validDate(date):
    #checks if entered date is valid 
    try:
        datetime.datetime.strptime(date, '%Y/%m/%d')
    except ValueError:
        return False

    return True


