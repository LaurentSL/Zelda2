import pygame

from code import level_fabric
from code.game_objects.weapon import Weapon
from code.y_sort_camera_group import YSortCameraGroup


class Level:

    def __init__(self):

        self.floor = None
        self.player = None
        self.enemies = []

        # Sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # attack sprites
        self.current_weapon = None
        self.current_spell = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        level_fabric.load_level(self)

    def update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update()
        self.player_attack_logic()
        self.visible_sprites.update()

    def draw(self, display_surface, camera_offset):
        self.floor.draw(display_surface, camera_offset)
        self.visible_sprites.custom_draw(display_surface, camera_offset)

    def create_weapon(self, weapon_index):
        direction_name = self.player.movement_component.get_direction_name()
        rect = self.player.animation_component.rect
        self.current_weapon = Weapon([self.visible_sprites, self.attack_sprites],
                                     weapon_index, direction_name, rect)

    def destroy_weapon(self):
        if self.current_weapon:
            self.current_weapon.kill()
            self.current_weapon = None

    def create_spell(self, spell_index):
        # TODO: afficher le sort à l'écran - particles
        print("Create spell")

    def destroy_spell(self):
        if self.current_spell:
            self.current_spell.kill()
            self.current_spell = None

    def player_attack_logic(self):
        for attack_sprite in self.attack_sprites:
            collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, dokill=False)
            for target_sprite in collision_sprites:
                # Todo: supprime le sprite mais pas l'ennemi !
                # if hasattr(target_sprite, 'destroy'):
                target_sprite.kill()
