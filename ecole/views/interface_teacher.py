from xmlrpc.client import MAXINT

from business.teacher_business import TeacherBusiness
from interface_student import display_course_with_students
from utils import input_number


def teacher_interface():
    print("Selectionner le compte d'un prof")
    list_teachers = TeacherBusiness.get_all_teachers()
    for teacher in list_teachers:
        print(teacher)
    account_choice = input_number("Entrez l'id du prof: ", 1, MAXINT)
    teacher = TeacherBusiness.get_teacher_by_id(account_choice)
    if(teacher is not None):
        list_course = teacher.courses_teached()
        for course in list_course:
            display_course_with_students(course)
