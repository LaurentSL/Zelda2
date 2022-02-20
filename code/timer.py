import pygame.time


class Timer:

    def __init__(self, cooldown = 100):
        self.cooldown = cooldown
        self.time = None
        self.is_running = False
        self.is_ending = False

    def launch(self, cooldown = -1):
        if cooldown > 0:
            self.cooldown = cooldown
        self.time = pygame.time.get_ticks()
        self.is_running = True
        self.is_ending = False

    def update(self):
        if self.is_running:
            current_time = pygame.time.get_ticks()
            if current_time - self.time >= self.cooldown:
                self.is_running = False
                self.is_ending = True

    def stop(self):
        self.is_ending = False

