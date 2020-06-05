import mysql.connector
import os
import subprocess as sp
from prettytable import PrettyTable
import re

mydb = mysql.connector.connect(
	host="localhost",
	user="monie",
	passwd="1111"
)

cursor = mydb.cursor()
cursor.execute("USE Flights")

mailregex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
dateregex = r'^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$'
fareregex = r"^\$?\-?([1-9]{1}[0-9]{0,2}(\,\d{3})*(\.\d{0,2})?|[1-9]{1}\d{0,}(\.\d{0,2})?|0(\.\d{0,2})?|(\.\d{1,2}))$|^\-?\$?([1-9]{1}\d{0,2}(\,\d{3})*(\.\d{0,2})?|[1-9]{1}\d{0,}(\.\d{0,2})?|0(\.\d{0,2})?|(\.\d{1,2}))$|^\(\$?([1-9]{1}\d{0,2}(\,\d{3})*(\.\d{0,2})?|[1-9]{1}\d{0,}(\.\d{0,2})?|0(\.\d{0,2})?|(\.\d{1,2}))\)$"
timeregex = r'(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)'

def checkMail(email):  
   
    if(re.search(mailregex,email)):  
        return True 
          
    else:  
        return False

def checkDate(date):

	if(re.search(dateregex,date)):
		return True

	else:
		return False

def checkTime(time):

	if(re.search(timeregex,time)):
		return True

	else:
		return False

def checkFare(fare):

	if(re.search(fareregex,fare)):
		return True
	else:
		return False

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

def createPassenger():

	tmp = sp.call('clear',shell=True)

	print("\nCreate a new passenger record below: \n")
	cnic_pass = raw_input("Please enter CNIC: ")

	while(cnic_pass.isdigit() == False):

		print("\nInvalid Customer ID. Please try again.\n")
		cnic_pass = raw_input("Please enter CNIC: ")

	while(len(cnic_pass) != 11):

		print("\nInvalid Customer ID. Please try again.\n")
		cnic_pass = raw_input("Please enter CNIC: ")


	name_pass = raw_input("Please enter full name: ")

	while(len(name_pass) > 255) == True:

		print("\nInvalid Customer Name. Please try again.\n")
		name_pass = raw_input("Please enter full name: ")

	while(hasNumbers(name_pass) == True):

		print("\nInvalid name.\n")
		name_pass = raw_input("Please enter name: ")

	mail_pass = raw_input("Please enter email address: ")

	while(checkMail(mail_pass) == False):

		print("\nInvalid Email.\n")
		mail_pass = raw_input("Please enter email address: ")

	age_pass = raw_input("Please enter age: ")

	while(age_pass.isdigit() == False):

		print("\nInvalid Age Format. Please try again.\n")
		age_pass = raw_input("Please enter age: ")

	add_pass = raw_input("Please enter address: ")

	while(len(add_pass) > 255) == True:

		print("\nInvalid Customer Name. Please try again.\n")
		add_pass = raw_input("Please enter full name: ")	

	gender_pass = raw_input("Please enter gender: ")

	while(gender_pass != 'M' and gender_pass != 'F'):

		print("\nInvalid Customer Gender. Please try again.\n")
		gender_pass = raw_input("Please enter gender: ")

	nat_pass = raw_input("Please enter nationality: ")

	while(hasNumbers(nat_pass) == True):

		print("\nInvalid Nationality.\n")
		nat_pass = raw_input("Please enter nationality: ")

	phone_pass = raw_input("Please enter phone: ")

	while(phone_pass.isdigit() == False):

		print("\nInvalid Customer Contact. Please try again.\n")
		phone_pass = raw_input("Please enter phone: ")

	while(len(phone_pass) != 11):

		print("\nInvalid Customer Contact. Please try again.\n")
		phone_pass = raw_input("Please enter phone: ")

	cursor = mydb.cursor()

	insertions = "INSERT INTO PASSENGER (cust_id,name,email,age,address,gender,nationality,contact) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
	values = (cnic_pass,name_pass,mail_pass,age_pass,add_pass,gender_pass,nat_pass,phone_pass)

	cursor.execute(insertions,values)
	mydb.commit()

	print("A new passenger record successfully created.")

