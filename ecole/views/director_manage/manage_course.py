from xmlrpc.client import MAXINT

from business.course_business import CourseBusiness
from business.teacher_business import TeacherBusiness
from models.course import Course
from utils.input_utils import input_str, input_date, input_number
from views.director_manage.manage import Manage
from views.interface_teacher import display_all_teacher


class ManageCourse(Manage):
    def get_name(self):
        return "cours"

    def get_name_pluriels(self):
        return "cours"

    def create(self):
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

    def read_all(self):
        list_courses = CourseBusiness.get_all_course()
        for course in list_courses:
            print(course)
            for student in course.students_taking_it:
                print("- ", student)
            print("")

    def remove(self):
        self.read_all()
        course_id = input_number("Entrez l'id du cours a supprimer: ", 0, MAXINT)
        course = CourseBusiness.get_course_by_id(course_id)
        if course is not None:
            result = CourseBusiness.delete_course(course)
            if result:
                print("Suppression success")
            else:
                print("Deletion failure")

    def update(self):
        pass
