import pygame.sprite

from code.components.movement_component import MovementComponent
from code.data import weapons
from code.game_objects.game_object import GameObject


class Weapon(GameObject):

    def __init__(self, groups, index, direction_name, player_rect):
        super().__init__(groups, player_rect.center)
        self.index = index
        self.load_image_and_rect(self.get_image_name(direction_name))
        self.set_position(direction_name, player_rect)

    def __repr__(self):
        return f"Weapon {self.get_name()}: position={self.position}"

    def set_position(self, direction_name, player_rect):
        if direction_name == MovementComponent.UP:
            self.position = player_rect.midtop + pygame.math.Vector2(5, -self.rect.height//2)
        elif direction_name == MovementComponent.DOWN:
            self.position = player_rect.midbottom + pygame.math.Vector2(-20, 0)
        elif direction_name == MovementComponent.LEFT:
            self.position = player_rect.midleft + pygame.math.Vector2(-self.rect.width, 6)
        else:
            self.position = player_rect.midright + pygame.math.Vector2(0, 6)

    def get_name(self):
        return weapons.get_name(self.index)

    def get_graphics(self):
        return weapons.get_graphics(self.index)

    def get_cooldown(self):
        return weapons.get_cooldown(self.index)

    def get_damage(self):
        return weapons.get_damage(self.index)

    def get_image_name(self, direction_name):
        image_name = f"{self.get_graphics()}{direction_name}.png"
        return image_name
