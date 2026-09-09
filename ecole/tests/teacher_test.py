from datetime import date

from business.course_business import CourseBusiness
from business.teacher_business import TeacherBusiness
from models.course import Course
from models.teacher import Teacher


def tests():
    print("Executing tests for Teacher")

    # Creation d'un teacher
    teacher = Teacher("FirstNameTest", "LastNameTest", 20, date(2021,5,1))
    new_teacher_id = TeacherBusiness.add_teacher(teacher)
    assert new_teacher_id != 0
    assert teacher.id == new_teacher_id

    #Creation d'un cours avec le nouveau teacher
    course = Course("FirstNameTest", date(2021,2,2), date(2026,5,1))
    course.teacher = teacher
    CourseBusiness.add_courses(course)

    #Recuperation du teacher dans la base de donnée
    read_teacher = TeacherBusiness.get_teacher_by_id(new_teacher_id)
    assert read_teacher is not None
    assert read_teacher.id == new_teacher_id
    assert read_teacher.first_name == 'FirstNameTest'
    assert read_teacher.last_name == 'LastNameTest'
    assert read_teacher.age == 20
    assert read_teacher.hiring_date == date(2021,5,1)

    #Edition du teacher
    read_teacher.first_name = 'NewFirstName'
    read_teacher.last_name = 'NewLastName'
    read_teacher.age = 21
    read_teacher.hiring_date = date(2024,6,7)
    assert TeacherBusiness.update_teacher(read_teacher)
    edited_student = TeacherBusiness.get_teacher_by_id(read_teacher.id)
    assert edited_student.first_name == 'NewFirstName'
    assert edited_student.last_name == 'NewLastName'
    assert edited_student.age == 21
    assert edited_student.hiring_date == date(2024,6,7)

    #Suppression du teacher que nous venons de créer
    assert CourseBusiness.delete_course(course)
    assert TeacherBusiness.delete_teacher(read_teacher)

    #Verifie que get_all n'est pas vide
    list_teacher:list|None = TeacherBusiness.get_all_teachers()
    assert list_teacher is not None
    assert len(list_teacher) > 0



if __name__ == '__main__':
    # tests unitaires
    tests()