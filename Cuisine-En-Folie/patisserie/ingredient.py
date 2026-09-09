from abc import ABC, abstractmethod

from patisserie import unite


class Ingredient(ABC):
    nom: str
    quantite: int

    @abstractmethod
    def get_unite(self) -> unite.Unite:
        pass