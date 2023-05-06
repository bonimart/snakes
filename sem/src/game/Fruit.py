from pyglet.math import Vec2
from random import randint

class Fruit:
    def __init__(self, shape):
        self.pos = Fruit.spawn(shape)
    
    def spawn(shape: Vec2):
        """
        Return a new, random position given the max x and y coordinates
        """
        return Vec2(0, randint(shape.x), randint(0, shape.y))

