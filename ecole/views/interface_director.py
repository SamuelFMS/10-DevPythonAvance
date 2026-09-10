from xmlrpc.client import MAXINT

from business.course_business import CourseBusiness
from business.student_business import StudentBusiness
from business.teacher_business import TeacherBusiness
from models.course import Course
from models.student import Student
from models.teacher import Teacher
from utils.input_utils import input_number, input_date, input_str
from views.interface_student import display_all_students


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

def create_course():
    course_name = input_str("Nom du cours: ", False)
    debut_date = input_date("Entrez la date de début: ")
    end_date = input_date("Entrez la date de fin: ")
    course = Course(course_name, debut_date, end_date)
    display_all_teacher()
    teacher_id = input_number("Entrez l'id du teacher: ", 1, MAXINT)
    teacher = TeacherBusiness.get_teacher_by_id(teacher_id)
    course.teacher = teacher
    if teacher is not None:
        new_id_course = CourseBusiness.add_courses(course)
        if new_id_course:
            print("Creation success")

def delete_course():
    display_all_courses()
    print("Entrez l'id du cours a supprimer")
    course_id = input_number("Entrez l'id du cours a supprimer: ", 0, MAXINT)
    course = CourseBusiness.get_course_by_id(course_id)
    if course is not None:
        result = CourseBusiness.delete_course(course)
        if result:
            print("Suppression success")
        else:
            print("Deletion failure")

def display_all_courses():
    list_courses = CourseBusiness.get_all_course()
    for course in list_courses:
        print(course)
        for student in course.students_taking_it:
            print("- ", student)
        print("")

def manage_course():
    print("1- Creer un nouveau cours")
    print("2- Modiifer un cours")
    print("3- Supprimer un cours")
    print("4- Affiche la liste des cours")
    print("5- Ne rien faire")
    choice = input_number("Que souhaitez vous faire ? ", 1, 5)
    if choice == 1:
        create_course()
    elif choice == 3:
        delete_course()
    elif choice == 4:
        display_all_courses()

def director_interface():
    print("1- Gérer les élèves")
    print("2- Gérer les enseignants")
    print("3- Gérer les cours")
    print("4- Ne rien faire")
    choice = input_number("Que souhaitez vous faire ? ", 1, 4)
    if choice == 1:
        manage_student()
    elif choice == 2:
        manage_teacher()
    elif choice == 3:
        manage_course()
