from dataclasses import dataclass

from patisserie.ingredient import Ingredient


@dataclass
class Appareil:
    list_ingredients: list[Ingredient]