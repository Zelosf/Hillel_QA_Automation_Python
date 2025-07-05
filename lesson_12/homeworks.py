def all_sum_numbers(example):
	try:
		numbers = example.split(",")
		total = sum(int(num) for num in numbers)
		return total
	except ValueError:
		return "Не можу це зробити"


"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two_numbers(a: int, b: int)-> int:
    return a + b



"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word_in_list(lst):
    longest_word = ''
    for element in lst:
        if len(element) > len(longest_word):
            longest_word = element
    return longest_word


"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average_list(lst1):
    return round(sum(lst1) / len(lst1), 3)