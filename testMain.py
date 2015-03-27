# A test program to complie various other applications.

import cx_Oracle
from helpers import connect
from violationRecord import VR_Start

def main():

	menu = ["1: New Vehicle Registration",\
			"2: Auto Transaction",\
			"3: Driver Licence Registration",\
			"4: Add Violation Record",\
			"5: Search Engine",\
			"6: Exit"]

	while(1):
		print("Welcome to Python Database Program!")
		for option in menu:
			print(option)
		select = input("Please select program (1-6): ")

		if select not in {1, 2, 3, 4, 5, 6}:
			print('Invalid option. Try again.')
			continue

		if(select == 1):
			print("you typed", select)
		if(select == 2):
			print("you typed", select)
		if(select == 3):
			print("you typed", select)
		if(select == 4):
			VR_Start()
		if(select == 5):
			print("you typed", select)
		if(select == 6):
			exit()


if __name__ == '__main__':
	connect()
	main()