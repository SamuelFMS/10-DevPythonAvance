from utils.input_utils import input_number
from utils.menu import Menu
from views.director_manage.manage_course import ManageCourse
from views.director_manage.manage_student import ManageStudent
from views.director_manage.manage_teacher import ManageTeacher


def manage_student():
    managestudent = ManageStudent()
    managestudent.manage()


def manage_teacher():
    manage = ManageTeacher()
    manage.manage()


def manage_course():
    manage = ManageCourse()
    manage.manage()


def director_interface():
    menu = Menu("Menu Directeur")
    menu.add_action("Gérer les élèves", manage_student)
    menu.add_action("Gérer les enseignants", manage_teacher)
    menu.add_action("Gérer les cours", manage_course)
    menu.show_menu(True)
