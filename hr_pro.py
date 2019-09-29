from datetime import date
this_year = 2019

class Employee:
	def __init__(self, name, age, salary, employment_date):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_date = employment_date

	def get_working_years(self):
		return date.today().year - int(self.employment_date)

	def __str__(self):
		return 'Name: %s, Age: %s, Salary: %s, Working Years: %d' %(self.name, self.age, self.salary, self.get_working_years())



class Manager(Employee):
	def __init__(self, name, age, salary, employment_date, bonus_percentage):
		super().__init__(name, age, salary, employment_date)
		self.bonus_percentage = bonus_percentage

	def get_bonus(self):
		return float(self.bonus_percentage) * float(self.salary)

	def __str__(self):
		return 'Name: %s, Age: %s, Salary: %s, Working Years: %d, Bonus %.3f' %(self.name, self.age, self.salary, self.get_working_years(), self.get_bonus())

employees = []
managers = []

print('Welcome to HR Pro 2019')


print('Optons:')
print()
print('		1. Show Employees')
print('		2. Show Managers')
print('		3. Add Employees')
print('		4. Add Managers')
print('		5. Exit')
print()
option = input('What would you like to do? ')

while option != '5':
	if option == '1':
		print('------------------------')
		for employee in employees:
			print(employee)
		print('------------------------')
	elif option == '2':
		print('------------------------')
		for manager in managers:
			print(manager)
		print('------------------------')
	elif option == '3':
		print('------------------------')
		
		name = input('Name:  ')
		age = input('Age:  ')
		salary = input('Salary:  ')
		employment_date = input('Employment Year:  ')
		employee = Employee(name, age, salary, employment_date)
		employees.append(employee)
		print('Employee added successfully!')
		print('------------------------')
	elif option == '4':
		print('------------------------')
		name = input('Name:  ')
		age = input('Age:  ')
		salary = input('Salary:  ')
		employment_date = input('Employment Year:  ')
		bonus_percentage = input('Bonus Percentage:  ')
		manager = Manager(name, age, salary, employment_date, bonus_percentage)
		managers.append(manager)
		print('Manager added successfully!')
		print('------------------------')
	else:
		print('------------------------')
		print('Invalid input, please choose one of the menu items above.')
		print('------------------------')


	print('Optons:')
	print()
	print('		1. Show Employees')
	print('		2. Show Managers')
	print('		3. Add Employees')
	print('		4. Add Managers')
	print('		5. Exit')
	print()
	option = input('What would you like to do? ')