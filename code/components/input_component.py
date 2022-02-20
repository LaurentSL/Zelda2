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
        if x == y == 0:
            self.player.stop()
        else:
            if not self.player.is_attacking:
                self.player.movement_component.can_move()
            self.player.movement_component.set_normalized_direction(x, y)

    def attack(self):
        if self.keys[pygame.K_SPACE]:
            direction = self.player.movement_component.direction
            self.player.stop()
            self.player.create_attack()

    def magic(self):
        if self.keys[pygame.K_LCTRL] and not self.player.attack_component.is_attacking():
            self.player.stop()
            self.player.magic_component.create_attack()

    def switch_weapon(self):
        if self.keys[pygame.K_a]:
            self.player.attack_component.switch_weapon()

    def switch_spell(self):
        if self.keys[pygame.K_e]:
            self.player.magic_component.switch_spell()

