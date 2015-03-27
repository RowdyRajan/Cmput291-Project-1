# A test program to complie various other applications.

#import cx_Oracle

def main():

	menu = ["1: New Vehicle Registration",\
			"2: Auto Transaction",\
			"3: Driver Licence Registration",\
			"4: Add Violation Record",\
			"5: Search Engine",\
			"6: Exit"]

	print("Welcome to Python Database Program!")
	for option in menu:
			print(option)
	print("Now you must choose...")

	while(1):
		select = int(input())
		if(select == 1):
			print("you typed", select)
		if(select == 2):
			print("you typed", select)
		if(select == 3):
			print("you typed", select)
		if(select == 4):
			print("you typed", select)
		if(select == 5):
			print("you typed", select)
		if(select == 6):
			print("you typed", select)
			exit()


def connectDatabase(connection=False):

	# I'm not sure what youre supposed to pass to make the connection work

	#Add proper connection Stuff from example code
	#We could also do a class that stores connection data like cursor etc.

	if(connection == False):
		#self.connected = False <--- if doing a class could have a status variable for connection. Makes no sense in current context so keep as comment
		print("Not Connected!")
		return None

	try:
		conn = cx_Oracle.connect(connection)

	except cx_Oracle.DatabaseError:
		print("Not Connected!")
		return None

	else:
		cursor = conn.cursor()
		#self.connected = True
		print("Connected!")
		return cursor

if __name__ == '__main__':
	connectDatabase()
	main()