def updateName(cust_id):

	tmp = sp.call('clear',shell=True)

	print("\nUpdate name of an existing passenger record: \n")

	new_name = raw_input("Enter the new name: ")

	while(len(new_name) > 255) == True:

		print("\nInvalid Customer Name. Please try again.\n")
		new_name = raw_input("Please enter full name: ")

	updation = "UPDATE PASSENGER SET name = %s WHERE cust_id = %s"
	updated_insert = (new_name,cust_id)

	cursor.execute(updation,updated_insert)
	mydb.commit()

	print("\nPassenger details have been updated.")

def updatePhone(cust_id):

	tmp = sp.call('clear',shell=True)

	print("\nUpdate contact of an existing passenger record: \n")

	new_num = raw_input("Enter the new number: ")

	while(new_num.isdigit() == False):

		print("\nInvalid Customer Contact. Please try again.\n")
		new_num = raw_input("Please enter phone: ")

	while(len(new_num) != 11):

		print("\nInvalid Customer Contact. Please try again.\n")
		new_num = raw_input("Please enter phone: ")

	updation = "UPDATE PASSENGER SET contact = %s WHERE cust_id = %s"
	updated_insert = (new_num,cust_id)

	cursor.execute(updation,updated_insert)
	mydb.commit()

	print("\nPassenger details have been updated.")

def updateAddress(cust_id):

	tmp = sp.call('clear',shell=True)

	print("\nUpdate address of an existing passenger record: \n")

	new_add = raw_input("Enter the new address: ")

	while(len(new_add) > 255) == True:

		print("\nInvalid Customer Name. Please try again.\n")
		new_add = raw_input("Please enter full name: ")

	updation = "UPDATE PASSENGER SET address = %s WHERE cust_id = %s"
	updated_insert = (new_add,cust_id)

	cursor.execute(updation,updated_insert)
	mydb.commit()

	print("\nPassenger details have been updated.")

def updateNationality(cust_id):

	tmp = sp.call('clear',shell=True)

	print("\nUpdate nationality of an existing passenger record: \n")

	new_nat = raw_input("Enter the new nationality: ")

	while(hasNumbers(new_nat) == True):

		print("\nInvalid Nationality.\n")
		new_nat = raw_input("Please enter nationality: ")

	updation = "UPDATE PASSENGER SET nationality = %s WHERE cust_id = %s"
	updated_insert = (new_nat,cust_id)

	cursor.execute(updation,updated_insert)
	mydb.commit()

	print("\nPassenger details have been updated.")

def viewFlights(depart_aircode,arrive_aircode,depart_date,arrive_date):

	tmp = sp.call('clear',shell=True)
	
	print("\nView all available flights in a particular time period:\n")

	show = "SELECT * FROM FLIGHT WHERE depart_aircode = %s and arrive_aircode = %s and depart_date >= %s and arrive_date <= %s"
	result = (depart_aircode,arrive_aircode,depart_date,arrive_date)

	cursor.execute(show,result)

	y = PrettyTable()
	y.field_names = ["flight_id","depart_time","arrive_time","depart_date","arrive_date","depart_aircode","arrive_aircode","airplane_code","status","fare"]

	for i in cursor:

		y.add_row(i)
		
	print(y)

def ticketRecord():

	tmp = sp.call('clear',shell=True)

	print("\nGenerate ticket record for a particular passenger for a particular flight.\n")

	book_id = raw_input("Please enter the booking ID: ")

	while(book_id.isdigit() == False):

		print("\nInvalid Booking ID. Please try again.\n")
		book_id = raw_input("Please enter the booking ID: ")

	while(len(book_id) != 5):

		print("\nInvalid Booking ID. Please try again.\n")
		book_id = raw_input("Please enter the booking ID: ")

	print("\nUse those passenger ID's which are in the passenger table.")

	pass_id = raw_input("Please enter the passenger's CNIC: ")

	while(pass_id.isdigit() == False):

		print("\nInvalid Customer ID. Please try again.\n")
		pass_id = raw_input("Please enter CNIC: ")

	while(len(pass_id) != 11):

		print("\nInvalid Customer ID. Please try again.\n")
		pass_id = raw_input("Please enter CNIC: ")

	print("\nUse those flight ID's which are in the flights table.")

	flight = raw_input("Please enter the flight ID: ")

	while(flight.isdigit() == False):

		print("\nInvalid Flight ID. Please try again.\n")
		flight = raw_input("Please enter the flight ID: ")

	while(len(flight) != 5):

		print("\nInvalid Flight ID. Please try again.\n")
		flight = raw_input("Please enter the flight ID: ")

	flight_class = raw_input("Please enter the flight class: ")

	while(hasNumbers(flight_class) == True):

		print("\nInvalid class.\n")
		flight_class = raw_input("Please enter class: ")

	flight_fare = raw_input("Please enter the flight fare: ")

	while(checkFare(flight_fare) == False):

		print("\nInvalid Fare.\n")
		flight_fare = raw_input("Please enter fare again: ")

	cursor = mydb.cursor()

	insertions = "INSERT INTO BOOKING (booking_id,cust_id,flight_id,class,fare) VALUES (%s,%s,%s,%s,%s)"
	values = (book_id,pass_id,flight,flight_class,flight_fare)

	cursor.execute(insertions,values)
	mydb.commit()

	print("\nTicket record has been successfully generated.\n")

