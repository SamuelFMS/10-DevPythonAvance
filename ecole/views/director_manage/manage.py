import string
from abc import ABC, abstractmethod
from os import name

from utils.menu import Menu


class Manage(ABC):
    @abstractmethod
    def create(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def read_all(self):
        pass
    @abstractmethod
    def remove(self):
        pass

    def manage(self):
        menu:Menu = Menu("Gestion " + self.get_name())
        menu.add_action("Creer un "+self.get_name(), self.create)
        menu.add_action("Modifier un "+self.get_name(), self.update)
        menu.add_action("Supprimer un "+self.get_name(), self.remove)
        menu.add_action("Affiche la listes des "+self.get_name(), self.read_all)
        menu.show_menu(True)

    @abstractmethod
    def get_name(self):
        pass
    @abstractmethod
    def get_name_pluriels(self):
        pass