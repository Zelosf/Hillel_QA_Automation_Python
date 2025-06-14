# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while number * multiplier <= 25:
        result = number * multiplier
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two_numbers(a: int, b: int)-> int:
    return a + b


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average_list(lst1):
    return sum(lst1) / len(lst1)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_str(str1: str)-> str:
    return str1[::-1]


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word_in_list(lst):
    longest_word = ''
    for element in lst:
        if len(element) > len(longest_word):
            longest_word = element
    return longest_word

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    return str1.find(str2)


# task 7
""" Рахує кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. (Lesson 6 task 1)"""

def more_ten_uniq_symbol(example_str: str) -> bool:
    unique_elements = set(example_str)
    return len(unique_elements) > 10

# task 8

""" Cтвормує новий list, який містить лише змінні типу стрінг (Lesson 6 task 3) """

def get_string(examaple_lst: list) -> list:
    str_lst = []
    for element in examaple_lst:
        if type(element) is str:
            str_lst.append(element)
    return str_lst


# task 9
""" Рахує суму усіх парних чисел в листі (Lesson 6 task 4) """

def sum_even_number(lst):
    sum_even = 0

    for element in lst:
        if type(element) is not int and type(element) is not float:
            continue
        else:
            if element % 2 == 0:
                sum_even += element

    return(sum_even)


# task 10
"""Виводить скількі разів у тексті зустрічається потрібна літера (Lesson 4 task 4)"""

def number_of_required_letters (example_str, find_symbol):
    qty_symbol = 0
    for char in example_str.lower():
        if char == find_symbol.lower():
            qty_symbol += 1
    return qty_symbol


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""