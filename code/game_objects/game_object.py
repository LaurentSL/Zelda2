import pygame

from code import utils


class GameObject(pygame.sprite.Sprite):

    def __init__(self,
                 groups: pygame.sprite.AbstractGroup = [],
                 position: pygame.math.Vector2 = pygame.math.Vector2(0, 0),
                 image_name: str = ""
                 ) -> None:
        super().__init__(groups)
        self.image: pygame.Surface = None
        self.rect: pygame.Rect = None
        if image_name is not None and image_name != "":
            self.load_image_and_rect(image_name)
            self.position = position

    def load_image_and_rect(self, image_name):
        self.image, self.rect = utils.load_image_and_rect(image_name)

    def update(self) -> None:
        pass

    @property
    def position(self):
        return self.rect.topleft

    @position.setter
    def position(self, value: pygame.Vector2):
        if self.rect is not None:
            self.rect.topleft = value
