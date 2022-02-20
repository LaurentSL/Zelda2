from typing import Tuple

import pygame

from code import settings
from code.game_objects.game_object import GameObject


class Tile(GameObject):
    TILE_SIZE = settings.TILE_SIZE

    def __init__(self,
                 groups: pygame.sprite.AbstractGroup,
                 position: pygame.math.Vector2,
                 image_name: str = None,
                 image_and_rect: Tuple[pygame.surface.Surface, pygame.rect.Rect] = None
                 ) -> None:
        super().__init__(groups, position, image_name)

        if image_and_rect is None and image_name is None:
            self.image = pygame.surface.Surface((Tile.TILE_SIZE, Tile.TILE_SIZE))
            self.rect = self.image.get_rect(topleft=position)

        if image_and_rect is not None:
            self.image, self.rect = image_and_rect
            self.rect = self.image.get_rect(topleft=position)

        self.collision_box = self.rect.inflate(0, -10)
