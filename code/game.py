import sys

import pygame

from code.level import Level
from code.components.input_component import InputComponent
from code.screen import Screen
from code import settings
from code.ui import UI


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.SCREEN_TITLE)
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])
        self.clock = pygame.time.Clock()
        self.screen = Screen()
        self.level = Level()
        self.player = self.level.player
        self.screen.level = self.level
        self.ui = UI()
        self.input = InputComponent(self.player)

    def run(self):
        while not self._is_exit():
            self._update()
            self._draw()
            self._fps()
        self._exit()

    def _update(self):
        self.input.update()
        self.level.update()

    def _draw(self):
        player_position = self.player.position
        camera_offset = self.screen.get_camera_offset(player_position)
        self.level.draw(self.screen.display_surface, camera_offset)
        self.ui.draw(self.player)
        self.screen.debug_draw(player_position, self.level.visible_sprites)
        self.screen.draw()

    def _fps(self):
        self.clock.tick(settings.FPS)

    @staticmethod
    def _is_exit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    @staticmethod
    def _exit():
        pygame.quit()
        sys.exit()
