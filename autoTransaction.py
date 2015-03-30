from helpers import *

def autoTransaction():		
	tran = input("Enter transaction Id: ")
	tran = digitAskLoop(tran, "ID alreay exits. Please enter again", tranIDExists)
	seller_id = None
	buyer_id = None
	v_id = None

	while(True):
		seller_id = input("Enter sellerID")
		seller_id = digitChecker(seller_id, "Not a valid SIN. Please enter again: ")
		if not sinExists(seller_id):
			if not yesOrNoChecker("SIN does not exist. Would you like to make this SIN a person?[y or n]: "):
				continue
			makeSinglePerson(seller_id)
		break

	while(True):
		buyer_id = input("Enter BuyerID")
		buyer_id = digitChecker(buyer_id, "Not a valid SIN. Please enter again: ")
		if not sinExists(buyer_id):
			if not yesOrNoChecker("SIN does not exist. Would you like to make this SIN a person?[y or n]: "):
				continue
			makeSinglePerson(buyer_id)
		break

	while(True):
		v_id = input("Enter vehicle ID")
		v_id = digitChecker(v_id, "Not a valid VID. Please enter again: ")
		if not VINExists(v_id):
			if not yesOrNoChecker("VID does not exist. Would you like to make this SIN a person?[y or n]: "):
				continue
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

			insertVehicle(v_id, maker, model, year, color, type_id)
			break
	
	date = input("Enter sale date: ")	
	date = dateChecker(date )
	
	sale = input("Enter amount of purchase: ")	
	sale = floatChecker(sale, "Invalid amount. Please enter again: ")
	
	insertAutoSale(tran, seller_id, buyer_id,v_id, date, sale)
	return  
	
	
