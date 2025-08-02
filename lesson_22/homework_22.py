from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, inspect, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


engine = create_engine("sqlite:///students.db", echo=True)
Base = declarative_base()

student_course = Table(
    'student_course',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    courses = relationship("Course", secondary=student_course, back_populates="students")

    def __repr__(self):
        return f"id={self.id}, name='{self.name}', age={self.age}"

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship("Student", secondary=student_course, back_populates="courses")

    def __repr__(self):
        return f"id={self.id}, title='{self.title}'"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()



