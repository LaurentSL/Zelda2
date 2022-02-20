import sys

import pygame


class InputComponent:

    def __init__(self, player):
        self.keys = None
        self.player = player

    def update(self):
        if self.player.is_attacking:
            return
        self.keys = pygame.key.get_pressed()
        self.exit()
        self.direction()
        self.attack()
        self.magic()
        self.switch_weapon()
        self.switch_spell()

    def exit(self):
        if self.keys[pygame.K_ESCAPE]:
            sys.exit(0)

    def direction(self):
        x = self.keys[pygame.K_RIGHT] - self.keys[pygame.K_LEFT]
        y = self.keys[pygame.K_DOWN] - self.keys[pygame.K_UP]
        self.player.direction_wanted = pygame.Vector2(x, y)

    def attack(self):
        self.player.ask_to_attack = self.keys[pygame.K_SPACE]

    def magic(self):
        self.player.ask_to_send_spell = self.keys[pygame.K_LCTRL]

    def switch_weapon(self):
        if self.keys[pygame.K_a]:
            self.player.attack_component.switch_weapon()

    def switch_spell(self):
        if self.keys[pygame.K_e]:
            self.player.magic_component.switch_spell()

