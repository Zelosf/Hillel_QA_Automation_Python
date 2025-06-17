#Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
#[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
#Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
#Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
#Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
#Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”



def all_sum_numbers_v1 (example):
	for element in example:
		sum_numbers = 0
		try:
			for number in element.split(","):
				sum_numbers += int(number)
			print(sum_numbers)
		except ValueError:
			print("Не можу це зробити")




def all_sum_numbers_v2 (example):
	try:
		numbers = example.split(",")
		total = sum(int(num) for num in numbers)
		return total
	except ValueError:
		return "Не можу це зробити"


a = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

all_sum_numbers_v1(a)

for item in a:
	result = all_sum_numbers_v2 (item)
	print(result)