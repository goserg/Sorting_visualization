from typing import Tuple

import pygame

from window_controller import screen
from gui.color_hepler import *


class Arrow:
    def __init__(self, pos: Tuple[int, int], size: int, left: bool = False) -> None:
        if left:
            self.rect = pygame.Rect(pos[0] - size // 2, pos[1], size // 2, size)
            self.shape = ((self.rect.x + self.rect.width - 1, self.rect.y),
                          (self.rect.x, self.rect.y + self.rect.height / 2),
                          (self.rect.x + self.rect.width - 1, self.rect.y + self.rect.height - 1),
                          )
        else:
            self.rect = pygame.Rect(pos[0], pos[1], size//2, size)
            self.shape = ((self.rect.x, self.rect.y),
                          (self.rect.x + self.rect.width - 1, self.rect.y + self.rect.height / 2),
                          (self.rect.x, self.rect.y + self.rect.height - 1),
                          )
        self.color = color_white

    def draw(self) -> None:
        pygame.draw.polygon(screen, self.color, self.shape)

    def update(self, mouse) -> bool:
        if (self.rect.x < mouse[0] < self.rect.x + self.rect.width
                and self.rect.y < mouse[1] < self.rect.y + self.rect.height):
            self.color = color_gray
            return True
        else:
            self.color = color_white
