#!/usr/bin/python3
#Search Engine
#List name, licence_no, addr, driving class, driving_condition and expiring_date
#by entering license_no or a given name. Display all duplicates.
#
#List violation records received by a person if the licence_no or sin is entered
#
#Print vehicle history - #times been sold, average price, #violations it has 
#based on VIN
from helpers import searchDB
def search():
	print('1. Licence information')
	print('2. Violation records')
	print('3. Vehicle history')
	print('4. Go back to main menu')
	while True:
		choice = input('Enter your choice (1-4): ')
		if choice not in {'1', '2', '3', '4'}:
			print('Invalid option. Try again.')
			continue
		else:
			break
	print("The value of choice is %s" %choice)
	if (choice=='1'):
		print('Press 1 to search by Licence number')
		print('Press 2 to search by name')
		while True:
			choice = input('Enter your choice (1-4): ')
			if( choice not in {'1', '2'}):
				print('Invalid option. Start over.')
				continue
			else:
				break
		if (choice == '1'):
			while True:
				li_num = input('Enter the number to be searched for: ')
				#test if valid number
				if(len(li_num)>15):
					print('Licence numbers are 15 characters long')
					continue
				else:
					break
			statement = """SELECT p.name, l.licence_no, p.addr, p.birthday, l.class, 
			d.description, l.expiring_date, p.sin, d.c_id
			FROM people p, drive_licence l, driving_condition d, restriction r
		   WHERE p.sin = l.sin(+) AND
		   l.licence_no = r.licence_no(+) AND
		   r.r_id = d.c_id(+) AND
		   l.licence_no = '%s'""" %li_num
			table = searchDB(statement)
			printLicence(table)
		else:
			driver_name = input("Enter driver name: ")
			statement = """SELECT p.name, l.licence_no, p.addr, p.birthday, l.class, 
			d.description, l.expiring_date, p.sin, d.c_id
			FROM people p, drive_licence l, driving_condition d, restriction r
		   WHERE p.sin = l.sin(+) AND
		   l.licence_no = r.licence_no(+) AND
		   r.r_id = d.c_id(+) AND
		   UPPER(p.name) = UPPER('%s')""" %driver_name
			table = searchDB(statement)
			printLicence(table)
	elif(choice=='2'):
		print('Press 1 to search by Licence number')
		print('Press 2 to search by SIN')
		while True:
			choice = input('Enter your choice (1-2): ')
			if( choice not in {'1', '2'}):
				print('Invalid option. Start over.')
				continue
			else:
				break
		if (choice == '1'):
			while True:
				li_num = input('Enter the number to be searched for: ')
				if(len(li_num)>15):
					print('Licence numbers are 15 characters long')
					continue
				else:
					break
			statement = """SELECT t.ticket_no, t.vdate, t.vtype, t.descriptions 
			FROM ticket t, ticket_type type, drive_licence d
		   	WHERE type.vtype (+)= t.vtype AND d.sin(+)=t.violator_no AND
		   d.licence_no = '%s'"""%li_num
			table = searchDB(statement)
			printLicence(table)
		else:
			while True:
				try: 
					SIN = int(input('Enter the SIN to be searched for: '))
				#test if valid number
				except ValueError:
					print('Input must be an integer.')
					continue
				if (SIN < 0):
					print("Input must be positive.")
					continue
				else:
					break
			statement = """SELECT t.ticket_no, t.vdate, t.vtype, t.descriptions, type.vtype  
			FROM ticket t, ticket_type type
		   	WHERE type.vtype (+)= t.vtype
		   AND t.violator_no = '%s'"""%SIN
			table = searchDB(statement)
			printLicence(table)
	elif(choice=='3'):
		while True:
			v_serial = input('Please enter the VIN to be searched for: ')
			if (len(v_serial)>15):
				print('VIN must be 15 characters long. Try again.')
				continue
			else:
				break
		statement = """select counts.c, avgs.a, viols.cnt from (select count(*) 
		as c from auto_sale where vehicle_id = '%s')counts, 
		(select SUM(price)/count(*) as a from auto_sale where vehicle_id = 
		 '%s')avgs, (select count(*) as cnt from ticket where vehicle_id = 
		'%s')viols""" % (v_serial, v_serial, v_serial)
		table = searchDB(statement)
		printVehicleHistory(table)
	elif(choice=='4'):
		return 0
	else:
		print("Something went horridly wrong!")
		return 0

def printLicence(table):
	if (len(table) == 0):
		print("Nothing found.")
		return

	for e in table:
		name = e[0].strip()
		licence_no = e[1].strip()
		addr = e[2].strip()
		birthday = e[3]
		Class = e[4].strip()
		if (e[5] is None):
			condition = "None"
		else:
			condition = e[5].strip()
		expiry = e[6]

		print("Name: %s" %name)
		print("Licence Number: %s" % licence_no)
		print("Address: %s" % addr)
		print("Birthday: %s" % str(birthday.strftime('%Y-%m-%d')))
		print("Driving Class: %s" % Class)
		print("Driving Condition: %s" % condition)
		print("Expiration Date: %s\n" % str(expiry.strftime('%Y-%m-%d')))


def printViolation(table):
	for e in table:
		ticketNumber = e[0]
		vDate = e[1]
		vType = e[2]
		descriptions = e[3]

		print("Ticket number: %d" % ticketNumber)
		print("Violation date: %s" % str(vDate.strftime('%Y-%m-%d')))
		print("Violation type: %s" % vType)
		print("Descriptions: %s\n" % descriptions)

	if (len(table) == 0):
		print("Nothing found.")

def printVehicleHistory(table):
	for e in table:
		totalSales = e[0]
		averagePrice = e[1]
		numberTickets = e[2]

		print("Total Sales: %s" %totalSales)
		print("Average Price: %s" % averagePrice)
		print("Number of Tickets: %s\n" % numberTickets)

	if len(table) == 0:
		print("Nothing Found.")
