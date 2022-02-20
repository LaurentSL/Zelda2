import pygame

from code import timer
from code import utils
from code.animation import Animation
from code.game_objects.game_object import GameObject


class AnimationComponent(GameObject):

    def __init__(self, groups, path, lst_animations_names, collide_inflate, position, notice_radius=0, attack_radius=0):
        super().__init__(groups, position)
        self.animations = {}
        self.animation = None
        self._import_assets(path, lst_animations_names)
        self.animation_name = ""
        self.switch_animation(self._get_first_animation_name())
        x, y = collide_inflate
        self.collision_box = self.rect.inflate(x, y)
        self.notice_radius = notice_radius
        self.attack_radius = attack_radius
        self.position = position

    def __repr__(self):
        return f"AnimationComponent - name: {self.animation_name}, animations: {self._get_animations_names()}"

    def _import_assets(self, path, lst_animations_names):
        self.animations = {}
        for name in lst_animations_names:
            self.animations[name] = Animation(path, name)

    def update(self):
        super().update()
        self.animation.update()
        self._update_image_and_rect()

    def switch_animation(self, animation_name):
        if animation_name == self.animation_name:
            return
        self.animation_name = animation_name
        self.animation = self.animations[self.animation_name]
        self.animation.reset()
        self._update_image_and_rect()

    def _update_image_and_rect(self):
        position = self.rect.topleft if self.rect else (0, 0)
        self.image, self.rect = self.animation.get_image_and_rect()
        self.rect.topleft = position

    def _get_animations_names(self):
        return list(self.animations.keys())

    def _get_first_animation_name(self):
        animations_names = self._get_animations_names()
        first_animation_name = animations_names[0]
        return first_animation_name

    @property
    def is_ending(self):
        return self.animation.is_ending
