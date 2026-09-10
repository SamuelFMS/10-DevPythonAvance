#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une école
"""
from xmlrpc.client import MAXINT

from business.course_business import CourseBusiness
from business.student_business import StudentBusiness
from business.teacher_business import TeacherBusiness


def student_interface():
    print("Selectionner le compte d'un éleve")
    list_students = StudentBusiness.get_all_students()
    for student in list_students:
        print(student)
    account_choice = input_number("Entrez le numéro de étudiant: ", 1, MAXINT)
    student = StudentBusiness.get_student_by_id(account_choice)
    if(student is not None):
        list_course = student.courses_taken()
        for course in list_course:
            display_course_with_students(course)

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

def display_course_with_students(course):
    print(course)
    for student in course.students_taking_it:
        print("- ", student)
    print("")

def input_number(message: str, min: int, max: int) -> int:
    try:
        saisie = int(input(message))
        if saisie >= min and saisie <= max:
            return saisie
        else:
            print(message)
            return input_number(message, min, max)
    except ValueError:
        print("Incorrect input. Please enter a number")
        return input_number(message, min, max)

def print_all_courses():
    list_courses = CourseBusiness.get_all_course()
    for course in list_courses:
        print(course)
        for student in course.students_taking_it:
            print("- ", student)
        print("")

def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre école
--------------------------""")

    # initialisation d'un ensemble de cours, enseignants et élèves composant l'école
    # school.init_static()

    # affichage de la liste des cours, leur enseignant et leurs élèves

    print("Authentification")
    print("1- s'authentifier en eleve")
    print("2- s'authentifier en enseignant")
    print("3- s'authentifier en directeur")

    choice = input_number("Authentification ? (Entrez le numéro) ", 1, 3)
    if choice == 1:
        student_interface()
    elif choice == 2:
        teacher_interface()
    elif choice == 3:
        print_all_courses()
if __name__ == '__main__':
    main()
