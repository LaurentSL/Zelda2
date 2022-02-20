import pygame

from code import settings
from code import utils


class UI:

    def __init__(self):
        # general
        self.display_surface = pygame.display.get_surface()
        font_filename = utils.get_full_filename(settings.UI_FONT_FILENAME)
        self.font = pygame.font.Font(font_filename, settings.UI_FONT_SIZE)
        # bar setup
        self.health_bar_rect = pygame.Rect(10, 10, settings.HEALTH_BAR_WIDTH, settings.BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 34, settings.ENERGY_BAR_WIDTH, settings.BAR_HEIGHT)

    def draw(self, player):
        self.draw_bar(player.health_percent, self.health_bar_rect, settings.HEALTH_COLOR)
        self.draw_bar(player.energy_percent, self.energy_bar_rect, settings.ENERGY_COLOR)
        self.draw_experience(player.experience)
        self.draw_selected(10, player.attack_component.weapon_image, player.attack_component.is_switching_weapon)
        self.draw_selected(95, player.magic_component.spell_image, player.magic_component.is_switching_spell)

    def draw_selected(self, x, image, has_switch):
        y = settings.SCREEN_HEIGHT - settings.ITEM_BOX_SIZE - 20
        color = settings.UI_BORDER_COLOR_ACTIVE if has_switch else settings.UI_BORDER_COLOR
        self.selection_box(x, y, image, color)

    def draw_bar(self, percent, bg_rect, color):
        pygame.draw.rect(self.display_surface, settings.UI_BG_COLOR, bg_rect)
        percent_rect = bg_rect.copy()
        percent_rect.width = bg_rect.width * percent
        pygame.draw.rect(self.display_surface, color, percent_rect)
        pygame.draw.rect(self.display_surface, settings.UI_BORDER_COLOR, bg_rect, settings.OUTLINE_WIDTH)

    def draw_experience(self, experience):
        position = (20, 30)
        text = f"Experience: {int(experience)}"
        utils.draw_text(self.display_surface, text, self.font, settings.TEXT_COLOR, position, 'bottomright')

    def selection_box(self, left, top, image, border_color):
        bg_rect = pygame.Rect(left, top, settings.ITEM_BOX_SIZE, settings.ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, settings.UI_BG_COLOR, bg_rect)
        if image:
            img_surf, img_rect = image
            img_rect.center = bg_rect.center
            self.display_surface.blit(img_surf, img_rect)
        pygame.draw.rect(self.display_surface, border_color, bg_rect, settings.OUTLINE_WIDTH)
