#!/usr/bin/python3
#Main menu - provides Five options to operate on the database
from helpers import connect
from newVehicleRegistration import registerVehicle
#from autoTransactionFile import autoTransaction
#from licenceRegistrationFile import licenceRegistration
from violationRecord import VR_Start
from search import search

def main():
	while True:
		print('1. New Vehicle Registration')
		print('2. Auto Transaction')
		print('3. Driver Licence Registration')
		print('4. Violation Record')
		print('5. Search Engine')
		print('6. Exit')
		while True:
			choice = input('Enter your choice (1-4): ')
			if choice not in {'1', '2', '3', '4', '5', '6'}:
				print('Invalid option. Try again.')
				continue
			else:
				break
		if (choice=='1'):
			registerVehicle()
		elif (choice == '2'):
			#autoTransaction()
		elif (choice == '3'):
			#licenceRegistration
		elif (choice == '4'):
			VR_Start()
		elif (choice == '5'):
			search()
		elif (choice == '6'):
			#leave program
			return 0
		else:
			print('Something went wrong. Exiting.')
			return 1

if __name__ == '__main__':
#prompt user to connect to database
	connect()
	main()
