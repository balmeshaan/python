first_number = (input("Enter the first number:  "))
second_number = (input("Enter the second number:  "))

if str(first_number).isdigit() and str(second_number).isdigit():
	operation = input("Choose the operation (+, -, /, *):  ")
			
	
	if operation == "+":
		print("The answer is", int(first_number) + int(second_number))
	elif operation == "-":
		print("The answer is", int(first_number) + int(second_number))
	elif operation == "*":
		print("The answer is", int(first_number) + int(second_number))
	elif operation == "/":
		print("The answer is", int(first_number) + int(second_number))
	else:
		print("You have entered something other than the available operations, please try again.")		
else:
	print("You have entered something other than numbers. Please enter real numbers this time.")