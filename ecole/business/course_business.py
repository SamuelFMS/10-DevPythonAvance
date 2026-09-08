from typing import ClassVar

from daos.course_dao import CourseDao
from models.course import Course


class CourseBusiness:
    course_dao: ClassVar[CourseDao] = CourseDao()

    @staticmethod
    def get_all_courses(self) -> list:
        courses: list = []
        return courses

    @staticmethod
    def add_courses(course: Course):
        return CourseBusiness.course_dao.create(course)

    @staticmethod
    def get_course_by_id(id_course: int):
        return CourseBusiness.course_dao.read(id_course)

    @staticmethod
    def get_students_from_course(id_course: int):
        return CourseBusiness.course_dao.get_students(id_course)

    @staticmethod
    def update_course(course: Course):
        return CourseBusiness.course_dao.update(course)

    @staticmethod
    def delete_course(course: Course):
        return CourseBusiness.course_dao.delete(course)