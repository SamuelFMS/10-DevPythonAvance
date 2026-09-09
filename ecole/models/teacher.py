# -*- coding: utf-8 -*-

"""
Classe Teacher
"""

from dataclasses import dataclass, field
from typing import Optional
from datetime import date

from business.course_business import CourseBusiness
from .person import Person
from .course import Course


@dataclass
class Teacher(Person):
    """Enseignant d'un ou plusieurs cours de l'école :
    - id              : clé primaire de l'entité persistante
    - hiring_date     : date d'arrivée dans l'école
    - courses_teached : cours qu'il ou elle enseigne
    """
    id: Optional[int] = field(default=None, init=False)
    hiring_date: date

    def add_course(self, course: Course) -> None:
        """Ajout du cours course à la liste des cours qu'il enseigne."""
        course.teacher = self

    def __str__(self) -> str:
        person_str = super().__str__()
        return f"{person_str}, arrivé(e) le {self.hiring_date}"

    def courses_teached(self):
        if self.id is not None:
            return CourseBusiness.get_courses_from_teacher(self.id)
        return None

