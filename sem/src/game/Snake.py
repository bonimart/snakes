from pyglet.math import Vec2
from pyglet.graphics import Batch
from pyglet.shapes import Rectangle
from random import randrange
from conf.config import BLOCK_SIZE, SNAKE_COLOR

class InvaliMoveDirection(Exception):
    pass

class Snake:
    def __init__(self, shape: Vec2, batch: Batch):
        self.head = Snake.spawn(shape)
        self.body = []
        self.batch = batch
        self.shape = []
        self.add_rect()

    def spawn(shape: Vec2):
        return Vec2(randrange(0, shape.x), randrange(0, shape.y))
    
    def get_new_head(self, dir: str):
        new_head = self.head
        if dir == "u":
           new_head.y += 1
        elif dir == "d":
            new_head.y -= 1
        elif dir == "l":
            new_head.x -= 1
        elif dir == "r":
            new_head.x += 1
        else:
            raise InvaliMoveDirection(f"received invalid direction: {dir}, expected u, d, l or r.")
        return new_head

    def move(self, new_head: Vec2, ate: bool):
        self.body.insert(0, self.head)
        self.head = new_head
        # we don't want to add a new Rectangle unless we are extending the snake for the sake of performance
        if ate:
            self.add_rect()
            return

        self.body.pop()
        # reuse last rectangle so that we don't have to delete it
        last_rect = self.shape.pop()
        last_rect.x = self.head.x*BLOCK_SIZE
        last_rect.y = self.head.y*BLOCK_SIZE
        self.shape.insert(0, last_rect)
    
    def crashed(self):
        return self.head in self.body

    def add_rect(self):
        self.shape.insert(0, Rectangle(self.head.x*BLOCK_SIZE, self.head.y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, SNAKE_COLOR, batch=self.batch))
