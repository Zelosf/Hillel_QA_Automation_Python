from homework_22 import Student, Course, Session


def add_student(name, age, course_ids=None):
    if course_ids is None:
        course_ids = []
    session = Session()
    new_student = Student(name=name, age=age)
    courses = session.query(Course).filter(Course.id.in_(course_ids)).all()
    new_student.courses = courses

    session.add(new_student)
    session.commit()
    session.close()


def get_students_by_course(course_name):
    with Session() as session:
        course = session.query(Course).filter_by(title=course_name).first()
        return course.students if course else []


def get_courses_by_student(student_name):
    with Session() as session:
        student = session.query(Student).filter_by(name=student_name).first()
        return student.courses if student else []


def update_student_name(student_id, new_name):
    with Session() as session:
        student = session.get(Student, student_id)
        if student:
            student.name = new_name
            session.commit()


def update_student_age(student_id, new_age):
    with Session() as session:
        student = session.get(Student, student_id)
        if student:
            student.age = new_age
            session.commit()


def delete_student(student_id):
    with Session() as session:
        student = session.query(Student).get(student_id)
        if student:
            session.delete(student)
            session.commit()


#add_student('Alex Hlushko', '34',[1, 2, 3])
#for result in get_students_by_course('Python Pro'):
#    print(result)

#for result in get_courses_by_student('Oleksand Hlushko'):
#    print(result)
#update_student_name(21, 'Oleksand Hlushko')
#update_student_age(21, 134)
#delete_student(22)