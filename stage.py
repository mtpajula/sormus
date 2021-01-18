from terrain.grid import Grid
from PIL import Image
import pygame


class Stage:

    def __init__(self, size):
        pygame.init()
        self.grid = Grid(pygame.display.set_mode((size, size)))
        self.grid.set_screen_size(size)
        self.game_objects = []

    def set_background_image(self, image_path):
        bg_image = Image.open(image_path)
        bg_pix = bg_image.load()
        self.grid.set_background(bg_pix)

    def set_object(self, game_object):
        self.game_objects.append(game_object)

    def init(self):
        self.grid.draw_background()

    def clear_objects(self):
        for game_object in self.game_objects:
            self.grid.clear_object(game_object)

    def draw_objects(self):
        for game_object in self.game_objects:
            self.grid.draw_object(game_object)

    def on_event(self, event):
        for game_object in self.game_objects:
            game_object.on_event(event)

    def step(self):
        pass

