# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". 
# Створіть об'єкт цього класу, представляючий студента. 
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента. 
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
	def __init__(self, name, surname, age, average_score=0):
		self.name = name
		self.surname = surname
		self.age = age
		self.average_score = average_score

	def greeting(self):
		return f'Hello my name is {self.name} {self.surname}. I am {self.age} years old.'

	def edit_score(self, average_score):
		self.average_score = average_score


student_1 = Student('Oleksandr', 'Hlushko', 34)
student_2 = Student('Stud1', 'Stud2', 114, 100)
print(student_1.greeting())
print(student_2.greeting())
student_1.edit_score(96)
print(student_1.average_score)
print(student_2.average_score)