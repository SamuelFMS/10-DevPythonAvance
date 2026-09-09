import threading
from abc import ABC, abstractmethod


class Commis(ABC, threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    @abstractmethod
    def run(self):
        pass