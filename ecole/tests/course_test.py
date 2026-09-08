from datetime import date

from business import school
from business.school import School
from daos.course_dao import CourseDao
from models.course import Course
from models.teacher import Teacher


def tests():
    print("Executing tests for Course")
    school: School = School()
    course_dao = CourseDao()

    # Creation d'un cours
    course = Course('test',date(2021,1,2),date(2026,5,1))
    course.teacher = school.get_course_by_id(1).teacher
    assert course.teacher.id != 0
    new_course_id = course_dao.create(course)
    assert new_course_id != 0
    assert course.id == new_course_id

    #Recuperation du cours dans la base de donnée
    read_course:Course = course_dao.read(new_course_id)
    assert read_course.id == new_course_id
    assert read_course.name == 'test'
    assert read_course.start_date == date(2021,1,2)
    assert read_course.end_date == date(2026,5,1)

    #Suppression du cours que nous venons de créer
    assert course_dao.delete(read_course)




if __name__ == '__main__':
    # tests unitaires
    tests()