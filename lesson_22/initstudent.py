import random
from homework_22 import Student, Course, Base, create_engine, sessionmaker

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


course_titles = ['Python Basic', 'Python Pro', 'Python Automotive', 'JAVA Basic', 'JAVA Pro']
courses = [Course(title=title) for title in course_titles]
session.add_all(courses)
session.commit()

student_names = ['Іван Іванов', 'Марія Петрова', 'Олексій Смирнов', 'Ольга Кузнецова', 'Дмитро Попов',
'Катерина Васильєва', 'Сергій Козлов', 'Наталя Новікова', 'Андрій Морозов', 'Тетяна Федорова',
'Михайло Соколов', 'Анна Іванова', 'Павло Лебедєв', 'Юлія Семенова', 'Микита Філіппов',
'Світлана Зайцева', 'Роман Волков', 'Вікторія Соловйова', 'Артем Кудрявцев', 'Олена Михайлова']

for name in student_names:

	student = Student(name=name)
	student.age = random.randint(18, 30)
	student.courses = random.sample(courses, k=random.randint(1, 3))
	session.add(student)

session.commit()
session.close()