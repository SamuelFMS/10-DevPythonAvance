from xmlrpc.client import MAXINT

from business.course_business import CourseBusiness
from business.student_business import StudentBusiness
from models.student import Student
from utils.input_utils import input_str, input_number
from utils.menu import Menu
from views.director_manage.manage import Manage


class ManageStudent(Manage):
    def get_name(self):
        return "étudiant"

    def get_name_pluriels(self):
        return "étudiants"

    def create(self):
        first_name = input_str("Prenom de l'eleve: ", False)
        last_name = input_str("Nom de l'eleve: ", False)
        age = input_number("Age de l'eleve: ", 0, 120)
        student: Student = Student(first_name, last_name, age)
        StudentBusiness.add_student(student)
        print(student)

    def read_all(self):
        list_students = StudentBusiness.get_all_students()
        for student in list_students:
            print(student)

    def remove(self):
        print("Selectionner le compte d'un éleve a supprimer")
        list_students = StudentBusiness.get_all_students()
        for student in list_students:
            print(student)
        account_choice = input_number("Entrez le numéro de étudiant: ", 1, MAXINT)
        student = StudentBusiness.get_student_by_id(account_choice)
        if (student is not None):
            StudentBusiness.delete_student(student)

    def update(self):
        pass

    def assign_student_to_course(self):
        student_list = StudentBusiness.get_all_students()
        for student in student_list:
            print(student)
        input_id_student = input_number("Choix de l'étudiant nbr: ", 1, MAXINT)
        student = StudentBusiness.get_student_by_id(input_id_student)
        if (student is not None):
            course_list = CourseBusiness.get_all_course()
            for course in course_list:
                print(course)
            input_id_course = input_number("Choix du cours: ", 1, MAXINT)
            course = CourseBusiness.get_course_by_id(input_id_course)
            if course is not None:
                CourseBusiness.assign_student_to_course(student, course)
            else:
                print("Le course n'existe pas")
        else:
            print("L'etudiant nbr n'existe pas")

    def manage(self):
        menu: Menu = Menu("Gestion " + self.get_name())
        menu.add_action("Creer un " + self.get_name(), self.create)
        menu.add_action("Modifier un " + self.get_name(), self.update)
        menu.add_action("Supprimer un " + self.get_name(), self.remove)
        menu.add_action("Affiche la listes des " + self.get_name(), self.read_all)
        menu.add_action(f"Assigner un {self.get_name()} a un cours", self.assign_student_to_course)
        menu.show_menu(True)
