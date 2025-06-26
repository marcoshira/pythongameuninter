#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys
from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.velocity_y = 0
        self.is_jumping = False
        self.gravity = 1
        self.jump_strength = -15

    def update(self):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
        ground_y = WIN_HEIGHT - 20
        if self.rect.bottom >= ground_y:
            self.rect.bottom = ground_y
            self.velocity_y = 0
            self.is_jumping = False

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.is_jumping:
                        self.velocity_y = self.jump_strength
                        self.is_jumping = True
