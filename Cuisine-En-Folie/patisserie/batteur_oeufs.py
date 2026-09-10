
import threading
import time
from dataclasses import dataclass

from patisserie.commis import Commis
from patisserie.oeuf import Oeuf

@dataclass(eq=False)
class BatteurOeufs(Commis):
    def run(self):
        if isinstance(self.recipient.ingredient, Oeuf):
            # on suppose qu'il faut 8 tours de batteur par œuf présent dans le bol
            nb_tours = self.recipient.ingredient.quantite * 8
            for no_tour in range(1, nb_tours + 1):
                print(f"\tJe bats les {self.recipient.ingredient.quantite} oeufs, tour n°{no_tour}")
                time.sleep(0.5)  # temps supposé d'un tour de batteur
        else:
            print("Ce ne sont pas des Oeufs")
