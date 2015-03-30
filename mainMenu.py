#!/usr/bin/python3
#Main menu - provides Five options to operate on the database
from helpers import connect
from newVehicleRegistration import registerVehicle
#from autoTransactionFile import autoTransaction
from driveLicence import start_license
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
			choice = input('Enter your choice (1-6): ')
			if choice not in {'1', '2', '3', '4', '5', '6'}:
				print('Invalid option. Try again.')
				continue
			else:
				break
		if (choice=='1'):
			registerVehicle()
		elif (choice == '2'):
			pass
			#autoTransaction()
		elif (choice == '3'):
			start_license()
			#licenceRegistration
		elif (choice == '4'):
			VR_Start()
		elif (choice == '5'):
			search()
		elif (choice == '6'):
			#leave program
			global connection
			exit()
		else:
			print('Something went wrong. Exiting.')
			exit()

if __name__ == '__main__':
#prompt user to connect to database
	connect()
	main()
