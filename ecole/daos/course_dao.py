# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""
from dataclasses import dataclass
from typing import Optional
from daos.dao import Dao
from models.course import Course


@dataclass
class CourseDao(Dao[Course]):
    def create(self, course: Course) -> int:
        """Crée en BD l'entité Course correspondant au cours course

        :param course: à créer sous forme d'entité Course en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        with Dao.connection.cursor() as cursor:
            sql = ("INSERT INTO course(name, start_date, end_date, id_teacher) VALUES(%s, %s, %s, %s)")
            cursor.execute(sql, (course.name, course.start_date, course.end_date, course.teacher.id))
            id_course = cursor.lastrowid
            Dao.connection.commit()
        if id_course is not None:
            course.id = id_course
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
            course = self.parse(record)

        return course

    def update(self, course: Course) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param course: cours déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        with Dao.connection.cursor() as cursor:
            sql = ("UPDATE course "
                   "SET name=%(name)s, "
                   "start_date=%(start_date)s, "
                   "end_date=%(end_date)s, "
                   "id_teacher=%(id_teacher)s "
                   "WHERE id_course=%(id_course)s")

            cursor.execute(sql, {"name": course.name, "start_date": course.start_date, "end_date": course.end_date,
                                 "id_teacher": course.teacher.id, "id_course": course.id})
            if (cursor.rowcount == 1):
                Dao.connection.commit()
                return True
            else:
                return False

    def delete(self, course: Course) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = ("DELETE FROM course "
                   "WHERE id_course=%s")
            cursor.execute(sql, (course.id))
            if cursor.rowcount == 1:
                Dao.connection.commit()
                return True
            else:
                return False

    def get_all(self) -> Optional[list[Course]]:
        list_course: Optional[list[Course]] = None
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM course"
            cursor.execute(sql)
            record = cursor.fetchall()
            if record is not None:
                list_course = []
                for course in record:
                    course_object: Optional[Course] = self.parse(course)
                    if(course_object is not None):
                        list_course.append(course_object)

        return list_course

    def parse(self, record) -> Optional[Course]:
        #Import local pour eviter circularité
        from daos.teacher_dao import TeacherDao
        from business.student_business import StudentBusiness

        course: Optional[Course]
        if record is not None:
            course = Course(record['name'], record['start_date'], record['end_date'])
            course.id = record['id_course']
            if record['id_teacher'] is not None:
                teacher_dao: TeacherDao = TeacherDao()
                course.teacher = teacher_dao.read(record['id_teacher'])
            course.students_taking_it = StudentBusiness.get_students_from_courses(record['id_course'])
        else:
            course = None
        return course

    def assign_student_to_course(self, id_student: int, course: Course) -> bool:
        with Dao.connection.cursor() as cursor:
            sql = """INSERT INTO takes(student_nbr, id_course) VALUES (%s, %s)"""
            cursor.execute(sql, (id_student, course.id))
            if cursor.rowcount == 1:
                Dao.connection.commit()
                return True
            else:
                return False

    def get_courses_by_student(self, id_student) -> Optional[list[Course]]:
        list_course: Optional[list[Course]] = None
        with Dao.connection.cursor() as cursor:
            sql = """SELECT course.*
                    FROM course
                    JOIN takes on takes.id_course = course.id_course
                    WHERE takes.student_nbr=%s"""
            cursor.execute(sql, (id_student,))
            record = cursor.fetchall()
            if record is not None:
                list_course = []
                for course in record:
                    course_object: Optional[Course] = self.parse(course)
                    if course_object is not None:
                        list_course.append(course_object)
        return list_course

    def get_courses_by_teacher(self, id_teacher) -> Optional[list[Course]]:
        list_course: Optional[list[Course]] = None
        with Dao.connection.cursor() as cursor:
            sql = """SELECT *
            FROM course
            WHERE course.id_teacher=%s"""
            cursor.execute(sql, (id_teacher,))
            record = cursor.fetchall()
            if record is not None:
                list_course = []
                for course in record:
                    course_object: Optional[Course] = self.parse(course)
                    if course_object is not None:
                        list_course.append(course_object)
        return list_course