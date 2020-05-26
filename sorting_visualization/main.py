from __future__ import annotations

import sys
import random
import colorsys

import pygame

from sorters.bubble_sorter import BubbleSorter
from sorters.gnome_sorter import GnomeSorter
from sorters.shaker_sorter import ShakerSorter
from sorters.selection_sorter import SelectionSorter
from sorters.insertion_sorter import InsertionSorter
from gui.button import Button
from gui.switch_button import SwitchButton
from window_controller import screen, SCR_W, SCR_H
from box import Box

SPEED = 10
DELAY = 0.5
SORTERS = [BubbleSorter, GnomeSorter, ShakerSorter, SelectionSorter, InsertionSorter]
b = None


def get_color(n):
    return colorsys.hsv_to_rgb(n, 1, 255)


def shuffle():
    global boxes, b, running, sort, lst
    box_spacing = 1
    box_width = (SCR_W - box_spacing * (n - 1)) / n
    max_box_height = SCR_H * 0.8
    lst = list(range(1, n + 1))
    rand_lst = list(lst)
    random.shuffle(rand_lst)
    boxes = []
    for i, item in enumerate(rand_lst):
        boxes.append(
            Box(((box_spacing + box_width) * i, SCR_H * 0.9),
                box_width,
                max_box_height * (item / n),
                get_color(lst.index(item) / n + 0.9),
                ))
    b = b or iter(BubbleSorter(boxes))


n = 50
shuffle()


def set_sorter(sorter):
    global b, running
    shuffle()
    b = iter(sorter(boxes))
    running = True


def set_n(i):
    global n, running
    if n != i:
        n = i
        shuffle()
        running = True


running = False


def update(mouse, click):
    global running
    for _ in range(SPEED):
        if running:
            try:
                next(b)
            except StopIteration:
                running = False

    set_50_btn.update(mouse, click)
    set_100_btn.update(mouse, click)
    set_200_btn.update(mouse, click)

    sorter_buttons.update(mouse, click)


def draw():
    screen.fill((0, 0, 0))
    for i in boxes:
        i.draw()

    set_50_btn.draw()
    set_100_btn.draw()
    set_200_btn.draw()

    sorter_buttons.draw()

    pygame.display.update()


set_50_btn = Button(
    "50",
    (620, SCR_H * 0.92),
    50,
    SCR_H * 0.06,
    action=set_n,
    args=50,
)

set_100_btn = Button(
    "100",
    (680, SCR_H * 0.92),
    50,
    SCR_H * 0.06,
    action=set_n,
    args=100,
)

set_200_btn = Button(
    "200",
    (740, SCR_H * 0.92),
    50,
    SCR_H * 0.06,
    action=set_n,
    args=200,
)

sorter_buttons = SwitchButton(
    pos=(50, SCR_H * 0.92),
    width=80,
    height=SCR_H * 0.06,
    action=set_sorter,
    args=SORTERS,
    initial_arg=BubbleSorter
)

while True:
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
    mouse = pygame.mouse.get_pos()

    update(mouse, click)
    draw()
