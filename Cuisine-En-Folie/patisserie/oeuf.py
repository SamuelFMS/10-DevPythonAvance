from dataclasses import dataclass

from patisserie import unite
from patisserie.ingredient import Ingredient

@dataclass
class Oeuf(Ingredient):
    def get_nom(self) -> str:
        return "Oeuf"

    def get_unite(self) -> unite.Unite:
        return unite.Unite.PIECE