from datetime import datetime, date

birth_year = int(input("Enter year of birth:  "))
birth_month = int(input("Enter month of birth:  "))
birth_day = int(input("Enter day of birth:  "))

t1 = date(year = 2019, month = 9, day = 4)
t2 = date(year = birth_year, month= birth_month, day = birth_day)
t3 = t1 - t2

years = t3.days / 365

def check_birthdate(t3):
	if t3.days > 0:
		return calculator_age(t3)
	else:
		print("Please enter a valid date of birth")

def calculator_age(t3):
	print("You are %i years old!" % (years))

check_birthdate(t3)	


