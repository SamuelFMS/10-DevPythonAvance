from dataclasses import dataclass

from patisserie.ingredient import Ingredient


@dataclass
class Recipient:
    nom_recipient: str
    ingredient: Ingredient
