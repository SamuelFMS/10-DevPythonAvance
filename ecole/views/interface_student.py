from xmlrpc.client import MAXINT

from business.student_business import StudentBusiness
from utils.input_utils import input_number


def student_interface():
    print("Selectionner le compte d'un éleve")
    list_students = StudentBusiness.get_all_students()
    for student in list_students:
        print(student)
    account_choice = input_number("Entrez le numéro de étudiant: ", 1, MAXINT)
    student = StudentBusiness.get_student_by_id(account_choice)
    if (student is not None):
        list_course = student.courses_taken()
        for course in list_course:
            display_course_with_students(course)


def display_course_with_students(course):
    print(course)
    for student in course.students_taking_it:
        print("- ", student)
    print("")
