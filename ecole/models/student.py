# -*- coding: utf-8 -*-

"""
Classe Student, fille de la classe Person
"""

from dataclasses import dataclass, field
from typing import ClassVar

from business import course_business
from business.course_business import CourseBusiness
from .person import Person
from .course import Course


@dataclass
class Student(Person):
    """Elève suivant un ou plusieurs cours de l'école :
    - students_nb   : nombre total d'élèves
    - student_nbr   : n° d'élève
    - courses_taken : liste des cours pris par cet élève
    """
    students_nb: ClassVar[int] = 0  # nb d'étudiants créés
    student_nbr: int|None = field(init=False)

    def courses_taken(self):
        if(self.student_nbr != None):
            return CourseBusiness.get_course_from_student(self.student_nbr)

    def __str__(self) -> str:
        person_str = super().__str__()
        return f"{person_str}, n° étudiant : {self.student_nbr}"
