# -*- coding: utf-8 -*-

"""
Classe School
"""

from dataclasses import dataclass, field
from datetime import date
from typing import ClassVar

from daos.student_dao import StudentDao
from daos.teacher_dao import TeacherDao
from models.address import Address
from models.teacher import Teacher
from models.student import Student


@dataclass
class School:
    teacherDao: ClassVar[TeacherDao]  = TeacherDao()

    @staticmethod
    def get_all_teachers(self) -> list:
        teachers: list = []
        return teachers


    @staticmethod
    def get_teacher_by_id(id_teacher: int):
        teacher_dao: TeacherDao = TeacherDao()
        return teacher_dao.read(id_teacher)
