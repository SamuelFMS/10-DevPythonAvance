#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une école
"""
from utils.menu import Menu
from views.interface_director import director_interface
from views.interface_student import student_interface
from views.interface_teacher import teacher_interface


def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre école
--------------------------""")

    authentification_menu = Menu("Authentification")
    authentification_menu.add_action("S'authentifier en tant qu'élève", student_interface)
    authentification_menu.add_action("S'authentifier en tant qu'enseignant", teacher_interface)
    authentification_menu.add_action("S'authentifier en tant que directeur", director_interface)
    authentification_menu.show_menu(True)


if __name__ == "__main__":
    main()
