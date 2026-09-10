#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une école
"""

from views.interface_director import director_interface
from views.interface_student import student_interface
from views.interface_teacher import teacher_interface
from utils import input_number


def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre école
--------------------------""")

    # initialisation d'un ensemble de cours, enseignants et élèves composant l'école
    # school.init_static()

    # affichage de la liste des cours, leur enseignant et leurs élèves

    program_running = True
    while program_running:
        print("Authentification")
        print("1- s'authentifier en eleve")
        print("2- s'authentifier en enseignant")
        print("3- s'authentifier en directeur")
        print("4- quitter l'application")

        choice = input_number("Authentification ? (Entrez le numéro) ", 1, 4)
        if choice == 1:
            student_interface()
        elif choice == 2:
            teacher_interface()
        elif choice == 3:
            director_interface()
        elif choice == 4:
            program_running = False
if __name__ == '__main__':
    main()
