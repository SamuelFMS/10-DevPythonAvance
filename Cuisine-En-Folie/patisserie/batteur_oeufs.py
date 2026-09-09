import threading
import time

from patisserie.commis import Commis
from patisserie.oeuf import Oeuf


class BatteurOeufs(Commis):
    def __init__(self, oeuf:Oeuf):
        super().__init__()
        self.oeuf = oeuf

    def run(self):
        # on suppose qu'il faut 8 tours de batteur par œuf présent dans le bol
        nb_tours = self.oeuf.quantite * 8
        for no_tour in range(1, nb_tours + 1):
            print(f"\tJe bats les {self.oeuf.quantite} oeufs, tour n°{no_tour}")
            time.sleep(0.5)  # temps supposé d'un tour de batteur
