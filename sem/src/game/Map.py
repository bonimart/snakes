from pyglet.math import Vec2
from pyglet.graphics import Batch
from pyglet.shapes import Rectangle
from conf.config import BACKGROUND_COLOR, BLOCK_SIZE, BLOCK_SIZE

class Map:
    def __init__(self, shape: Vec2, batch: Batch):
        self.shape = shape
        self.sprite = Rectangle(0, 0, BLOCK_SIZE*shape.x, BLOCK_SIZE*shape.y, BACKGROUND_COLOR, batch=batch)
        
