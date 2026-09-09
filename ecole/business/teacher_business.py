from typing import ClassVar

from daos.teacher_dao import TeacherDao
from models.teacher import Teacher


class TeacherBusiness:
    teacher_dao: ClassVar[TeacherDao]  = TeacherDao()

    @staticmethod
    def get_all_teachers():
        return TeacherBusiness.teacher_dao.get_all()

    @staticmethod
    def get_teacher_by_id(id_teacher: int):
        return TeacherBusiness.teacher_dao.read(id_teacher)

    @staticmethod
    def add_teacher(teacher: Teacher):
        return TeacherBusiness.teacher_dao.create(teacher)

    @staticmethod
    def delete_teacher(teacher: Teacher):
        return TeacherBusiness.teacher_dao.delete(teacher)

    @staticmethod
    def update_teacher(teacher: Teacher):
        return TeacherBusiness.teacher_dao.update(teacher)