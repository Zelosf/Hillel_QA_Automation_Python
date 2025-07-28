#Генератори:
#Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def successive_even_numbers(n):
	for number in range(0, n+1, 2):
		yield number


for n in successive_even_numbers(22):
	print(n)


#Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def fibonacci(n):
	first, second = 0, 1
	while first <=n:
		yield first
		first, second = second, first + second

for n in fibonacci(10000):
	print(n)

