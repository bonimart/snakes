from pyglet.math import Vec2
from pyglet.graphics import Batch
from src.game.Map import Map
from src.game.Fruit import Fruit
from conf.config import HEIGHT, WIDTH

class Game:
    shape = Vec2(WIDTH, HEIGHT)

    def __init__(self, solver=None):
        self.batch = Batch()
        self.map = Map(Game.shape, self.batch)
        self.fruit = Fruit(Game.shape, self.batch)
        self.score = 0

    def draw(self):
        self.batch.draw()