def viewHistory(cust_id):

	tmp = sp.call('clear',shell=True)

	show = "SELECT booking_id,flight_id,class,fare FROM BOOKING WHERE cust_id = %s"

	cursor.execute(show,(cust_id,))

	y = PrettyTable()
	y.field_names = ["booking_id","flight_id","class","fare"]

	for i in cursor:

		y.add_row(i)
		
	print(y)


def cheapFlight(depart_aircode,arrive_aircode):

	tmp = sp.call('clear',shell=True)

	cheaps = "SELECT flight_id,depart_aircode,arrive_aircode,fare FROM FLIGHT WHERE fare = (SELECT min(fare) FROM FLIGHT WHERE depart_aircode = %s and arrive_aircode = %s)"
	result = (depart_aircode,arrive_aircode)

	cursor.execute(cheaps,result)
	
	y = PrettyTable()
	y.field_names = ["flight_id","depart_aircode","arrive_aircode","fare"]

	for i in cursor:

		y.add_row(i)
		
	print(y)

def cancelBooking(booking_id):

	tmp = sp.call('clear',shell=True)

	cancel = "DELETE FROM BOOKING WHERE booking_id = %s"

	cursor.execute(cancel,(booking_id,))

	mydb.commit()

	print("\nThe respective booking has been cancelled.")

# Functions for Question 4 start from this point onward.

def createFlight():

	tmp = sp.call('clear',shell=True)

	print("\nAdd a new flight record, with the required details.\n")

	flight = raw_input("Please enter the flight ID: ")

	while(flight.isdigit() == False):

		print("\nInvalid Flight ID. Please try again.\n")
		flight = raw_input("Please enter the flight ID: ")

	while(len(flight) != 5):

		print("\nInvalid Flight ID. Please try again.\n")
		flight = raw_input("Please enter the flight ID: ")

	d_time = raw_input("Please enter the departure time: ")

	while(checkTime(d_time) == False):

		print("\nInvalid time.\n")
		d_time = raw_input("Please enter the departure time: ")

	a_time = raw_input("Please enter the arrival time: ")

	while(checkTime(a_time) == False):

		print("\nInvalid time.\n")
		a_time = raw_input("Please enter the arrival time: ")

	d_date = raw_input("Please enter the departure date: ")

	while(checkDate(d_date) == False):

		print("\nInvalid Date.\n")
		d_date = raw_input("Please enter the departure date: ")

	a_date = raw_input("Please enter the arrival date: ")

	while(checkDate(a_date) == False):

		print("\nInvalid Date.\n")
		a_date = raw_input("Please enter the arrival date: ")

	while((a_date < d_date) == True):

		print("\nYour arrival date is less than your departure date. Typo? Try again.")
		a_date = raw_input("Please enter the arrival date: ")

	d_code = raw_input("Please enter the departure airport code: ")
	a_code = raw_input("Please enter the arrival airport code: ")

	print("\nUse airplane codes only from the airplane table.")
	plane_code = raw_input("Please enter the airplane code: ")
	f_status = raw_input("Please enter the flight's status: ")

	while(hasNumbers(f_status) == True):

		print("\nInvalid status.\n")
		f_status = raw_input("Please enter status: ")

	flight_fare = raw_input("Please enter the flight fare: ")

	while(checkFare(flight_fare) == False):

		print("\nInvalid Fare.\n")
		flight_fare = raw_input("Please enter fare again: ")

	cursor = mydb.cursor()

	insertions = "INSERT INTO FLIGHT (flight_id,depart_time,arrive_time,depart_date,arrive_date,depart_aircode,arrive_aircode,airplane_code,status,fare) VALUES (%s,%s,%s,%s,%s,%s,%s,(SELECT airplane_code FROM AIRPLANE WHERE airplane_code = %s),%s,%s)"
	values = (flight,d_time,a_time,d_date,a_date,d_code,a_code,plane_code,f_status,flight_fare)

	cursor.execute(insertions,values)
	mydb.commit()

	print("\nA new flight record successfully created.")

