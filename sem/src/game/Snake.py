from pyglet.math import Vec2
from pyglet.graphics import Batch
from pyglet.shapes import Rectangle
from random import randrange
from copy import copy
import numpy as np
from conf.config import BLOCK_SIZE, SNAKE_COLOR_LIGHT, SNAKE_COLOR_DARK

class Snake:
    def __init__(self, shape: Vec2, batch: Batch):
        self.head = Snake.spawn(shape)
        # self.body = np.array([Vec2(0, 0) for i in range(shape.x*shape.y - 1)])
        # self.tail_length = 0
        self.body = []
        # self.body = []
        self.batch = batch
        self.shape = []
        self.add_rect()

    def spawn(shape: Vec2):
        return Vec2(randrange(0, shape.x), randrange(0, shape.y))
    
    def get_new_head(self, dir: Vec2):
        new_head = self.head + dir
        return new_head

    def move(self, new_head: Vec2, ate: bool):
        # old_len = len(self.body)
        # self.body = np.insert(self.body[:-1], 0, self.head, axis=0)
        # assert len(self.body) == old_len
        self.body.insert(0, copy(self.head))
        # self.body.insert(0, deepcopy(self.head))
        self.head = new_head
        # we don't want to add a new Rectangle unless we are extending the snake for the sake of performance
        if ate:
            self.add_rect()
            self.update_rect_gradient()
            return

        self.body.pop()
        # reuse last rectangle so that we don't have to delete it
        last_rect = self.shape.pop()
        last_rect.x = self.head.x*BLOCK_SIZE
        last_rect.y = self.head.y*BLOCK_SIZE
        self.shape.insert(0, last_rect)
        self.update_rect_gradient()

    def crashed(self, new_head):
        # print(new_head)
        # body = [Vec2(*body_part) for body_part in self.body[:self.tail_length]]
        return new_head in self.body 

    def add_rect(self):
        self.shape.insert(0, Rectangle(self.head.x*BLOCK_SIZE, self.head.y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, SNAKE_COLOR_LIGHT, batch=self.batch))

    def die(self):
        for rect in self.shape:
            rect.delete()

    def update_rect_gradient(self):
        l = len(self.shape)
        for i, rect in enumerate(self.shape):
            i_dark, i_light = i/l, (l-i)/l
            light = [int(i_light*col) for col in SNAKE_COLOR_LIGHT]
            dark = [int(i_dark*col) for col in SNAKE_COLOR_DARK]
            rect.color = tuple([dark[i] + light[i] for i in range(3)])
            # for j in range(3):
                # rect.color[j] += dark[j] + light[j] - rect.color[j]

