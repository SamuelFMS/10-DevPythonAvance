from datetime import date

from business import school
from business.school import School
from daos.teacher_dao import TeacherDao
from models.teacher import Teacher


def tests():
    print("Executing tests for Teacher")
    school: School = School()
    teacher_dao = TeacherDao()

    # Creation d'un cours
    teacher = Teacher("FirstNameTest", "LastNameTest", 20, date(2021,5,1))
    new_teacher_id = teacher_dao.create(teacher)
    assert new_teacher_id != 0
    assert teacher.id == new_teacher_id

    #Recuperation du cours dans la base de donnée
    read_teacher = teacher_dao.read(new_teacher_id)
    assert read_teacher is not None
    assert read_teacher.id == new_teacher_id
    assert read_teacher.first_name == 'FirstNameTest'
    assert read_teacher.last_name == 'LastNameTest'
    assert read_teacher.age == 20
    assert read_teacher.hiring_date == date(2021,5,1)

    #Suppression du cours que nous venons de créer
    assert teacher_dao.delete(read_teacher)




if __name__ == '__main__':
    # tests unitaires
    tests()