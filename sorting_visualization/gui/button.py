from typing import Tuple, Callable, Any

import pygame

from window_controller import screen
from gui.color_hepler import *
from gui.button_fsm import States
from gui.button_abc import ButtonABC


def text_objects(text, font):
    text_surface = font.render(text, True, color_black)
    return text_surface, text_surface.get_rect()


class Button(ButtonABC):
    def __init__(self,
                 text: str,
                 pos: Tuple[int, int],
                 width: int,
                 height: int,
                 action: Callable,
                 args: Any = None,
                 ) -> None:
        super().__init__()
        self.text = text
        self.pos = int(pos[0]), int(pos[1])
        self.height = int(height)
        self.width = int(width)
        self.action = action
        self.args = args
        self.update_color()

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], self.width, self.height))
        large_text = pygame.font.Font('freesansbold.ttf', 15)
        text_surf, text_rect = text_objects(self.text, large_text)
        text_rect.center = (self.pos[0] + self.width / 2, self.pos[1] + self.height / 2)
        screen.blit(text_surf, text_rect)

    def update(self, mouse, click):
        mouse_pressed = pygame.mouse.get_pressed()
        if (self.pos[0] < mouse[0] < self.pos[0] + self.width
                and self.pos[1] < mouse[1] < self.pos[1] + self.height):
            if click:
                if self.args:
                    self.action(self.args)
                else:
                    self.action()
            if mouse_pressed[0]:
                self.state = States.PRESSED
            else:
                self.state = States.HOVER
        else:
            self.state = States.NORMAL
        self.update_color()
