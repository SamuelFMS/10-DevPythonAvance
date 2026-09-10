from abc import ABC, abstractmethod


class Business[T](ABC):
    @staticmethod
    @abstractmethod
    def add(add: T)->int:
        pass
    @staticmethod
    @abstractmethod
    def get_all():
        pass
    @staticmethod
    @abstractmethod
    def delete(delete: T):
        pass
    @staticmethod
    @abstractmethod
    def update(update: T):
        pass
