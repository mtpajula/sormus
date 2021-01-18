
import pygame


class Grid:

    def __init__(self, screen):
        self.blocks = 100
        self.screen_size = None
        self.screen = screen
        self.block_size = 0
        self.background = None

    def set_screen_size(self, screen_size):
        self.screen_size = screen_size
        self.reset_block_size()

    def set_background(self, background):
        self.background = background

    def reset_block_size(self):
        self.block_size = round(self.screen_size / self.blocks)

    def screen_pos(self, xy):
        return xy * self.block_size

    def draw_pixel(self, x, y, color, border=True):
        rect = pygame.Rect(self.screen_pos(x), self.screen_pos(y),
                           self.block_size, self.block_size)

        if border:
            pygame.draw.rect(self.screen, color, rect, 1)
        else:
            pygame.draw.rect(self.screen, color, rect)

    def draw_grid(self):
        for x in range(self.blocks):
            for y in range(self.blocks):
                self.draw_pixel(x, y, (50, 50, 50), True)

    def draw_background(self):
        for x in range(self.blocks):
            for y in range(self.blocks):
                self.draw_pixel(x, y, self.background[x, y], False)

    def clear_object(self, game_object):
        for pixel in game_object.structure:
            x = pixel.x + game_object.x
            y = pixel.y + game_object.y
            self.draw_pixel(x, y, self.background[x, y], False)

    def draw_object(self, game_object):
        for pixel in game_object.structure:
            x = pixel.x + game_object.x
            y = pixel.y + game_object.y
            self.draw_pixel(x, y, pixel.color, False)
