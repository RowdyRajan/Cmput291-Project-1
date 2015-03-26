from helpers import *

def main():
	while(True):
		serial_no = input("Enter new vehicle ID: ")
		serial_no = digitAskLoop(serial_no, "Vehicle ID already exits. Please enter a new ID: ", VINisIn)
	
		maker = input("Enter vehicle maker: ")
		maker = blackSpaceLoop(maker, "Invalid Maker. Please re-enter: ")

		model = input("Enter vehicle model: ")
		model = blackSpaceLoop(model, "Invalid Model. Please re-enter: ")
		
		year = input("Enter vehicle year: ")
		year = maxWidthDigitChecker(year, 'Invalid year. Please enter again: ',4)		
		color = input("Enter vehicle color: ")
		color = blackSpaceLoop(maker, "Invalid Color. Please re-enter: ")
		type_id = input("Enter the vehicle type_id: ")
		#TODO: Write typeIDExists 
		#type_id = askLoop(type_id, "Invalid type_id. Please enter again: ", typeIDExits)
		
		person = input("Enter the SIN of the new owner")
		person = askLoop(person, 
		
	
def digitAskLoop(answer,askString, confirmFunction):
	while(not answer.isdigit() or confirmFunction(answer)):
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
	return int(answer)
 
def digitChecker(answer, askString):
	while(not answer.isdigit()):
		answer = input(askString)
	return int(answer)

def blankSpaceLoop(answer, askString){
	while answer.isspace():
		answer = input(askString)
	return answer
} 
if __name__ == "__main__":
	main() 
