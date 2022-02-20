import pygame as pygame


class YSortCameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()

    def custom_draw(self, display_surface, camera_offset):
        for sprite in sorted(self.sprites(), key=lambda sprite_y: sprite_y.rect.centery):
            offset_position = sprite.rect.topleft + camera_offset
            display_surface.blit(sprite.image, offset_position)
