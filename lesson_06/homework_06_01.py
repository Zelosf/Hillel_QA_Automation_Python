#Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()


example_str = input('Введіть строку:')
unique_elements = set(example_str)

if len(unique_elements) > 10:
	print(True)
else:
	print(False)

