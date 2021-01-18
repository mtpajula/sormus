import pygame

from movement.enemy_move import EnemyMove
from movement.player_move import PlayerMove
from stage import Stage
from stuff.game_object import GameObject


def main():
    stage = Stage(800)
    stage.set_background_image('bg.bmp')
    stage.init()

    obj = GameObject()
    obj.set_position(10, 10)
    obj.set_action(PlayerMove())
    stage.set_object(obj)

    for num in range(1, 6):
        obj = GameObject()
        obj.set_position(10 * num, 80)
        obj.set_action(EnemyMove())
        stage.set_object(obj)

    stage.draw_objects()

    while True:

        for event in pygame.event.get():
            stage.clear_objects()

            stage.on_event(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            stage.draw_objects()

        stage.step()
        pygame.display.flip()


if __name__ == '__main__':
    main()
