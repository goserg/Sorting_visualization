import pygame

from window_controller import screen


class Box:
    def __init__(self, pos, width, height, color):
        self.pos = int(pos[0]), int(pos[1])
        self.height = int(height)
        self.width = int(width)
        self.color = color

    def __lt__(self, other):
        return self.height < other.height

    def __gt__(self, other):
        return self.height > other.height

    def __le__(self, other):
        return self.height <= other.height

    def __ge__(self, other):
        return self.height >= other.height

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], self.width, -self.height))