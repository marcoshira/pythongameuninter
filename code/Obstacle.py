#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import random
from code.Entity import Entity
from code.Const import ENTITY_SPEED, WIN_WIDTH


class Obstacle(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = random.randint(8, 16)

    def move(self):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.rect.x = WIN_WIDTH + random.randint(50, 200)
            self.speed = random.randint(8, 16)
