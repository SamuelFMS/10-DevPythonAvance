from datetime import date

from business import school
from business.school import School
from daos.student_dao import StudentDao
from models.student import Student


def tests():
    print("Executing tests for student")
    school: School = School()
    student_dao = StudentDao()

    # Creation d'un cours
    student = Student("FirstNameTest", "LastNameTest", 20)
    new_student_id = student_dao.create(student)
    assert new_student_id != 0
    assert student.student_nbr == new_student_id

    #Recuperation du cours dans la base de donnée
    read_student = student_dao.read(new_student_id)
    assert read_student is not None
    assert read_student.student_nbr == new_student_id
    assert read_student.first_name == 'FirstNameTest'
    assert read_student.last_name == 'LastNameTest'
    assert read_student.age == 20

    #Suppression du cours que nous venons de créer
    assert student_dao.delete(read_student)




if __name__ == '__main__':
    # tests unitaires
    tests()