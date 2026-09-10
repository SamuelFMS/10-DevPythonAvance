from business.student_business import StudentBusiness
from models.student import Student
from utils.input_utils import input_str, input_number
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
