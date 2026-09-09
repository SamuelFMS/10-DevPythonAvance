from dataclasses import dataclass

from patisserie import unite
from patisserie.ingredient import Ingredient


@dataclass
class Chocolat(Ingredient):
    def get_nom(self) -> str:
        return "Chocolat"

    def get_unite(self) -> unite.Unite:
        return unite.Unite.GRAMME