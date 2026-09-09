from dataclasses import dataclass
from typing import Optional

from daos.address_dao import AddressDao
from daos.dao import Dao
from models.teacher import Teacher


@dataclass
class TeacherDao(Dao[Teacher]):
    def create(self, teacher: Teacher) -> int:
        address_id = None
        with Dao.connection.cursor() as cursor:
            sql_person = (
                "INSERT INTO person (first_name, last_name, age, id_address) VALUES (%s,%s,%s,%s)"
            )
            cursor.execute(sql_person, (teacher.first_name, teacher.last_name, teacher.age, address_id))
            id_person = cursor.lastrowid
            sql_teacher = (
                "INSERT INTO teacher (hiring_date, id_person) VALUES (%s, %s)"
            )
            cursor.execute(sql_teacher, (teacher.hiring_date, id_person))
            id_teacher = cursor.lastrowid
            if id_teacher is not None:
                teacher.id = id_teacher
                Dao.connection.commit()
                return id_teacher
        return 0

    def read(self, id_teacher: int) -> Optional[Teacher]:
        """Renvoit le l'étudiant correspondant à l'entité dont l'id est id_teacher
           (ou None s'il n'a pu être trouvé)"""
        teacher: Optional[Teacher]

        with Dao.connection.cursor() as cursor:
            sql = (
                "SELECT * "
                "FROM teacher "
                "JOIN person on person.id_person = teacher.id_person "
                "WHERE id_teacher = %s"
            )
            cursor.execute(sql, (id_teacher))
            record = cursor.fetchone()
        if record is not None:
            teacher = Teacher(
                first_name=record['first_name'],
                last_name=record['last_name'],
                age=record['age'],
                hiring_date=record['hiring_date']
            )
            teacher.id = id_teacher
            if record['id_address']:
                address_dao: AddressDao = AddressDao()
                teacher.address = address_dao.read(record['id_address'])
        else:
            teacher = None

        return teacher

    def update(self, teacher: Teacher) -> bool:
        """Met à jour en BD l'entité Teacher correspondant au Teacher, pour y correspondre
        :param teacher: teacher déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = (
                """UPDATE person, teacher 
                SET person.first_name = %(first_name)s, 
                person.last_name = %(last_name)s, 
                person.age = %(age)s, 
                person.id_address = %(id_address)s, 
                teacher.hiring_date = %(hiring_date)s 
                WHERE teacher.id_teacher = %(id_teacher)s AND teacher.id_person = person.id_person"""
            )

            id_address = None
            if teacher.address is not None:
                id_address = teacher.address.id
            cursor.execute(sql, {"first_name": teacher.first_name, "last_name": teacher.last_name, "age": teacher.age,
                                 "id_address": id_address, "hiring_date": teacher.hiring_date,"id_teacher": teacher.id})
            if (cursor.rowcount == 2):
                Dao.connection.commit()
                return True
            else:
                return False

    def delete(self, teacher: Teacher) -> bool:
        with Dao.connection.cursor() as cursor:
            sql_get_id_person_before_delete = ("SELECT id_person FROM teacher WHERE id_teacher=%s")
            cursor.execute(sql_get_id_person_before_delete, (teacher.id,))
            record = cursor.fetchone()
            id_person_before_delete = record['id_person']
            sql_teacher = (
                "DELETE FROM teacher "
                "WHERE id_teacher=%s"
            )
            cursor.execute(sql_teacher, (teacher.id,))
            sql_person = (
                "DELETE FROM person "
                "WHERE id_person=%s"
            )
            cursor.execute(sql_person, (id_person_before_delete))
            if cursor.rowcount == 1:
                Dao.connection.commit()
                return True
            else:
                return False

    def get_all(self) -> Optional[list[Teacher]]:
        return []