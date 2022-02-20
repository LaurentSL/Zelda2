import pygame

from code.components.animation_component import AnimationComponent
from code.components.attack_component import AttackComponent
from code.components.magic_component import MagicComponent
from code.player.player_state_controller import PlayerStateController
from code.player.player_stats import Stats


class Player:
    IDLE = '_idle'
    ATTACK = '_attack'
    MOVE = ''
    CHARACTER_PATH = "../graphics/player/"
    ANIMATIONS = ['up', 'down', 'left', 'right', 'up_idle', 'down_idle', 'left_idle', 'right_idle',
                  'up_attack', 'down_attack', 'left_attack', 'right_attack']

    def __init__(self, position, collide_inflate, obstacle_sprites,
                 create_weapon_function, destroy_weapon_function,
                 create_spell_function, destroy_spell_function):
        self.stats = Stats(health=100, energy=60, attack=10, magic=4, speed=5)
        self.obstacle_sprites = obstacle_sprites
        self._state_controller = PlayerStateController(self)
        self.direction_name = "down"
        self.animation_component = AnimationComponent([], Player.CHARACTER_PATH, Player.ANIMATIONS,
                                                      collide_inflate, position)
        self.attack_component = AttackComponent(create_weapon_function, destroy_weapon_function)
        self.magic_component = MagicComponent(create_spell_function, destroy_spell_function)
        self.ask_to_attack = False
        self.direction_wanted = pygame.Vector2(0, 0)
        self.ask_to_send_spell = False

    @property
    def ask_to_move(self):
        return self.direction_wanted != pygame.Vector2(0, 0)

    @property
    def health(self):
        return self.stats.health

    @property
    def health_percent(self):
        return self.stats.get_health_percent()

    @property
    def energy(self):
        return self.stats.energy

    @property
    def energy_percent(self):
        return self.stats.get_energy_percent()

    @property
    def attack(self):
        return self.stats.attack

    @property
    def magic(self):
        return self.stats.magic

    @property
    def speed(self):
        return self.stats.speed

    @property
    def experience(self):
        return self.stats.experience

    @property
    def position(self):
        return self.animation_component.position

    @property
    def sprite(self):
        return self.animation_component

    def update(self):
        self._state_controller.update()
        self.switch_animation()
        self.attack_component.update()
        self.magic_component.update()
        self.animation_component.update()

    def create_attack(self):
        self.attack_component.attack()

    @property
    def is_attacking(self):
        return self.attack_component.is_attacking()

    def switch_animation(self):
        animation_name = f"{self.direction_name}"
        if self.get_status_name() != "move":
            animation_name += f"_{self.get_status_name()}"
        self.animation_component.switch_animation(animation_name)

    def get_status_name(self):
        return self._state_controller.get_status_name()
