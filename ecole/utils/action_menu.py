from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class ActionMenu:
    label: str
    action: Callable