def updateDepartTime(flight_id):

	new_dep = raw_input("Enter the new departure time: ")

	while(checkTime(new_dep) == False):

		print("\nInvalid time.\n")
		new_dep = raw_input("Please enter the departure time: ")

	updation = "UPDATE FLIGHT SET depart_time = %s WHERE flight_id = %s"
	updated_insert = (new_dep,flight_id)

	cursor.execute(updation,updated_insert)
	mydb.commit()

	print("\nFlight record has been updated.")

def updateArriveTime(flight_id):

	new_arr = raw_input("Enter the new arrival time: ")

	while(checkTime(new_arr) == False):

		print("\nInvalid time.\n")
		new_arr = raw_input("Please enter the arrival time: ")


	updation = "UPDATE FLIGHT SET arrive_time = %s WHERE flight_id = %s"
	updated_insert = (new_arr,flight_id)

	cursor.execute(updation,updated_insert)
	mydb.commit()

	print("\nFlight record has been updated.")

def updateDepartAirport(flight_id):

	new_dair = raw_input("Enter the new departure airport code: ")

	updation = "UPDATE FLIGHT SET depart_aircode = %s WHERE flight_id = %s"
	updated_insert = (new_dair,flight_id)

	cursor.execute(updation,updated_insert)
	mydb.commit()

	print("\nFlight record has been updated.")

def updateArriveAirport(flight_id):

	new_aair = raw_input("Enter the new arrival airport code: ")

	updation = "UPDATE FLIGHT SET arrive_aircode = %s WHERE flight_id = %s"
	updated_insert = (new_aair,flight_id)

	cursor.execute(updation,updated_insert)
	mydb.commit()

	print("\nFlight record has been updated.")

def updateDepartDate(flight_id):

	new_ddate = raw_input("Enter the new departure date: ")

	while(checkDate(new_ddate) == False):

		print("\nInvalid Date.\n")
		new_ddate = raw_input("Please enter the departure date: ")

	updation = "UPDATE FLIGHT SET depart_date = %s WHERE flight_id = %s"
	updated_insert = (new_ddate,flight_id)

	cursor.execute(updation,updated_insert)
	mydb.commit()

	print("\nFlight record has been updated.")

def updateArriveDate(flight_id):

	new_adate = raw_input("Enter the new arrival date: ")

	while(checkDate(new_adate) == False):

		print("\nInvalid Date.\n")
		new_adate = raw_input("Please enter the arrival date: ")

	updation = "UPDATE FLIGHT SET arrive_date = %s WHERE flight_id = %s"
	updated_insert = (new_adate,flight_id)

	cursor.execute(updation,updated_insert)
	mydb.commit()

	print("\nFlight record has been updated.")

def updateStatus(flight_id):

	new_stat = raw_input("Enter the new flight status: ")

	while(hasNumbers(new_stat) == True):

		print("\nInvalid status.\n")
		new_stat = raw_input("Please enter status: ")

	updation = "UPDATE FLIGHT SET status = %s WHERE flight_id = %s"
	updated_insert = (new_stat,flight_id)

	cursor.execute(updation,updated_insert)
	mydb.commit()

	print("\nFlight record has been updated.")

def updateFare(flight_id):

	new_fare = raw_input("Enter the new flight fare: ")

	while(checkFare(new_fare) == False):

		print("\nInvalid Fare.\n")
		new_fare = raw_input("Please enter fare again: ")

	updation = "UPDATE FLIGHT SET fare = %s WHERE flight_id = %s"
	updated_insert = (new_fare,flight_id)

	cursor.execute(updation,updated_insert)
	mydb.commit()

	print("\nFlight record has been updated.")

def cancelFlight(flight_id):

	tmp = sp.call('clear',shell=True)

	cancel1 = "DELETE FROM FLIGHT WHERE flight_id = %s"

	cursor.execute(cancel1,(flight_id,))

	mydb.commit()

	print("\nThe respective flight has been cancelled.")

