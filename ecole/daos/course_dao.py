# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""
from daos.student_dao import StudentDao
from daos.teacher_dao import TeacherDao
from models.course import Course
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

from models.student import Student


@dataclass
class CourseDao(Dao[Course]):
    def create(self, course: Course) -> int:
        """Crée en BD l'entité Course correspondant au cours course

        :param course: à créer sous forme d'entité Course en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        with Dao.connection.cursor() as cursor:
            sql = (
                "INSERT INTO course(name, start_date, end_date, id_teacher) VALUES(%s, %s, %s, %s)"
            )
            cursor.execute(sql, (course.name, course.start_date, course.end_date, course.teacher.id))
            id_course = cursor.lastrowid
            Dao.connection.commit()
        if id_course is not None:
            return id_course
        else:
            return 0

    def read(self, id_course: int) -> Optional[Course]:
        """Renvoit le cours correspondant à l'entité dont l'id est id_course
           (ou None s'il n'a pu être trouvé)"""
        course: Optional[Course]
        
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM course WHERE id_course=%s"
            cursor.execute(sql, (id_course,))
            record = cursor.fetchone()
        if record is not None:
            course = Course(record['name'], record['start_date'], record['end_date'])
            course.id = record['id_course']
            if record['id_teacher'] is not None:
                teacher_dao: TeacherDao = TeacherDao()
                course.teacher = teacher_dao.read(record['id_teacher'])
        else:
            course = None

        return course

    def update(self, course: Course) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param course: cours déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        return True

    def delete(self, course: Course) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True

    def get_students(self, id_course: int) -> Optional[list[Student]]:
        list_student: Optional[list[Student]]
        with Dao.connection.cursor() as cursor:
            sql = (
                "SELECT * FROM takes "
                "WHERE id_course=%s"
            )
            cursor.execute(sql, (id_course,))
            record = cursor.fetchall()
        if record is not None:
            student_dao = StudentDao()
            list_student = []
            for student in record:
                list_student.append(student_dao.read(student["student_nbr"]));

        return list_student
