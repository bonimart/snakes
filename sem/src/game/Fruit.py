from pyglet.math import Vec2
from pyglet.graphics import Batch
from pyglet.shapes import Rectangle
from random import randrange
from conf.config import BLOCK_SIZE, FRUIT_COLOR

class Fruit:
    def __init__(self, shape: Vec2, batch: Batch):
        self.max_x = shape.x
        self.max_y = shape.y
        self.pos = None
        self.sprite = Rectangle(0, 0, BLOCK_SIZE, BLOCK_SIZE, FRUIT_COLOR, batch=batch)
        self.respawn()
    
    def respawn(self):
        """
        Respawn the fruit on a new position
        """
        self.pos = Vec2(randrange(0, self.max_x), randrange(0, self.max_y))
        self.sprite.x = self.pos.x*BLOCK_SIZE
        self.sprite.y = self.pos.y*BLOCK_SIZE
        # print(f"respawning fruit on position {self.pos.x}, {self.pos.y}")

    def rot(self):
        self.sprite.delete()

