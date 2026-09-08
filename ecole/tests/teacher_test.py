from datetime import date
from business.teacher_business import TeacherBusiness
from models.teacher import Teacher


def tests():
    print("Executing tests for Teacher")

    # Creation d'un cours
    teacher = Teacher("FirstNameTest", "LastNameTest", 20, date(2021,5,1))
    new_teacher_id = TeacherBusiness.add_teacher(teacher)
    assert new_teacher_id != 0
    assert teacher.id == new_teacher_id

    #Recuperation du cours dans la base de donnée
    read_teacher = TeacherBusiness.get_teacher_by_id(new_teacher_id)
    assert read_teacher is not None
    assert read_teacher.id == new_teacher_id
    assert read_teacher.first_name == 'FirstNameTest'
    assert read_teacher.last_name == 'LastNameTest'
    assert read_teacher.age == 20
    assert read_teacher.hiring_date == date(2021,5,1)

    #Suppression du cours que nous venons de créer
    assert TeacherBusiness.delete_teacher(read_teacher)




if __name__ == '__main__':
    # tests unitaires
    tests()