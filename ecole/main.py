#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une école
"""
from xmlrpc.client import MAXINT

from business.course_business import CourseBusiness
from business.student_business import StudentBusiness
from business.teacher_business import TeacherBusiness
from models.course import Course
from models.student import Student
from models.teacher import Teacher
from utils import input_number, input_str, input_date


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

def create_student():
    first_name = input_str("Prenom de l'eleve: ", False)
    last_name = input_str("Nom de l'eleve: ", False)
    age = input_number("Age de l'eleve: ", 0,120)
    student: Student = Student(first_name, last_name, age)
    StudentBusiness.add_student(student)
    print(student)

def delete_student():
    print("Selectionner le compte d'un éleve a supprimer")
    list_students = StudentBusiness.get_all_students()
    for student in list_students:
        print(student)
    account_choice = input_number("Entrez le numéro de étudiant: ", 1, MAXINT)
    student = StudentBusiness.get_student_by_id(account_choice)
    if (student is not None):
        StudentBusiness.delete_student(student)

def display_all_students():
    list_students = StudentBusiness.get_all_students()
    for student in list_students:
        print(student)

def manage_student():
    print("1- Creer un eleve")
    print("2- Modifier un eleve")
    print("3- Supprimer un eleve")
    print("4- Afficher la liste d'eleves")
    print("5- Ne rien faire")
    choice = input_number("Que souhaitez vous faire ? ", 1, 5)
    if choice == 1:
        create_student()
    elif choice == 3:
        delete_student()
    elif choice == 4:
        display_all_students()

def create_teacher():
    first_name = input_str("Prenom de l'enseignant: ", False)
    last_name = input_str("Nom de l'enseignant: ", False)
    age = input_number("Age de l'enseignant: ", 0,120)
    date = input_date("Date d'arrivé: ")
    teacher: Teacher = Teacher(first_name, last_name, age, date)
    TeacherBusiness.add_teacher(teacher)

def delete_teacher():
    display_all_teacher()
    choice_teacher = input_number("Entrez l'id enseignant a supprimer: ", 1, MAXINT)
    teacher = TeacherBusiness.get_teacher_by_id(choice_teacher)
    if teacher is not None:
        if TeacherBusiness.delete_teacher(teacher):
            print("Suppression avec success")

def display_all_teacher():
    list_teacher = TeacherBusiness.get_all_teachers()
    for teacher in list_teacher:
        print(teacher)

def manage_teacher():
    print("1 - Creer un enseignant")
    print("2 - Modifier un enseignant")
    print("3 - Supprimer un enseignant")
    print("4 - Affiche la liste d'enseignants")
    print("5 - Ne rien faire")
    choice = input_number("Que souhaitez vous faire ? ", 1, 5)
    if choice == 1:
        create_teacher()
    elif choice == 3:
        delete_teacher()
    elif choice == 4:
        display_all_teacher()

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
