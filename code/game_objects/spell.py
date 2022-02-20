import pygame.sprite

from code.components.movement_component import MovementComponent
from code import utils
from code.data import spells
from code.game_objects.game_object import GameObject


class Spell(GameObject):

    def __init__(self, groups, index, direction_name, player_rect):
        super().__init__(groups)
        self.index = index
        self.load_image_and_rect(f"{self.get_graphics()}{direction_name}.png")
        self.set_position(direction_name, player_rect)

    def set_position(self, direction_name, player_rect):
        if direction_name == MovementComponent.UP:
            self.position = player_rect.midtop + pygame.math.Vector2(10, 0)
        elif direction_name == MovementComponent.DOWN:
            self.position = player_rect.midbottom + pygame.math.Vector2(-10, 0)
        elif direction_name == MovementComponent.LEFT:
            self.position = player_rect.midleft + pygame.math.Vector2(0, 16)
        else:
            self.position = player_rect.midright + pygame.math.Vector2(0, 16)

    def get_name(self):
        return spells.get_name(self.index)

    def get_graphics(self):
        return spells.get_graphics(self.index)

    def get_strength(self):
        return spells.get_strength(self.index)

    def get_cost(self):
        return spells.get_cost(self.index)
