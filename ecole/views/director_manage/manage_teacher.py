from business.teacher_business import TeacherBusiness
from models.teacher import Teacher
from utils.input_utils import input_str, input_number, input_date
from views.director_manage.manage import Manage
from views.interface_teacher import display_all_teacher


class ManageTeacher(Manage):
    def get_name(self):
        return "enseignant"

    def get_name_pluriels(self):
        return "enseignants"

    def create(self):
        first_name = input_str("Prenom de l'enseignant: ", False)
        last_name = input_str("Nom de l'enseignant: ", False)
        age = input_number("Age de l'enseignant: ", 0, 120)
        date = input_date("Date d'arrivé: ")
        teacher: Teacher = Teacher(first_name, last_name, age, date)
        TeacherBusiness.add_teacher(teacher)

    def read_all(self):
        display_all_teacher()

    def remove(self):
        display_all_teacher()
        choice_teacher = input_number("Entrez l'id enseignant a supprimer: ", 1, MAXINT)
        teacher = TeacherBusiness.get_teacher_by_id(choice_teacher)
        if teacher is not None:
            result = TeacherBusiness.delete_teacher(teacher)
            if result:
                print("Suppression avec success")

    def update(self):
        pass
