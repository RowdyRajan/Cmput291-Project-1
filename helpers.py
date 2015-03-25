import cx_Oracle
import string

def ReturnData(statement)
	# helper function for getX
	curs = connection.cursor()
	curs.execute(statement)
	rows = curs.fetchall()
	curs.close()
	return rows[0][0]

def InDB(statement):
	# helper function to see if something exists in 
	curs = connection.cursor()
	curs.execute(statement)
	rows = curs.fetchall()
	if len(rows) > 0:
		curs.close()
		return True
	curs.close()
	return False

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
				
def VINisIn(VIN):
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
	return(InDB(statement))
