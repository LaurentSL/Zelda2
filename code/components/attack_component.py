from code import settings
from code import utils
from code.data import weapons
from code.timer import Timer


class AttackComponent:

    def __init__(self, create_weapon_function, destroy_weapon_function):
        self.create_weapon_function = create_weapon_function
        self.destroy_weapon_function = destroy_weapon_function
        self.timer_attack = Timer(400)
        self.timer_switch_weapon = Timer(200)
        self.weapon_index = 0
        self.weapon_image = self.load_weapon_image()

    def update(self):
        self.timer_attack.update()
        self.timer_switch_weapon.update()
        self.destroy_weapon()

    def attack(self):
        if not self.is_attacking():
            self.timer_attack.launch()
            self.create_weapon_function(self.weapon_index)

    def destroy_weapon(self):
        if self.timer_attack.is_ending:
            self.destroy_weapon_function()
            self.timer_attack.stop()

    def is_attacking(self):
        return self.timer_attack.is_running

    def is_switching_weapon(self):
        return self.timer_switch_weapon.is_running

    def switch_weapon(self):
        if not self.is_attacking() and not self.is_switching_weapon():
            self.timer_switch_weapon.launch()
            self.weapon_index = weapons.get_next_index(self.weapon_index)
            self.weapon_image = self.load_weapon_image()

    def load_weapon_image(self):
        filename = weapons.get_graphics(self.weapon_index) + settings.UI_WEAPON_IMAGE_FILENAME
        return utils.load_image_and_rect(filename)
