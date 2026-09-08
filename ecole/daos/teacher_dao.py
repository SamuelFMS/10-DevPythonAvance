from dataclasses import dataclass
from typing import Optional

from daos.address_dao import AddressDao
from daos.dao import Dao
from models.teacher import Teacher


@dataclass
class TeacherDao(Dao[Teacher]):
    def create(self, teacher: Teacher) -> int:
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