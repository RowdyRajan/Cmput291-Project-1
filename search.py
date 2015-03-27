#!/usr/bin/python3
#Search Engine
#List name, licence_no, addr, driving class, driving_condition and expiring_date
#by entering license_no or a given name. Display all duplicates.
#
#List violation records received by a person if the licence_no or sin is entered
#
#Print vehicle history - #times been sold, average price, #violations it has 
#based on VIN
from helpers import ReturnData
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
	if (choice==1):
		print('Press 1 to search by Licence number')
		print('Press 2 to search by name')
		while True:
			choice = input('Enter your choice (1-4): ')
			if( choice not in {'1', '2'}):
				print('Invalid option. Start over.')
				continue
			else:
				break
		if (choice == 1):
			while True:
				try:
					li_num = int(input('Enter the number to be searched for'))
				#test if valid number
				except ValueError:
					print('Input must be an integer.')
					continue
				if (li_num < 0):
					print("Input must be positive.")
					continue
				else:
					break
			statement = """SELECT p.name, l.licence_no, p.addr, p.birthday, 
			l.class, c.c_id, c.description, l.expiring_date, p.sin
			FROM people p, drive_licence l, driving_condition c, restriction r
			WHERE (LEFT OUTER JOIN l ON p.sin = l.sin) AND (LEFT OUTER JOIN 
			r ON l.licence_no = r.licence_no) AND (LEFT OUTER JOIN c ON 
			r.r_id = c.c_id) AND l.licence_no = '%s'""" %(li_num)
			ReturnData(statement)
		else:
			driver_name = input("Enter driver name: ")
			statement = """SELECT p.name, l.licence_no, p.addr, p.birthday, 
			l.class, c.c_id, c.description, l.expiring_date, p.sin	FROM 
			people p, drive_licence l, driving_condition c, restriction r WHERE 
			(LEFT OUTER JOIN l ON p.sin = l.sin) AND (LEFT OUTER JOIN r ON 
			l.licence_no = r.licence_no) AND (LEFT OUTER JOIN c ON r.r_id 
			= c.c_id) AND UPPER(p.name) = UPPER('%s')""" %(driver_name)
			ReturnData(statement)
	elif(choice==2):
		print('Press 1 to search by Licence number')
		print('Press 2 to search by SIN')
		while True:
			choice = input('Enter your choice (1-4): ')
			if( choice not in {'1', '2'}):
				print('Invalid option. Start over.')
				continue
			else:
				break
		if (choice == 1):
			while True:
				try:
					li_num = int(input('Enter the number to be searched for'))
				#test if valid number
				except ValueError:
					print('Input must be an integer.')
					continue
				if (li_num < 0):
					print("Input must be positive.")
					continue
				else:
					break
			statement = """SELECT t.ticket_no, t.violator_no, t.vehicle_id, 
				 t.office_no, t.vtype, t.vdate, t.place, t.descriptions, type.fine
				 FROM ticket t, ticket_type type, drive_licence drive
				 left outer join ticket_type type on type.vtype = t.vtype AND 
				 left outer drive_licence drive on drive.sin = t.violator_no 
				 AND drive.licence_no = '%s'""" %(li_num)
			ReturnData(statement)
		else:
			while True:
				try: 
					SIN = int(input('Enter the SIN to be searched for'))
				#test if valid number
				except ValueError:
					print('Input must be an integer.')
					continue
				if (SIN < 0):
					print("Input must be positive.")
					continue
				else:
					break
				statement = """SELECT t.ticket_no, t.violator_no, t.vehicle_id, 
				 t.office_no, t.vtype, t.vdate, t.place, t.descriptions, type.fine
				 FROM ticket t, ticket_type type
				 left outer join ticket_type type on type.vtype = t.vtype 
				AND t.violator_no = '%s'""" %(SIN)
				ReturnData(statement)
	elif(choice==3):
		while True:
			v_serial = input('Please enter the VIN to be searched for: ')
			if (len(v_serial)!=15):
				print('VIN must be 15 characters long. Try again.')
				continue
			else:
				break
		statement = """SELECT v.serial_no AS Serial_No, COUNT(DISTINCT transaction_id) AS NumberOfSales, AVG(price) AS AveragePrice, COUNT(DISTINCT t.ticket_no) AS NumberOfTickets
		  FROM vehicle v, auto_sale a, ticket t
		  left outer join ticket t on t.vehicle_id = v.serial_no AND
		  left outer join auto_sale a on a.vehicle_id = v.serial_no AND 
		  UPPER(v.serial_no) = UPPER('%s')
		  GROUP BY v.serial_no""" %(v_serial)
		ReturnData(statement)
	elif(choice==4):
		return 0
	else:
		print("Something went horridly wrong!")
		return 0
