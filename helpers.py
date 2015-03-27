import cx_Oracle
import getpass
import string
import re
import datetime


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

def deleteOwner(VIN):
	query = "DELETE FROM owner WHERE vehicle_id = '%s'"%VIN
	cursor = connection.cursor()
	cursor.execute(query)
	cursor.close()


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
	# helper function to insert a row
	global connection
	cursor = connection.cursor()
	cursor.execute(statement)
	cursor.close()
	#connection.commit()
	return

def getName(SIN):
	# Returns SIN's name
	statement = "select p.name from people p where (p.sin) = ('%s')" % (SIN)
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

def OwnerExists(SIN,VID):
	# Returns if SIN exists
	statement = "select o.owner_id from owner o where (o.owner_id) = ('%s') AND (o.vehicle_id) = ('%s')" % (SIN, VID)
	return(InDB(statement))


def licenceExists(l_no):
	# License for Inputted SIN exists?
	statement = "select l.licence_no from drive_licence l where (l.licence_no) = ('%s')" % (l_no)
	return InDB(statement)

def typeIDExists(type_id):
	#Checks to see if a vehicle type id exits 
	statement = "select vt.type_id from vehicle_type vt where (vt.type_id) = %s" % (type_id)
	return InDB(statement)

def tranIDExists(tran_id):
	#Checks to see if a vehicle type id exits 
	statement = "select a.transaction_id from auto_sale a where (a.transaction_id) = %s" % (tran_id)
	return InDB(statement)

def insertVehicle(serial_no, maker, model, year,color,type_id):
	statement = "INSERT into vehicle values ('%s' , '%s' , '%s' , %s , '%s' ,%s)" % (serial_no, maker, model, year,color,type_id)
	return InsertData(statement)

def insertPerson(SIN, name, height, weight, eyecolor , haircolor, addr, gender, birthday):
	statement = "INSERT into people values ('%s' , '%s' , %s , %s , '%s' ,'%s', '%s', '%s', to_date('%s', 'yyyy/mm/dd'))" % (SIN,name,height,weight,eyecolor,haircolor,addr, gender,birthday)
	return InsertData(statement)

def insertOwner(owner_id, vehicle_id, is_primary_owner):
	statement = "insert into owner values ('%s' , '%s' , '%s')" % (owner_id,vehicle_id, is_primary_owner)

def insertTicket(ticket_no, violator_no, vehicle_no, office_no, vtype, vdate, place, description):
	statement = "INSERT into ticket values (%d , '%s' , '%s' , '%s' , '%s' , to_date('%s', 'yyyy/mm/dd'), '%s', '%s' )" % (ticket_no, violator_no, vehicle_no, office_no, vtype, vdate, place, description)
	return InsertData(statement)

def insertLicence(licNo, SIN, licClass, photo, issuingDate, expireDate):
	statement = "INSERT into ticket values ('%s', '%s' , '%s' , to_date('%s', 'yyyy/mm/dd'), to_date('%s', 'yyyy/mm/dd'))" % (licNo, SIN, licClass, photo, issuingDate, expireDate)
	InsertData(statement)
	return

def dateChecker(answer):
    #checks if answer is a valid date
    #asks with askString untill valid date is given 

    #returns a strng of valid date 
    matches = re.findall(r'(^\s*\d{4}/\d{2}/\d{2}){1}\s*$',answer)
    while len(matches) == 0 or not validDate(answer.strip()):
        if len(matches) == 0:
            answer = input("Invalid format. Input in the format yyyy/mm/dd: ")
        else:
            answer = input("Invalid date. Please enter an actual date: ")
        matches = re.findall(r'(^\s*\d{4}/\d{2}/\d{2}){1}\s*$',answer)
    return answer.strip()

def validDate(date):
    #checks if entered date is valid 
    try:
        datetime.datetime.strptime(date, '%Y/%m/%d')
    except ValueError:
        return False

    return True

def digitAskLoop(answer,askString, confirmFunction):
	"""
	This function will take an answer and a confirm function
	and will keep asking for input with the askString until 
	confirmFunction returns true  based on the input and the
	input is a digit.

	returns: a valid answer based on the cofirmFunction
	"""
	while(not answer.isdigit() or confirmFunction(answer)):
		if not answer.isdigit():
			answer = input("Not a valid number. Please re-enter: ")
		else:
			answer = input(askString);
	return answer;


def digitNotInAskLoop(answer,askString, confirmFunction):
	"""
	This function will take an answer and a confirm function
	and will keep asking for input with the askString until 
	confirmFunction returns false based on the input

	returns: a valid answer based on the cofirmFunction
	"""
	while(not answer.isdigit() or not confirmFunction(answer)):
		if not answer.isdigit():
			answer = input("Not a valid number. Please re-enter: ")
		else:
			answer = input(askString);
	return answer;

