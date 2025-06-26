#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys
from pygame import Surface, Rect
from pygame.font import Font
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.score = 0
        self.start_ticks = pygame.time.get_ticks()
        self.player = EntityFactory.get_entity("Player1")
        self.obstacles = []
        self.obstacle_spawn_delay = 3000
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("Level1Bg"))
        self.entity_list.append(self.player)
        self.entity_list.extend(self.obstacles)

    def run(self):
        pygame.mixer_music.load(f"./asset/{self.name}.mp3")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            current_time = pygame.time.get_ticks()
            if (
                not self.obstacles
                and current_time - self.start_ticks > self.obstacle_spawn_delay
            ):
                obstacle = EntityFactory.get_entity("Obstacle1")
                self.obstacles.append(obstacle)
                self.entity_list.append(obstacle)
            clock.tick(60)
            elapsed_ms = pygame.time.get_ticks() - self.start_ticks
            self.score = elapsed_ms // 2
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                ent.update()
            for obstacle in self.obstacles:
                if self.player.rect.colliderect(obstacle.rect):
                    return self.handle_collision()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.level_text(24, f"Score: {self.score}", (255, 255, 255), (25, 10))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(
            name="Lucida Sans Typewriter", size=text_size
        )
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def handle_collision(self):
        pygame.mixer_music.load("./asset/Score.mp3")
        pygame.mixer_music.play(-1)
        self.game_over_screen()

    def game_over_screen(self):
        background = pygame.image.load("./asset/ScoreBg.png").convert_alpha()
        font = pygame.font.SysFont("Lucida Sans Typewriter", 20)
        text1 = font.render(f"Game Over - SCORE {self.score}", True, (255, 255, 255))
        text2 = font.render(
            "Press R to Return to the menu or Q to quit", True, (255, 255, 255)
        )
        text_rect = text1.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        text2_rect = text2.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 30))

        while True:
            self.window.fill((0, 0, 0))
            self.window.blit(background, (0, 0))
            self.window.blit(text1, text_rect)
            self.window.blit(text2, text2_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_r:
                        return "retry"
