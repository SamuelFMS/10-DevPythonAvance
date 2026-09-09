from dataclasses import dataclass
from typing import Optional

from daos.address_dao import AddressDao
from daos.dao import Dao
from models.student import Student


@dataclass
class StudentDao(Dao[Student]):
    def create(self, student: Student) -> int:
        """Crée en BD l'entité Student correspondant a l'élève

        :param Student: à créer sous forme d'entité Student en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        address_id = None
        with Dao.connection.cursor() as cursor:
            sql_person = ("INSERT INTO person (first_name, last_name, age, id_address) VALUES (%s,%s,%s,%s)")
            cursor.execute(sql_person, (student.first_name, student.last_name, student.age, address_id))
            id_person = cursor.lastrowid
            sql_student = ("INSERT INTO student (id_person) VALUES (%s)")
            cursor.execute(sql_student, (id_person,))
            id_student = cursor.lastrowid
            if id_student is not None:
                student.student_nbr = id_student
                Dao.connection.commit()
                return id_student
        return 0

    def read(self, id_student: int) -> Optional[Student]:
        """Renvoit le l'étudiant correspondant à l'entité dont l'id est id_Student
           (ou None s'il n'a pu être trouvé)"""
        student: Optional[Student]

        with Dao.connection.cursor() as cursor:
            sql = ("SELECT * "
                   "FROM student "
                   "JOIN person on person.id_person = student.id_person "
                   "WHERE student_nbr = %s")
            cursor.execute(sql, (id_student))
            record = cursor.fetchone()
        student = self.parse(record)
        return student

    def update(self, student: Student) -> bool:
        """Met à jour en BD l'entité Student correspondant à l'etudiant, pour y correspondre

        :param student: student déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = ("UPDATE person "
                   "JOIN student ON student.id_person = person.id_person "
                   "SET person.first_name = %(first_name)s, "
                   "person.last_name = %(last_name)s, "
                   "person.age = %(age)s, "
                   "person.id_address = %(id_address)s "
                   "WHERE student.student_nbr = %(student_nbr)s")

            id_address = None
            if student.address is not None:
                id_address = student.address.id
            cursor.execute(sql, {"first_name": student.first_name, "last_name": student.last_name, "age": student.age,
                                 "id_address": id_address, "student_nbr": student.student_nbr})
            if (cursor.rowcount == 1):
                Dao.connection.commit()
                return True
            else:
                return False

    def delete(self, student: Student) -> bool:
        """Supprime en BD l'entité Student correspondant à student

        :param student: Etudiant dont l'entité Student correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql_get_id_person_before_delete = ("SELECT id_person FROM student WHERE student_nbr=%s")
            cursor.execute(sql_get_id_person_before_delete, (student.student_nbr,))
            record = cursor.fetchone()
            id_person_before_delete = record['id_person']
            sql_student = ("DELETE FROM student "
                           "WHERE student_nbr=%s")
            cursor.execute(sql_student, (student.student_nbr,))
            sql_person = ("DELETE FROM person "
                          "WHERE id_person=%s")
            cursor.execute(sql_person, (id_person_before_delete))
            if cursor.rowcount == 1:
                Dao.connection.commit()
                return True
            else:
                return False

    def get_all(self) -> Optional[list[Student]]:
        list_student: Optional[list[Student]] = None
        with Dao.connection.cursor() as cursor:
            sql = """SELECT * FROM student 
                JOIN person on person.id_person = student.id_person """
            cursor.execute(sql)
            record = cursor.fetchall()
            if record is not None:
                list_student = []
                for student in record:
                    student_object: Optional[Student] = self.parse(student)
                    if (student_object is not None):
                        list_student.append(student_object)
        return list_student

    def parse(self, record) -> Optional[Student]:
        student: Optional[Student]
        if record is not None:
            student = Student(first_name=record['first_name'], last_name=record['last_name'], age=record['age'], )
            student.student_nbr = record['student_nbr']
            if record['id_address']:
                address_dao: AddressDao = AddressDao()
                student.address = address_dao.read(record['id_address'])
        else:
            student = None
        return student
