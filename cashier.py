total = [{'products':''}]

serial = 0


total[serial]['products'] = input('Item (enter "done" when finished):  ')

while total[serial]['products'] != 'done':
	total[serial]['price'] = float(input('Price:  '))
	total[serial]['qty'] = input('Quantity:  ')
	serial += 1
	total.append({})
	total[serial]['products'] = input('Item (enter "done" when finished):  ') 

del total[-1]

if serial == 0:
	print('add some products first!')
else:
	print('-----------------------')
	print('Here\'s your receipt...')
	print('-----------------------')

for item in total:
	if serial == 0:
		print('add some products first!')
	else:
		print(item['qty'], item['products'], str(float(item['qty']) * item['price']) + 'KD')
		
print('-----------------------')

total_list = ['']

for summable in total:
	total_list.append(float(summable['qty']) * summable['price'])

del total_list[0]

print('Total Price: ', str(sum(total_list)) + 'KD')




