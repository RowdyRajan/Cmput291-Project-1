from helpers import *
import re

def registerVehicle():
	while(True):
		serial_no = input("Enter new vehicle ID: ");
		serial_no = digitAskLoop(serial_no, "Vehicle ID already exits. Please enter a new ID: ", VINExists);
	
		maker = input("Enter vehicle maker: ");
		maker = blankSpaceLoop(maker, "Invalid Maker. Please re-enter: ");

		model = input("Enter vehicle model: ");
		model = blankSpaceLoop(model, "Invalid Model. Please re-enter: ");
		
		year = input("Enter vehicle year: ");
		year = maxWidthDigitChecker(year, 'Invalid year. Please enter again: ',4);		
		
		color = input("Enter vehicle color: ");
		color = blankSpaceLoop(maker, "Invalid Color. Please re-enter: ");
		
		type_id = input("Enter the vehicle type_id: ");
		type_id = digitNotInAskLoop(type_id, "Type_id does not exist. Please enter again: ",typeIDExists );
	
		insertVehicle(serial_no, maker, model, year, color, type_id)	
		
		makePerson(1,serial_no)	
		if yesOrNoChecker("Would you like to enter a secondary owner? [Enter y/n]"):
			makePerson(2,serial_no)
		
		return	


