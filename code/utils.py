import csv
import pathlib

import pygame

from code import settings

pygame.init()
debug_font = pygame.font.Font(None, 30)


def debug(info, y=10, x=10):
    display_surface = pygame.display.get_surface()
    draw_text(display_surface, info, debug_font, "White", (x, y))


def draw_text(display_surface, text, font, color, position, anchor='topleft'):
    text_surf = font.render(str(text), False, color)
    text_rect = text_surf.get_rect(topleft=(0, 0))
    if "top" in anchor:
        text_rect.y += position[1]
    if "bottom" in anchor:
        text_rect.y = settings.SCREEN_HEIGHT - text_rect.height - position[1]
    if "left" in anchor:
        text_rect.x += position[0]
    if "right" in anchor:
        text_rect.x = settings.SCREEN_WIDTH - text_rect.width - position[0]
    pygame.draw.rect(display_surface, settings.UI_BG_COLOR, text_rect.inflate(20, 20))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, settings.UI_BORDER_COLOR, text_rect.inflate(20, 20), settings.OUTLINE_WIDTH)


def load_image_and_rect(relative_file_path, position=(0, 0), anchor='topleft'):
    image_name = get_full_filename(relative_file_path)
    image = pygame.image.load(image_name).convert_alpha()
    if anchor == 'center':
        rect = image.get_rect(center=position)
    else:
        rect = image.get_rect(topleft=position)
    return image, rect


def import_csv_layout(relative_file_path):
    csv_name = get_full_filename(relative_file_path)
    terrain_map = []
    with open(csv_name) as level_map:
        layout = csv.reader(level_map, delimiter=",")
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_all_images_and_rect_from_folder(relative_folder_path):
    surface_list = []
    folder_path = get_full_filename(relative_folder_path)
    for file in folder_path.glob("*.*"):
        image_surface, image_rect = load_image_and_rect(file)
        surface_list.append((image_surface, image_rect))
    return surface_list


def get_full_filename(relative_file_path):
    file_path = pathlib.Path(__file__).resolve().parent
    csv_name = file_path / relative_file_path
    return csv_name
