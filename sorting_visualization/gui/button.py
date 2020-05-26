from enum import Enum, auto

from window_controller import *


def text_objects(text, font):
    text_surface = font.render(text, True, color_black)
    return text_surface, text_surface.get_rect()


class Button:
    class States(Enum):
        HOVER = auto()
        PRESSED = auto()
        FOCUSED = auto()
        NORMAL = auto()

    def __init__(self, text, pos, width, height, action, args=None):
        self.text = text
        self.pos = int(pos[0]), int(pos[1])
        self.height = int(height)
        self.width = int(width)
        self.color = None
        self.state = self.States.NORMAL
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
                self.state = self.States.PRESSED
            else:
                self.state = self.States.HOVER
        else:
            self.state = self.States.NORMAL
        self.update_color()

    def update_color(self):
        if self.state == self.States.NORMAL:
            self.color = color_white
        elif self.state == self.States.PRESSED:
            self.color = color_red
        elif self.state == self.States.HOVER:
            self.color = color_gray
