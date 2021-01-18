from stuff.game_pixel import GamePixel


class GameObject:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.structure = [
            GamePixel(1, 0, (255, 255, 255)),
            GamePixel(0, 1, (100, 0, 0)),
            GamePixel(1, 1, (100, 0, 0)),
            GamePixel(2, 1, (100, 0, 0)),
            GamePixel(1, 2, (100, 0, 0)),
            GamePixel(0, 3, (100, 0, 0)),
            GamePixel(1, 3, (100, 0, 0)),
            GamePixel(2, 3, (100, 0, 0)),
            GamePixel(0, 4, (100, 0, 0)),
            GamePixel(2, 4, (100, 0, 0)),
        ]
        self.actions = []

    def set_action(self, action):
        self.actions.append(action)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def on_event(self, event):
        for action in self.actions:
            action.event(event, self)

