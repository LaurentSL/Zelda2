import pygame

from code import settings


class Screen:

    def __init__(self):
        # flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
        # bits_per_pixel = 16
        # self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), flags, bits_per_pixel)
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.screen_offset = self._set_screen_offset()

    def clear(self):
        self.screen.fill('black')

    @staticmethod
    def draw():
        pygame.display.update()

    def get_camera_offset(self, camera_position):
        camera_offset = self.screen_offset - camera_position
        return camera_offset

    def _set_screen_offset(self):
        screen_half_width = self.display_surface.get_width() // 2
        screen_half_height = self.display_surface.get_height() // 2
        return pygame.math.Vector2(screen_half_width, screen_half_height)

    def debug_draw(self, camera_position, visible_sprites):
        if not settings.DEBUG:
            return
        for visible_sprite in visible_sprites:
            self._debug_draw_rect(visible_sprite.rect, settings.UI_BORDER_COLOR, camera_position)
            try:
                self._debug_draw_circle(visible_sprite.rect.center,
                                        visible_sprite.notice_radius, settings.UI_BORDER_COLOR, camera_position)
                self._debug_draw_circle(visible_sprite.rect.center,
                                        visible_sprite.attack_radius, settings.UI_BORDER_COLOR_ACTIVE, camera_position)
                self._debug_draw_rect(visible_sprite._collision_box, settings.UI_BORDER_COLOR_ACTIVE, camera_position)
            except AttributeError:
                pass

    def _debug_draw_rect(self, rect, color, camera_position):
        rect_to_draw: pygame.Rect = rect.copy()
        rect_to_draw.topleft += self.get_camera_offset(camera_position)
        pygame.draw.rect(self.display_surface, color, rect_to_draw, 3)

    def _debug_draw_circle(self, center, radius, color, camera_position):
        center += self.get_camera_offset(camera_position)
        pygame.draw.circle(self.display_surface, color, center, radius, 3)
