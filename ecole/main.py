#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une école
"""
from business.course_business import CourseBusiness


def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre école
--------------------------""")

    # initialisation d'un ensemble de cours, enseignants et élèves composant l'école
    # school.init_static()

    # affichage de la liste des cours, leur enseignant et leurs élèves

    list_courses = CourseBusiness.get_all_course()
    for course in list_courses:
        print(course)
        for student in course.students_taking_it:
            print("- ", student)
        print("")
if __name__ == '__main__':
    main()
