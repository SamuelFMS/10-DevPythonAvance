from utils.input_utils import input_number
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