def askLoop(answer,askString,confirmFunction):
	"""
	This function will take an answer and a confirm function
	and will keep asking for input with the askString until 
	confirmFunction returns true based on the input or the
	input is not blank

	returns: a valid answer based on the cofirmFunction
	"""
	while confirmFunction(answer) or answer.isspace():
		answer = input(askString)

def maxWidthDigitChecker(answer, askString, maxNumberSize):
	"""
	This function will take an answer and a confirm function
	and will keep asking for input with the askString until 
	confirmFunction returns true based on the input and the
	answer is a digit with a size less than maxNumberSize

	returns: a valid answer based on the cofirmFunction
	"""
	while(not answer.isdigit()	or len(answer) != maxNumberSize):
		answer = input(askString)
	return answer
 
def digitChecker(answer, askString):
	#checkis if answetr is a digit and asks with
	#askString until it is confirmed a digit
	#returns a answer is a digit
	while(not answer.isdigit()):
		answer = input(askString)
	return answer

def floatChecker(answer, askString):
	#checkis if answer is float and asks with
	#askString until it is confirmed a digit
	#returns a answer is a digit
	while(not answer.isdigit()):
		parts = answer.split('.')
		if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
			return answer
		answer = input(askString)
	return answer

def blankSpaceLoop(answer, askString):
	#checks to see if answer is blank and asks
	#with ask string until the answer in not
	#blank
	while answer.isspace():
		answer = input(askString)
	return answer

def yesOrNoChecker(askString):
	#Checks if answer is yes or no
	answer = input(askString)
	while answer not in ['y', 'n']:
		answer = input("Please enter y or n: ")

	if answer == 'y':
		return True 
	return False 


def makePerson(OwnerType, VID):
	"""
	Makes a person and adds them to the data base
	Ownertype is the type of owner they are:
	1 = primary owner
	2= secondary owner
	"""

	ownerTypeMap = { 1 : ["primary owner", 'y'] , 2 : ["secondary owner", 'n']}

	while True:
		SIN = input("Enter the SIN of the new " + ownerTypeMap[OwnerType][0] + ' ');
		SIN = digitChecker(SIN, "Not a valid SIN. Please enter again: ");
		
		if OwnerExists(SIN,VID):
			print("Invalid Sin. Owner Exists")
			continue
		if not sinExists(SIN) or OwnerExists(SIN,VID) :
			if not yesOrNoChecker("SIN does not exist. Would you like to make this SIN a person?[y or n]: "):	 
				continue
			
			name = input("Enter the persons name: ")
			name = blankSpaceLoop(name, "Blank Name. Please enter something: ")
			
						 				
			height = input("Enter the person's height: ")
			height = floatChecker(height, "Invalid number. Please enter again: ")

			weight = input("Enter the person's weight: ")
			weight = floatChecker(weight ,"Invalid number. Please enter again: ")
			eyecolor  = input("Enter the person's eyecolor: ")
			eyecolor = blankSpaceLoop(eyecolor ,"Blank entree. Please enter something: ")
			haircolor  = input("Enter the person's haircolor: ")
			haircolor = blankSpaceLoop(haircolor ,"Blank entree. Please enter something: ")


			addr  = input("Enter the person's address: ")
			addr = blankSpaceLoop(addr ,"Blank entree. Please enter something: ")
			
						
			gender  = input("Enter the person's gender: ")
			while gender not in ['m', 'f']:
				gender = input("Please enter m or f: ")	
			
			birthday = input("Enter date of birth: ")	
			birthday = dateChecker(birthday)
			
			insertPerson(SIN,name,height,weight,eyecolor,haircolor,addr,gender,birthday)
		insertOwner(SIN, VID,ownerTypeMap[OwnerType][1])
		break
	return

def makeSinglePerson(SIN):
	#Asks for inputs for a person
	name = input("Enter the persons name: ")
	name = blankSpaceLoop(name, "Blank Name. Please enter something: ")
			
	height = input("Enter the person's height: ")
	height = floatChecker(height, "Invalid number. Please enter again: ")

	weight = input("Enter the person's weight: ")
	weight = floatChecker(weight ,"Invalid number. Please enter again: ")
	eyecolor  = input("Enter the person's eyecolor: ")
	eyecolor = blankSpaceLoop(eyecolor ,"Blank entree. Please enter something: ")
	haircolor  = input("Enter the person's haircolor: ")
	haircolor = blankSpaceLoop(haircolor ,"Blank entree. Please enter something: ")


	addr  = input("Enter the person's address: ")
	addr = blankSpaceLoop(addr ,"Blank entree. Please enter something: ")
			
						
	gender  = input("Enter the person's gender: ")
	while gender not in ['m', 'f']:
		gender = input("Please enter m or f: ")	
			
	birthday = input("Enter date of birth: ")	
	birthday = dateChecker(birthday)
			
	insertPerson(SIN,name,height,weight,eyecolor,haircolor,addr,gender,birthday)