def flightsOnDay(depart_aircode,arrive_aircode,depart_date,arrive_date):

	tmp = sp.call('clear',shell=True)

	show = "SELECT * FROM FLIGHT WHERE depart_aircode = %s or arrive_aircode = %s and depart_date = %s or arrive_date = %s"
	result = (depart_aircode,arrive_aircode,depart_date,arrive_date)

	cursor.execute(show,result)
	
	y = PrettyTable()
	y.field_names = ["flight_id","depart_time","arrive_time","depart_date","arrive_date","depart_aircode","arrive_aircode","airplane_code","status","fare"]

	for i in cursor:

		y.add_row(i)
		
	print(y)

def viewTables():

	tmp = sp.call('clear',shell=True)

	# Printing Passengers Table

	print("Passengers Table: \n")

	passengers = "SELECT * FROM PASSENGER"

	cursor.execute(passengers)

	passTable = PrettyTable()
	passTable.field_names = ["cust_id","name","email","age","address","gender","nationality","contact"]

	for i in cursor:

		passTable.add_row(i)

	print(passTable)
	print("\n")

	# Printing Bookings Table

	print("Bookings Table: \n")

	bookings = "SELECT * FROM BOOKING"

	cursor.execute(bookings)

	bookTable = PrettyTable()
	bookTable.field_names = ["booking_id","cust_id","flight_id","class","fare"]

	for i in cursor:

		bookTable.add_row(i)

	print(bookTable)
	print("\n")

	# Printing Flights Table

	print("Flights Table: \n")

	flights = "SELECT * FROM FLIGHT"

	cursor.execute(flights)

	flyTable = PrettyTable()
	flyTable.field_names = ["flight_id","depart_time","arrive_time","depart_date","arrive_date","depart_aircode","arrive_aircode","airplane_code","status","fare"]

	for i in cursor:

		flyTable.add_row(i)

	print(flyTable)	
	print("\n")

	# Printing Airplane Table

	print("Airplane Table: \n")

	air = "SELECT * FROM AIRPLANE"

	cursor.execute(air)

	airTable = PrettyTable()
	airTable.field_names = ["airplane_code","airline_id","capacity","model"]

	for i in cursor:

		airTable.add_row(i)

	print(airTable)	
	print("\n")


# MAIN INTERFACE

user = "moniex"
user_pass = "moniex"

admin = "momin"
admin_pass = "momin"


def selectPerson():

	tmp = sp.call('clear',shell=True)

	print("\nWelcome aboard! What do you want to login as?\n 1. Receptionist\n 2. Administrator")

	person = input("\nSelect your option: ")

	if person == 1:
		
		print("\nPlease enter your login details: \n\n")

		username = raw_input("Username: ")

		while(username != "moniex"):

			print("\nIncorrect username. Please try again!")
			username = raw_input("\nUsername: ")

		password = raw_input("Password: ")

		while(password != "moniex"):

			print("\nIncorrect password. Please try again!")
			password = raw_input("\nPassword: ")

		return True

	elif person == 2:

		print("\nPlease enter your login details: \n\n")

		username = raw_input("Username: ")

		while(username != "momin"):

			print("\nIncorrect username. Please try again!")
			username = raw_input("\nUsername: ")

		password = raw_input("Password: ")

		while(password != "momin"):

			print("\nIncorrect password. Please try again!")
			password = raw_input("\nPassword: ")	

		return False

outer_opt = selectPerson()

