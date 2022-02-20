import string

from code.data import monsters


class EnemyStats:

    @classmethod
    def create_enemy_stats(cls, name):
        index = monsters.get_index(name)
        return cls(health=monsters.get_health(index),
                   experience=monsters.get_experience(index),
                   damage=monsters.get_damage(index),
                   attack_type=monsters.get_attack_type(index),
                   attack_sound=monsters.get_attack_sound(index),
                   speed=monsters.get_speed(index),
                   resistance=monsters.get_resistance(index),
                   attack_radius=monsters.get_attack_radius(index),
                   notice_radius=monsters.get_notice_radius(index),
                   collide_inflate=monsters.get_collide_inflate(index)
                   )

    def __init__(self, health: int, experience: int, damage: int, attack_type: string, attack_sound: string,
                 speed: int, resistance: int, attack_radius: int, notice_radius: int, collide_inflate):
        self.health = health
        self.health_max = self.health
        self.experience = experience
        self.damage = damage
        self.attack_type = attack_type
        self.attack_sound = attack_sound
        self.speed = speed
        self.resistance = resistance
        self.attack_radius = attack_radius
        self.notice_radius = notice_radius
        self.collide_inflate = collide_inflate

    def __repr__(self):
        msg = f"Enemy stats(health={self.health}/{self.health_max}, experience={self.experience}, " \
              f"damage={self.damage}, attack type={self.attack_type}, attack sound={self.attack_sound}, " \
              f"speed={self.speed}, resistance={self.resistance}, attack radius={self.attack_radius}, " \
              f"notice radius={self.notice_radius}"
        return msg

    def get_health_percent(self):
        return self.health / self.health_max
