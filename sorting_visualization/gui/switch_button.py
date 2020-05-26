from typing import Tuple, List, Callable, Any

import pygame

from window_controller import screen
from gui.color_hepler import *
from gui.arrow import Arrow
from gui.button_fsm import States
from gui.button_abc import ButtonABC


def text_objects(text, font):
    text_surface = font.render(text, True, color_black)
    return text_surface, text_surface.get_rect()


class SwitchButton(ButtonABC):
    def __init__(self,
                 pos: Tuple[int, int],
                 width: int,
                 height: int,
                 action: Callable,
                 args: List[Any],
                 initial_arg: Any,
                 ) -> None:
        super().__init__()
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.width = width
        self.height = height
        self.action = action
        self.args = args
        self.current = initial_arg
        self.left_arrow = Arrow((pos[0] - 4, pos[1]), height, left=True)
        self.right_arrow = Arrow((pos[0] + width + 4, pos[1]), height)
        self.update_color()

    def update(self, mouse: Tuple[int, int, int], click: bool) -> None:
        mouse_pressed = pygame.mouse.get_pressed()
        if (self.pos_x < mouse[0] < self.pos_x + self.width
                and self.pos_y < mouse[1] < self.pos_y + self.height):
            if click:
                self.action(self.current)
            if mouse_pressed[0]:
                self.state = States.PRESSED
            else:
                self.state = States.HOVER
        else:
            self.state = States.NORMAL

        if self.left_arrow.update(mouse):
            if click:
                self.current = self.args[self.args.index(self.current) - 1]
        elif self.right_arrow.update(mouse):
            if click:
                index = self.args.index(self.current) + 1
                index %= len(self.args)
                self.current = self.args[index]
        self.update_color()

    def draw(self) -> None:
        pygame.draw.rect(screen, self.color, (self.pos_x, self.pos_y, self.width, self.height))
        large_text = pygame.font.Font('freesansbold.ttf', 15)
        text_surf, text_rect = text_objects(self.current.name, large_text)
        text_rect.center = (self.pos_x + self.width / 2, self.pos_y + self.height / 2)
        screen.blit(text_surf, text_rect)

        self.left_arrow.draw()
        self.right_arrow.draw()
