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
			InsertData
		if(select == 2):
			return


def 

def getInfo():
	pass

	# get licence_no (unique)
		# check if already in database

	# get sin
		# must already exist



if __name__ == '__main__':
	Licence()

