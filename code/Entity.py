#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from abc import ABC, abstractmethod
from code.Helper import resource_path


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load(
            resource_path("./asset/" + name + ".png")
        ).convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(
        self,
    ):
        pass

    def update(self):
        pass
