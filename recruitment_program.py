skills = ['coding', 'editing', 'data entry', 'analysis', 'accounting']

name = input('what is your name?  ')
age =  input('how old are you?  ')
experience = input("how many years of experience do you have?  ")

cv = {'name':name,'age': age, 'experience':experience, 'skills':[]}
bullet = 0
for skill in skills:
	bullet += 1
	print(str(bullet) + ". " + str(skill))
	
skill_1 = input('please choose a skill by typing the corresponding number:  ')
skill_2 = input('please choose another skill by typing the corresponding number:  ')

def first_skill():
	if skill_1 == '1':
		cv['skills'].append(skills[0])
		return second_skill()
	elif skill_1 == '2':
		cv['skills'].append(skills[1])
		return second_skill()
	elif skill_1 == '3':
		cv['skills'].append(skills[2])
		return second_skill()
	elif skill_1 == '4':
		cv['skills'].append(skills[3])
		return second_skill()	
	elif skill_1 == '5':
		cv['skills'].append(skills[4])
		return second_skill()
	else:
		print('please choose a valid number')


def second_skill():
	if skill_2 == '1':
		cv['skills'].append(skills[0])
		return acceptance()
	elif skill_2 == '2':
		cv['skills'].append(skills[1])
		return acceptance()
	elif skill_2 == '3':
		cv['skills'].append(skills[2])
		return acceptance()
	elif skill_2 == '4':
		cv['skills'].append(skills[3])	
		return acceptance()
	elif skill_2 == '5':
		cv['skills'].append(skills[4])
		return acceptance()
	else:
		print('please choose a valid number')

def acceptance():
	if int(age) > 18 and int(experience) > 2 and 'coding' in cv['skills']:
		print('Congratulations, you have been accepted!')
	else:
		print('Sorry, no acceptance this time...')

first_skill()
