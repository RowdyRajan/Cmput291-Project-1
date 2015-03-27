from helpers import *

def main():
	while(True):
		serial_no = input("Enter new vehicle ID: ");
		serial_no = digitAskLoop(serial_no, "Vehicle ID already exits. Please enter a new ID: ", VINisIn);
	
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
	
		insertVehicle(serial_no, maker, model, year, color, type_id);	
		
		makePerson(1)	
def digitAskLoop(answer,askString, confirmFunction):
	while(not answer.isdigit() or confirmFunction(answer)):
		if not answer.isdigit():
			answer = input("Not a valid number. Please re-enter:")
		else:
			answer = input(askString);
	return answer;


def digitNotInAskLoop(answer,askString, confirmFunction):
	while(not answer.isdigit() or not confirmFunction(answer)):
		if not answer.isdigit():
			answer = input("Not a valid number. Please re-enter:")
		else:
			answer = input(askString);
	return answer;

def askLoop(answer,askString,confirmFunction):
	while confirmFunction(answer) or answer.isspace():
		answer = input(askString)

def maxWidthDigitChecker(answer, askString, maxNumberSize):
	while(not answer.isdigit()	or len(answer) != maxNumberSize):
		answer = input(askString)
	return answer
 
def digitChecker(answer, askString):
	while(not answer.isdigit()):
		answer = input(askString)
	return answer

def floatChecker(answer, askString):
	
	while(not answer.isdigit()):
		parts = answer.spilt('.')
		if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
			return answer
		answer = input(askString)
	return answer

def blankSpaceLoop(answer, askString):
	while answer.isspace():
		answer = input(askString)
	return answer

def yesOrNoChecker(askString):
	answer = input(askString)
	while answer != 'y' or answer != 'n':
		answer = input("Please enter y or n")

	if answer == 'y':
		return True 
	return False 
	
def makeAPerson(OwnerType):
	
	OwnerTypeMap = { 1 : ["primary owner", 'y'] , 2 : ["secondary owner", 'n']}

	while True:
		SIN = input("Enter the SIN of the new" + ownerTypeMap[OwnerType][0]);
		SIN = digitChecker(SIN, "Not a valid SIN. Please enter again");
			
		if not sinExists(SIN):
			if not yesOrNoChecker("SIN does not exist. Would you like to make this SIN a person?[y or n]"):	 
				continue
			
			name = input("Enter the persons name")
			name = blankSpaceLoop(name, "Blank Name. Please enter something")
			
						 				
			height = input("Enter the person's height")
			height = floatChecker(height, "Invalid number. Please enter again")

			weight = input("Enter the person's weight")
            weight = floatChecker(weight ,"Invalid number. Please enter again")
			eyecolor  = input("Enter the person's eyecolor")
            eyecolor = blankSpaceLoop(eyecolor ,"Blank entree. Please enter something")

			addr  = input("Enter the person's address")
			addr = blankSpaceLoop(addr ,"Blank entree. Please enter something")
			
						
			gender  = input("Enter the person's gender")
			while answer != 'm' or answer != 'f':
				gender = input("Please enter m or f")

			

if __name__ == "__main__":
	main() 
