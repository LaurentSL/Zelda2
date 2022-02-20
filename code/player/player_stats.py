class Stats:

    def __init__(self, health: int, energy: int, attack: int, magic: int, speed: int):
        self.health = health
        self.health_max = self.health
        self.energy = energy
        self.energy_max = self.energy
        self.attack = attack
        self.attack_max = self.attack
        self.magic = magic
        self.magic_max = self.magic
        self.speed = speed
        self.speed_max = self.speed
        self.experience = 0

    def __repr__(self):
        msg = f"stats(health={self.health}/{self.health_max}, energy={self.energy}/{self.energy_max}, " \
              f"attack={self.attack}/{self.attack_max}, magic={self.magic}/{self.magic_max}, " \
              f"speed={self.speed}/{self.speed_max}, experience={self.experience}"
        return msg

    def get_health_percent(self):
        return self.health / self.health_max

    def get_energy_percent(self):
        return self.energy / self.energy_max
