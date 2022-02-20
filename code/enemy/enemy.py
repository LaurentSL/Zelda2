import pygame.math

from code.components.animation_component import AnimationComponent
from code.data import monsters
from code.enemy.enemy_stats import EnemyStats
from code.enemy.enemy_state_controller import EnemyStateController


class Enemy:
    ANIMATIONS = ['idle', 'attack', 'move']
    GRAPHIC_PATH = "../graphics/monsters/"

    def __init__(self, monster_name, position, obstacle_sprites, player):
        self.monster_name = monster_name
        self.stats = EnemyStats.create_enemy_stats(self.monster_name)
        self.player = player
        self.obstacle_sprites = obstacle_sprites
        self.animation_component = self.create_animation(monster_name, position,
                                                         self.stats.notice_radius, self.stats.attack_radius)
        self.state_controller = EnemyStateController(self)

    @property
    def sprite(self):
        return self.animation_component

    def create_animation(self, monster_name, position, notice_radius, attack_radius):
        animation_path = f"{self.GRAPHIC_PATH}{self.monster_name}/"
        monster_index = monsters.get_index(monster_name)
        collide_inflate = monsters.get_collide_inflate(monster_index)
        return AnimationComponent([], animation_path, self.ANIMATIONS, collide_inflate, position,
                                  notice_radius, attack_radius)

    @property
    def position(self):
        return self.animation_component.rect.center

    def update(self):
        self.state_controller.update()
        self.draw()

    def get_distance_to_player(self):
        direction_to_player = self.get_direction_to_player()
        distance_to_player = direction_to_player.magnitude()
        return distance_to_player

    def get_direction_to_player(self):
        enemy_vector = pygame.math.Vector2(self.position)
        player_vector = pygame.math.Vector2(self.player.position)
        direction_to_player = (player_vector - enemy_vector)
        return direction_to_player

    def draw(self):
        status_name = self.state_controller.get_status_name()
        if status_name == "can_attack":
            status_name = "idle"
        self.animation_component.switch_animation(status_name)
        self.animation_component.update()

    def is_in_notice_radius(self):
        return 0 < self.get_distance_to_player() <= self.stats.notice_radius

    def is_in_attack_radius(self):
        return 0 < self.get_distance_to_player() <= self.stats.attack_radius

    def is_attacking(self):
        return self.state_controller.is_attacking()
