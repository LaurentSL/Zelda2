import pygame.math

from code.game_objects.game_object import GameObject


class Floor(GameObject):

    def __init__(self, groups, image_name):
        super().__init__(groups, pygame.math.Vector2(0, 0), image_name)

    def draw(self, display_surface, camera_offset):
        display_surface.blit(self.image, self.rect.topleft + camera_offset)
