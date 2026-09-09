from datetime import date
from typing import Optional

from business.course_business import CourseBusiness
from models.course import Course
from models.teacher import Teacher


def tests():
    print("Executing tests for Course")

    # Creation d'un cours
    course = Course('test',date(2021,1,2),date(2026,5,1))
    course.teacher = CourseBusiness.get_course_by_id(1).teacher
    assert course.teacher.id != 0
    new_course_id = CourseBusiness.add_courses(course)
    assert new_course_id != 0
    assert course.id == new_course_id

    #Recuperation du cours dans la base de donnée
    read_course:Course|None = CourseBusiness.get_course_by_id(new_course_id)
    assert read_course is not None
    assert read_course.id == new_course_id
    assert read_course.name == 'test'
    assert read_course.start_date == date(2021,1,2)
    assert read_course.end_date == date(2026,5,1)

    #Edition du cours
    read_course.teacher = CourseBusiness.get_course_by_id(2).teacher
    assert read_course.teacher.id != course.teacher.id
    read_course.start_date = date(2021,3,5)
    read_course.end_date = date(2025,5,30)
    read_course.name = "Lecture"
    assert CourseBusiness.update_course(read_course)
    assert read_course.id is not None
    edited_course = CourseBusiness.get_course_by_id(read_course.id)
    assert edited_course.teacher == CourseBusiness.get_course_by_id(2).teacher
    assert edited_course.start_date == date(2021,3,5)
    assert edited_course.end_date == date(2025,5,30)
    assert edited_course.name == "Lecture"

    #Suppression du cours que nous venons de créer
    assert CourseBusiness.delete_course(read_course)

    #Verifie que get_all n'est pas vide
    list_course:list|None = CourseBusiness.get_all_course()
    assert list_course is not None
    assert len(list_course) > 0


if __name__ == '__main__':
    # tests unitaires
    tests()