from code import timer
from code import utils


class Animation:

    def __init__(self, path, name):
        self.timer = timer.Timer(100)
        self.animation_images_and_rect = utils.import_all_images_and_rect_from_folder(path + name)
        self.animation_index = 0
        self.is_ending = False

    def update(self):
        self.timer.update()

    def reset(self):
        self.animation_index = 0

    def get_image_and_rect(self):
        if not self._is_waiting_next_animation_frame():
            self._get_next_frame_index()
            self.timer.launch()
        return self.animation_images_and_rect[self.animation_index]

    def _get_next_frame_index(self):
        self.animation_index += 1
        self.is_ending = False
        if self.animation_index >= len(self.animation_images_and_rect):
            self.animation_index = 0
            self.is_ending = True

    def _is_waiting_next_animation_frame(self):
        return self.timer.is_running

