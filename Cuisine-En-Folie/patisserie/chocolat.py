from patisserie import unite
from patisserie.ingredient import Ingredient


class Chocolat(Ingredient):
    def get_unite(self) -> unite.Unite:
        return unite.Unite.GRAMME