if outer_opt:

	tmp = sp.call('clear',shell=True)

	print("\n\t\t\tAIRLINE RESERVATION SYSTEM")
	print("\n\t\t\tLogged in as Receptionist\n")
	print("Select your option: \n")

	print("1: Create a new passenger record.\n")
	print("2: Update details of an existing passenger record.\n")
	print("3: View all available flights in a particular time period.\n")
	print("4: Generate ticket record for a particular passenger for a particular flight.\n")
	print("5: View the cheapest flight.\n")
	print("6: View flight history of a particular passenger.\n")
	print("7: Cancel a particular ticket record.\n")
	print("8: Quit.\n\n")

	user_choice = input("Enter your option: ")

	if(user_choice == 1):

		createPassenger()

	elif(user_choice == 2):

		tmp = sp.call('clear',shell=True)
			
		print("\n1: Update Name. \n")
		print("2: Update Contact. \n")
		print("3: Update Address. \n")
		print("4: Update Nationality. \n")

		opt = input("Select your option: ")

		if opt == 1:
			cust_id = raw_input("Input the Customer ID of the passenger: ")
			
			while(cust_id.isdigit() == False):

				print("\nInvalid Customer ID. Please try again.\n")
				cust_id = raw_input("Please enter CNIC: ")

			while(len(cust_id) != 11):

				print("\nInvalid Customer ID. Please try again.\n")
				cust_id = raw_input("Please enter CNIC: ")

			updateName(cust_id)

		elif opt == 2:
			cust_id = raw_input("Input the Customer ID of the passenger: ")

			while(cust_id.isdigit() == False):

				print("\nInvalid Customer ID. Please try again.\n")
				cust_id = raw_input("Please enter CNIC: ")

			while(len(cust_id) != 11):

				print("\nInvalid Customer ID. Please try again.\n")
				cust_id = raw_input("Please enter CNIC: ")

			updatePhone(cust_id)

		elif opt == 3:
			cust_id = raw_input("Input the Customer ID of the passenger: ")

			while(cust_id.isdigit() == False):

				print("\nInvalid Customer ID. Please try again.\n")
				cust_id = raw_input("Please enter CNIC: ")

			while(len(cust_id) != 11):

				print("\nInvalid Customer ID. Please try again.\n")
				cust_id = raw_input("Please enter CNIC: ")

			updateAddress(cust_id)

		elif opt == 4:
			cust_id = raw_input("Input the Customer ID of the passenger: ")

			while(cust_id.isdigit() == False):

				print("\nInvalid Customer ID. Please try again.\n")
				cust_id = raw_input("Please enter CNIC: ")

			while(len(cust_id) != 11):

				print("\nInvalid Customer ID. Please try again.\n")
				cust_id = raw_input("Please enter CNIC: ")

			updateNationality(cust_id)

		else:
			print("\nInvalid option. Goodbye!")
			
	elif(user_choice == 3):

		depart_code = raw_input("\nInput the departure airport IATA code: ")
		arrive_code = raw_input("Input the arrival airport IATA code: ")
		dep_date = raw_input("\nInput the departure date: ")

		while(checkDate(dep_date) == False):

			print("\nInvalid Date.\n")
			dep_date = raw_input("Please enter the departure date: ")

		arr_date = raw_input("Input the arrival date: ")


		while(checkDate(arr_date) == False):

			print("\nInvalid Date.\n")
			arr_date = raw_input("Please enter the arrival date: ")

		while((arr_date < dep_date) == True):

			print("\nYour arrival date is less than your departure date. Typo? Try again.")
			arr_date = raw_input("Please enter the arrival date: ")

		viewFlights(depart_code,arrive_code,dep_date,arr_date)

	elif(user_choice == 4):

		ticketRecord()

	elif(user_choice == 5):

		depart_code = raw_input("\nInput the departure airport IATA code: ")
		arrive_code = raw_input("Input the arrival airport IATA code: ")

		cheapFlight(depart_code,arrive_code)

	elif (user_choice == 6):
			cust_id = raw_input("Input the Customer ID of the passenger: ")

			while(cust_id.isdigit() == False):

				print("\nInvalid Customer ID. Please try again.\n")
				cust_id = raw_input("Please enter CNIC: ")

			while(len(cust_id) != 11):

				print("\nInvalid Customer ID. Please try again.\n")
				cust_id = raw_input("Please enter CNIC: ")

			viewHistory(cust_id)

	elif(user_choice == 7):

		booking_id = raw_input("Input the Booking ID that needs to be cancelled: ")

		while(booking_id.isdigit() == False):

			print("\nInvalid Booking ID. Please try again.\n")
			booking_id = raw_input("Please enter the booking ID: ")

		cancelBooking(booking_id)

	elif(user_choice == 8):

		print("Wishing to see you again soon :(.\n")


