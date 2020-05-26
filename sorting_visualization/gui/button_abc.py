from enum import Enum, auto
from typing import Tuple

from gui.button_fsm import States
from gui.color_hepler import *


class ButtonABC:
    class States(Enum):
        HOVER = auto()
        PRESSED = auto()
        FOCUSED = auto()
        NORMAL = auto()

    def __init__(self):
        self.state = States.NORMAL
        self.color = color_white

    def update(self, mouse: Tuple[int, int, int], click: bool) -> None:
        ...

    def draw(self) -> None:
        ...

    def update_color(self) -> None:
        if self.state == States.NORMAL:
            self.color = color_white
        elif self.state == States.PRESSED:
            self.color = color_red
        elif self.state == States.HOVER:
            self.color = color_gray
