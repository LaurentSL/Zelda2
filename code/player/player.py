from code.components.animation_component import AnimationComponent
from code.components.attack_component import AttackComponent
from code.components.magic_component import MagicComponent
from code.components.movement_component import MovementComponent
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
        self._stats = Stats(health=100, energy=60, attack=10, magic=4, speed=5)
        self._state_controller = PlayerStateController(self)
        self.animation_component = AnimationComponent([], Player.CHARACTER_PATH, Player.ANIMATIONS,
                                                      collide_inflate, position)
        self.movement_component = MovementComponent(obstacle_sprites, self.animation_component,
                                                    self.animation_component.collision_box,
                                                    self._stats.speed)
        self.attack_component = AttackComponent(create_weapon_function, destroy_weapon_function)
        self.magic_component = MagicComponent(create_spell_function, destroy_spell_function)

    @property
    def health(self):
        return self._stats.health

    @property
    def health_percent(self):
        return self._stats.get_health_percent()

    @property
    def energy(self):
        return self._stats.energy

    @property
    def energy_percent(self):
        return self._stats.get_energy_percent()

    @property
    def attack(self):
        return self._stats.attack

    @property
    def magic(self):
        return self._stats.magic

    @property
    def speed(self):
        return self._stats.speed

    @property
    def experience(self):
        return self._stats.experience

    @property
    def position(self):
        return self.animation_component.position

    @property
    def sprite(self):
        return self.animation_component

    def update(self):
        self.switch_animation()
        self.attack_component.update()
        self.magic_component.update()
        self.movement_component.update()
        # self.animation_component.position = self.movement_component.position
        self.animation_component.update()

    def stop(self):
        self.movement_component.stop()

    def create_attack(self):
        self.attack_component.attack()

    @property
    def is_attacking(self):
        return self.attack_component.is_attacking()

    def switch_animation(self):
        animation_name = self.movement_component.get_direction_name() + self.get_status_name()
        self.animation_component.switch_animation(animation_name)

    def get_status_name(self):
        if self.attack_component.is_attacking():
            return self.ATTACK
        elif self.movement_component.is_moving():
            return self.MOVE
        else:
            return self.IDLE
