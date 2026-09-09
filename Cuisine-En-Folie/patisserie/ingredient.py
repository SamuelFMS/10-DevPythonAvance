from abc import ABC, abstractmethod
from dataclasses import dataclass

from patisserie import unite

@dataclass
class Ingredient(ABC):
    quantite: int

    @abstractmethod
    def get_nom(self) -> str:
        pass

    @abstractmethod
    def get_unite(self) -> unite.Unite:
        pass