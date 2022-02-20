import pygame


class MovementComponent:
    UP = 'up'
    DOWN = 'down'
    RIGHT = 'right'
    LEFT = 'left'

    def __init__(self, obstacle_sprites, game_object, collision_box, speed):
        self._obstacles_sprites = obstacle_sprites
        self.game_object = game_object
        self._collision_box = collision_box
        self.direction = pygame.math.Vector2()
        self._speed = speed
        self._speed_reference = speed
        self.position = self.game_object.position

    def __repr__(self):
        return f"MovementComponent: direction={self.direction}, speed={self._speed}/{self._speed_reference}, " \
               f"position: {self.position}"

    def update(self):
        self._move()

    def move_to(self, direction):
        if direction.magnitude() == 0:
            return
        self.direction = direction.normalize()
        self._move()

    def _move(self):
        if self._speed == 0:
            return
        self.move_horizontal()
        self.move_vertical()
        self.game_object.position = self.position

    @property
    def position(self):
        return self._collision_box.topleft

    @position.setter
    def position(self, value):
        self._collision_box.topleft = value

    def move_horizontal(self):
        self._collision_box.x += self.direction.x * self._speed
        self.collision_horizontal()

    def move_vertical(self):
        self._collision_box.y += self.direction.y * self._speed
        self.collision_vertical()

    def collision_horizontal(self):
        if self.direction.x == 0:
            return
        for sprite in self._obstacles_sprites:
            if sprite.collision_box.colliderect(self._collision_box):
                if self.direction.x > 0:  # go to the right
                    self._collision_box.right = sprite.collision_box.left
                else:  # go to the left
                    self._collision_box.left = sprite.collision_box.right

    def collision_vertical(self):
        if self.direction.y == 0:
            return
        for sprite in self._obstacles_sprites:
            if sprite.collision_box.colliderect(self._collision_box):
                if self.direction.y > 0:  # go to the bottom
                    self._collision_box.bottom = sprite.collision_box.top
                else:  # go to the top
                    self._collision_box.top = sprite.collision_box.bottom

    def get_direction_name(self):
        if self.direction.x < 0:
            return self.LEFT
        elif self.direction.x > 0:
            return self.RIGHT
        elif self.direction.y < 0:
            return self.UP
        else:
            return self.DOWN

    def stop(self):
        self._speed = 0

    def can_move(self):
        self._speed = self._speed_reference

    def set_normalized_direction(self, x, y):
        if x == y == 0:
            self.stop()
        else:
            self.direction.x = x
            self.direction.y = y
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()

    def is_moving(self):
        return self._speed != 0
