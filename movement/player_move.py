import pygame


class PlayerMove:

    def event(self, event, game_object):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game_object.y = game_object.y - 1
            elif event.key == pygame.K_DOWN:
                game_object.y = game_object.y + 1
            elif event.key == pygame.K_LEFT:
                game_object.x = game_object.x - 1
            elif event.key == pygame.K_RIGHT:
                game_object.x = game_object.x + 1
