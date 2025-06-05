#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

list_num = (1, 'q', 3, 5, 6.0, 7, 8)
sum_even_number = 0

for element in list_num:
	if type(element) is not int and type(element) is not float:
		continue
	else:
		if element % 2 == 0:
			sum_even_number += element
print(f'Сумма усіх парних чисел = {sum_even_number}')