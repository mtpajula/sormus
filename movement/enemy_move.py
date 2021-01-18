import pygame


class EnemyMove:

    def event(self, event, game_object):
        if event.type == pygame.KEYDOWN:
            game_object.y = game_object.y - 1
