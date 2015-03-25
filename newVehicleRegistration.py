import helpers

def main():
	while(True):
		serial_no = input("Enter new vehicle ID: ");
		serial_no = askLoop(serial_no, "Invalid Vehicle ID. Please enter a new ID: ", VINisIN);
		maker = input("Enter vehicle maker: ");
		model = input("Enter vehicle model: ");
		
		year = input("Enter vehicle year: ");
		year = digitChecker(year, "Invalid year. Please enter again: ")
			
		color = input("Enter vehicle color: ");
	

		type_id = input("Enter the vehicle type_id: ")
		#TODO: Write typeIDExists 
		#type_id = askLoop(type_id, "Invalid type_id. Please enter again: ", typeIDExits);

	
def askLoop(answer,askString, confirmFunction):
	while(not answer.isdigit() or not confirmFunction(answer)):
		answer = input(askString);

	return answer;


def digitChecker(answer, askString, maxNumberSize):
	while(not answer.isdigit()	and len(answer) != maxNumberSize):
		answer = input(askString)
	return int(answer)
 
def digitChecker(answer, askString):
	while(not answer.isdigit()):
		answer = input(askString)
	return int(answer) 
