from code.timer import Timer
from code import utils
from code.data import spells


class MagicComponent:

    def __init__(self, create_attack_function, destroy_function):
        self.create_attack_function = create_attack_function
        self.destroy_function = destroy_function
        self.timer_attack = Timer(400)
        self.timer_switch_spell = Timer(200)
        self.spell_index = 0
        self.spell_image = self.load_spell_image()

    def update(self):
        self.timer_attack.update()
        self.timer_switch_spell.update()
        self.destroy_spell()

    def create_attack(self):
        if not self.is_attacking():
            self.timer_attack.launch()
            self.create_attack_function(self.spell_index)

    def destroy_spell(self):
        if self.timer_attack.is_ending:
            self.destroy_function()
            self.timer_attack.stop()

    def is_attacking(self):
        return self.timer_attack.is_running

    def is_switching_spell(self):
        return self.timer_switch_spell.is_running

    def switch_spell(self):
        if not self.is_attacking() and not self.is_switching_spell():
            self.timer_switch_spell.launch()
            self.spell_index = spells.get_next_index(self.spell_index)
            print(spells.get_name(self.spell_index))
            self.spell_image = self.load_spell_image()

    def load_spell_image(self):
        filename = spells.get_graphics(self.spell_index)
        return utils.load_image_and_rect(filename)
