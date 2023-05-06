from pyglet.math import Vec2
from pyglet.graphics import Batch
from src.game.Map import Map
from src.game.Fruit import Fruit
from src.game.Snake import Snake
from conf.config import HEIGHT, WIDTH

class Game:
    shape = Vec2(WIDTH, HEIGHT)

    def __init__(self, solver=None):
        self.batch = Batch()
        self.map = Map(Game.shape, self.batch)
        self.snake = Snake(Game.shape, self.batch)
        self.fruit = Fruit(Game.shape, self.batch)
        self.dir = "u"
        self.score = 0

    def draw(self):
        self.batch.draw()

    def step(self):
        new_head = self.snake.get_new_head(self.dir)
        self.adjust_bounds(new_head)
        ate = self.ate(new_head)
        self.snake.move(new_head, ate)
        
        if ate:
            self.fruit.respawn()
            self.score += 1

    def ate(self, new_head):
        return self.fruit.pos == new_head or self.fruit.pos == self.snake.head or self.fruit.pos in self.snake.body

    def adjust_bounds(self, head):
        head.x = max(0, head.x)
        head.x = min(head.x, self.shape.x - 1)
        head.y = max(0, head.y)
        head.y = min(head.y, self.shape.y - 1)

