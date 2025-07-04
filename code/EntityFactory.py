#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Obstacle import Obstacle
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case "Level1Bg":
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f"Level1Bg{i}", (0, 0)))
                    list_bg.append(Background(f"Level1Bg{i}", (WIN_WIDTH, 0)))
                return list_bg
            case "Player1":
                return Player("Player1", (30, WIN_HEIGHT - 20))
            case "Obstacle1":
                return Obstacle("Obstacle1", (WIN_WIDTH + 100, WIN_HEIGHT - 40))
