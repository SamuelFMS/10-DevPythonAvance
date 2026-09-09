from abc import ABC

from patisserie import unite


class Ingredient(ABC):
    nom: str
    quantite: int
    unite: unite