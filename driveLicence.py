# Driver Licence Registration
"""
Driver Licence Registration

This component is used to record the information needed to issuing a drive licence, 
including the personal information and a picture for the driver. 
You may assume that all the image files are stored in a local disk system.

CREATE TABLE drive_licence (
  licence_no      CHAR(15),
  sin             char(15),
  class           VARCHAR(10),
  photo           BLOB,
  issuing_date    DATE,
  expiring_date   DATE,
  PRIMARY KEY (licence_no),
  UNIQUE (sin),
  FOREIGN KEY (sin) REFERENCES people
        ON DELETE CASCADE

"""

from helpers import *

def License():
	print("Welcome to the driver's licence licensing agency. Here you can add a new drivers licence to the system")
	while(1):
		print("1: Enter New Licence")
		print("2: Return to Main Menu.")
		try:
			select = int(input())
		except:
			print('Invalid option. Try again.')
			continue

		if(select == 1):
			InsertData()
		if(select == 2):
			return


def getInfo():

	licNo = None
	SIN = None
	licClass = None
	photo = None
	issuingDate = None
	expireDate = None

	while True:
		if(licNo == None):
			licNo = input("Licence number: ")
			if(len(licNo)>15):
				print("Licence number too long")
				if(tryAgain()):
					licNo = None
					continue
				else:
					return None
			if( licenceExists(licNo) ):
				print("Duplicate licence number in database.")
				if(tryAgain()):
					licNo = None
					continue
				else:
					return None
			
		if(SIN == None):
			SIN = input("SIN: ")
			if( sinExists(SIN) == False):
				print("No record of person in Database, please try again.")
				if(tryAgain()):
					SIN = None
					continue
				else:
					return None
			

		if(licClass == None):
			licClass = input("Licence Class: ")
			if(len(licNo)>10):
				print("Class entry too long")
				if(tryAgain()):
					licClass = None
					continue
				else:
					return None
			
			
		if(photo == None):
			photoPath = input("Local image file including path and extention: ")
			#Load image into memory from local file 
			#(Assumes a file by this name exists in the directory you are running from)
			f_image  = open(photoPath,'rb')
			image  = f_image.read()

			cursor.setinputsizes(image=cx_Oracle.LONG_BINARY)

			insert = "insert into pictures (photo_id, title, place, image) values (:photo_id, :title, :place, :image)"

			cursor.execute(insert,{'photo_id':pid, 'title':title,'place':place, 'image':image})



			statement = "SELECT v.photo FROM ticket_type v WHERE (v.photo) = ('%s')" % (photo)
			if( InDB(statement) == False ):
				print("Invalid violation type, please re-enter.")
				if(tryAgain()):
					photo = None
					continue
				else:
					return None
								
		if(issuingDate == None):
			issuingDate = input("Issuing Date (eg. yyyy/mm/dd): ").strip()
			issuingDate = dateChecker(issuingDate)

		if(expireDate == None):
			expireDate = input("Expiry Date (eg. yyyy/mm/dd): ").strip()
			expireDate = dateChecker(expireDate)

		insertLicence(licNo, SIN, licClass, photo, issuingDate, expireDate)

		print("Would you like to enter a restriction?:")


		return


def tryAgain():
	# Possible helper function to repeat input attempt			
	print("Try again? (Y/N):\n\r")
	while(1):
		ans = input().strip().lower()
		if ans in ("yes", "y"):
			return True
		if ans in ("no", "n"):
			return False



if __name__ == '__main__':
	Licence()

