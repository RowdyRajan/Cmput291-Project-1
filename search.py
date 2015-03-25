#!/usr/bin/python3
#Search Engine
#List name, licence_no, addr, driving class, driving_condition and expiring_date
#by entering license_no or a given name. Display all duplicates.
#
#List violation records received by a person if the licence_no or sin is entered
#
#Print vehicle history - #times been sold, average price, #violations it has 
#based on VIN
def search():
	println('1. Licence information')
	println('2. Violation records')
	println('3. Vehicle history')
	println('4. Go back to main menu')
	choice = input('Enter your choice (1-4): ')
	while True:
		if input not in {'1', '2', '3', '4'}:
			println('Invalid option. Try again.')
			continue
		else:
			break

	if (input==1):
		println('Press 1 to search by Licence number')
		println('Press 2 to search by name')
		while True:
			choice = input('Enter your choice (1-4): ')
			if( choice not in {'1', '2'}):
				println('Invalid option. Start over.')
				continue
			else:
				break
		if (choice == 1):
			while True:
				li_num = input('Enter the number to be searched for')
				#test if valid number
		
