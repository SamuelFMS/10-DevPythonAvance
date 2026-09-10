
import threading
from abc import ABC, abstractmethod
from dataclasses import dataclass
from threading import Thread
from patisserie.recipient import Recipient


@dataclass(eq=False)
class Commis(ABC, Thread):
    recipient: Recipient
    def __post_init__(self):
        threading.Thread.__init__(self)

    @abstractmethod
    def run(self):
        pass