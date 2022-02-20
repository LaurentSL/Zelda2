import random

from code import settings
from code import utils
from code.enemy.enemy import Enemy
from code.game_objects.floor import Floor
from code.game_objects.tile import Tile
from code.player.player import Player


def load_level(level):
    layouts = _get_layouts()
    graphics = _get_graphics()
    for style, layout in layouts.items():
        for row_index, row in enumerate(layout):
            for column_index, tile_code in enumerate(row):
                if tile_code != "-1":
                    x = column_index * Tile.TILE_SIZE
                    y = row_index * Tile.TILE_SIZE
                    _create_boundary(level, style, x, y)
                    _create_grass(level, graphics, style, x, y)
                    _create_object(level, graphics, style, x, y, tile_code)
                    _create_entities(level, style, x, y, tile_code)
    _set_player_on_enemies(level)
    level.floor = Floor([], "../graphics/tilemap/ground.png")


def _get_graphics():
    graphics = {
        settings.LAYOUT_GRASS: utils.import_all_images_and_rect_from_folder("../graphics/grass"),
        settings.LAYOUT_OBJECT: utils.import_all_images_and_rect_from_folder("../graphics/objects")
    }
    return graphics


def _get_layouts():
    layouts = {
        settings.LAYOUT_BOUNDARY: utils.import_csv_layout("../map/map_FloorBlocks.csv"),
        settings.LAYOUT_GRASS: utils.import_csv_layout("../map/map_Grass.csv"),
        settings.LAYOUT_OBJECT: utils.import_csv_layout("../map/map_Objects.csv"),
        settings.LAYOUT_ENTITIES: utils.import_csv_layout("../map/map_Entities.csv")
    }
    return layouts


def _set_player_on_enemies(level):
    for enemy in level.enemies:
        enemy.player = level.player


def _create_object(level, graphics, style, x, y, tile_code):
    if style == settings.LAYOUT_OBJECT:
        object_image = graphics[settings.LAYOUT_OBJECT][int(tile_code)]
        tile = Tile([level.visible_sprites, level.obstacle_sprites], (x, y), image_and_rect=object_image)
        tile.rect = tile.image.get_rect(topleft=(x, y - Tile.TILE_SIZE))


def _create_grass(level, graphics, style, x, y):
    if style == settings.LAYOUT_GRASS:
        random_grass_image = random.choice(graphics[settings.LAYOUT_GRASS])
        Tile([level.visible_sprites, level.obstacle_sprites, level.attackable_sprites],
             (x, y), image_and_rect=random_grass_image)


def _create_boundary(level, style, x, y):
    if style == settings.LAYOUT_BOUNDARY:
        Tile([level.obstacle_sprites], (x, y))


def _create_entities(level, style, x, y, tile_code):
    if style != settings.LAYOUT_ENTITIES:
        return
    if tile_code == settings.ENTITY_PLAYER:
        _create_player(level, x, y)
    elif tile_code in settings.ENEMIES.keys():
        _create_enemy(level, settings.ENEMIES[tile_code], x, y)


def _create_enemy(level, enemy_name, x, y):
    new_enemy = Enemy(enemy_name, (x, y), level.obstacle_sprites, level.player)
    level.enemies.append(new_enemy)
    level.visible_sprites.add(new_enemy.sprite)
    level.attackable_sprites.add(new_enemy.sprite)


def _create_player(level, x, y):
    level.player = Player((x, y), (0, -26), level.obstacle_sprites,
                          level.create_weapon, level.destroy_weapon,
                          level.create_spell, level.destroy_spell)
    level.visible_sprites.add(level.player.sprite)
