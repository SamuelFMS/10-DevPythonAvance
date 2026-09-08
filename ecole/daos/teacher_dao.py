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
            if record['id_address']:
                address_dao: AddressDao = AddressDao()
                teacher.address = address_dao.read(record['id_address'])
        else:
            teacher = None

        return teacher

    def update(self, teacher: Teacher) -> bool:
        return True

    def delete(self, teacher: Teacher) -> bool:
        return True