else:

	tmp = sp.call('clear',shell=True)

	print("\n\t\t\tAIRLINE RESERVATION SYSTEM")
	print("\n\t\t\tLogged in as Administrator\n")
	print("Select your option: \n")

	print("1: Create a new flight record.\n")
	print("2: Update details of an existing flight record.\n")
	print("3: Cancel a particular flight record.\n")
	print("4: View all flights landing and taking off for a particular airport on that day.\n")
	print("5: View every table of the database in tabular form.\n")
	print("6: Quit.\n")

	user_choice = input("Enter your option: ")

	if user_choice == 1:

		createFlight()

	elif user_choice == 2:

		tmp = sp.call('clear',shell=True)

		print("\n1: Update Departure Time. \n")
		print("2: Update Arrival Time. \n")
		print("3: Update Departure Airport Code. \n")
		print("4: Update Arrival Airport Code. \n")
		print("5: Update Flight Status. \n")
		print("6: Update Flight Fare. \n")
		print("7: Update Departure Date. \n")
		print("8: Update Arrival Date. \n")

		opt = input("Select your option: ")

		if opt == 1:

			tmp = sp.call('clear',shell=True)
			flight_id = raw_input("Input the Flight ID: ")

			while(flight_id.isdigit() == False):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			while(len(flight_id) != 5):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			updateDepartTime(flight_id)

		elif opt == 2:

			tmp = sp.call('clear',shell=True)
			flight_id = raw_input("Input the Flight ID: ")

			while(flight_id.isdigit() == False):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			while(len(flight_id) != 5):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			updateArriveTime(flight_id)

		elif opt == 3:

			tmp = sp.call('clear',shell=True)
			flight_id = raw_input("Input the Flight ID: ")

			while(flight_id.isdigit() == False):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			while(len(flight_id) != 5):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			updateDepartAirport(flight_id)

		elif opt == 4:

			tmp = sp.call('clear',shell=True)
			flight_id = raw_input("Input the Flight ID: ")

			while(flight_id.isdigit() == False):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			while(len(flight_id) != 5):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			updateArriveAirport(flight_id)

		elif opt == 5:

			tmp = sp.call('clear',shell=True)
			flight_id = raw_input("Input the Flight ID: ")

			while(flight_id.isdigit() == False):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			while(len(flight_id) != 5):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			updateStatus(flight_id)

		elif opt == 6:

			tmp = sp.call('clear',shell=True)
			flight_id = raw_input("Input the Flight ID: ")

			while(flight_id.isdigit() == False):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			while(len(flight_id) != 5):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			updateFare(flight_id)

		elif opt == 7:

			tmp = sp.call('clear',shell=True)
			flight_id = raw_input("Input the Flight ID: ")

			while(flight_id.isdigit() == False):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			while(len(flight_id) != 5):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			updateDepartDate(flight_id)

		elif opt == 8:

			tmp = sp.call('clear',shell=True)
			flight_id = raw_input("Input the Flight ID: ")

			while(flight_id.isdigit() == False):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			while(len(flight_id) != 5):

				print("\nInvalid Flight ID. Please try again.\n")
				flight_id = raw_input("Please enter the flight ID: ")

			updateArriveDate(flight_id)

		else:
			print("\nInvalid option. Goodbye!")

	elif(user_choice == 3):

		flight_id = raw_input("Input the Flight ID that needs to be cancelled: ")

		while(flight_id.isdigit() == False):

			print("\nInvalid Flight ID. Please try again.\n")
			flight_id = raw_input("Please enter the flight ID: ")

		while(len(flight_id) != 5):

			print("\nInvalid Flight ID. Please try again.\n")
			flight_id = raw_input("Please enter the flight ID: ")

		cancelFlight(flight_id)

	elif(user_choice == 4):

		tmp = sp.call('clear',shell=True)
		depart_code = raw_input("\nInput the departure airport IATA code: ")
		arrive_code = raw_input("Input the arrival airport IATA code: ")

		while(depart_code != arrive_code):

			print("\nIATA code should be the same since we are considering this for one particular airport.")
			depart_code = raw_input("\nInput the departure airport IATA code: ")
			arrive_code = raw_input("Input the arrival airport IATA code: ")

		dep_date = raw_input("\nInput the departure date: ")

		while(checkDate(dep_date) == False):

			print("\nInvalid Date.\n")
			dep_date = raw_input("Please enter the departure date: ")

		arr_date = raw_input("Input the arrival date: ")

		while(checkDate(arr_date) == False):

			print("\nInvalid Date.\n")
			arr_date = raw_input("Please enter the arrival date: ")

		while((arr_date < dep_date) == True):

			print("\nYour arrival date is less than your departure date. Typo? Try again.")
			arr_date = raw_input("Please enter the arrival date: ")

		flightsOnDay(depart_code,arrive_code,dep_date,arr_date)

	elif(user_choice == 5):

		tmp = sp.call('clear',shell=True)
		viewTables()




