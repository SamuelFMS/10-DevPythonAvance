from typing import ClassVar

from daos.student_dao import StudentDao
from models.student import Student


class StudentBusiness:
    student_dao: ClassVar[StudentDao] = StudentDao()

    @staticmethod
    def get_all_students():
        return StudentBusiness.student_dao.get_all()

    @staticmethod
    def get_student_by_id(id_student: int):
        return StudentBusiness.student_dao.read(id_student)

    @staticmethod
    def add_student(student: Student):
        return  StudentBusiness.student_dao.create(student)

    @staticmethod
    def delete_student(student: Student):
        return StudentBusiness.student_dao.delete(student)

    @staticmethod
    def update_student(student: Student):
        return StudentBusiness.student_dao.update(student)

    @staticmethod
    def get_students_from_courses(id_course: int):
        return StudentBusiness.student_dao.get_students_from_course(id_course)