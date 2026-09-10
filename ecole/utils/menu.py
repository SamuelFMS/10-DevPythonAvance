from collections.abc import Callable
from dataclasses import dataclass, field

from utils.action_menu import ActionMenu
from utils.input_utils import input_number


@dataclass
class Menu():
    title: str
    listeAction: list[ActionMenu] = field(default_factory=list)

    def add_action(self, label: str, action: Callable):
        self.listeAction.append(ActionMenu(label, action))

    def show_menu(self, continueRunning: bool):
        print(self.title)
        index = 1
        for action in self.listeAction:
            print(f"{index}: {action.label}")
            index += 1
        if continueRunning:
            print(f"{index}: Arreter {self.title}")
            index += 1
        choice = input_number(f"Entrez votre choix: ",1, index-1)
        if choice == index-1:
            continueRunning = False
        else:
            self.listeAction[choice-1].action()
        if continueRunning:
            self.show_menu(continueRunning)
