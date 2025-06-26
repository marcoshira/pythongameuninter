#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys

from code.Menu import Menu
from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                while True:
                    level = Level(self.window, "Level1", menu_return)
                    level_return = level.run()
                    if level_return == "retry":
                        continue
                    else:
                        break
            else:
                pygame.quit()
                sys.exit()
