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
        ...
        return 0

    def read(self, id_student: int) -> Optional[Student]:
        """Renvoit le l'étudiant correspondant à l'entité dont l'id est id_Student
           (ou None s'il n'a pu être trouvé)"""
        student: Optional[Student]

        with Dao.connection.cursor() as cursor:
            sql = (
                "SELECT * "
                "FROM student "
                "JOIN person on person.id_person = student.id_person "
                "WHERE student_nbr = %s"
            )
            cursor.execute(sql, (id_student))
            record = cursor.fetchone()
        if record is not None:
            student = Student(
                first_name=record['first_name'],
                last_name=record['last_name'],
                age=record['age'],
                student_nbr=record['student_nbr'],
            )
            if record['id_address']:
                address_dao: AddressDao = AddressDao()
                student.address = address_dao.read(record['id_address'])
        else:
            student = None

        return student


    def update(self, student: Student) -> bool:
        """Met à jour en BD l'entité Student correspondant à student, pour y correspondre

        :param student: Student déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        return True

    def delete(self, student: Student) -> bool:
        """Supprime en BD l'entité Student correspondant à student

        :param student: Etudiant dont l'entité Student correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True
