from pyglet.math import Vec2
from pyglet.graphics import Batch
from src.game.Map import Map
from src.game.Fruit import Fruit
from src.game.Snake import Snake
from conf.config import HEIGHT, WIDTH, BLOCK_SIZE, TEXT_COLOR, FONT
import pyglet
from pyglet.text import Label

class Game:
    shape = Vec2(WIDTH, HEIGHT)

    def __init__(self, solver=None):
        self.batch = Batch()
        self.map = Map(Game.shape, self.batch)
        self.snake = Snake(Game.shape, self.batch)
        self.fruit = Fruit(Game.shape, self.batch)
        self.dir = "u"
        self.score = 0
        self.over = False
        self.game_over_text = None

    def draw(self):
        self.batch.draw()

    def step(self):
        new_head = self.snake.get_new_head(self.dir)
        self.adjust_bounds(new_head)
        
        if self.snake.crashed(new_head):
            self.over = True
            pyglet.clock.unschedule(self.update)
            pyglet.clock.schedule_once(self.end_game, 1)
        
        ate = self.ate(new_head)
        self.snake.move(new_head, ate)
        
        if ate:
            self.fruit.respawn()
            self.score += 1

    def ate(self, new_head):
        return self.fruit.pos == new_head or self.fruit.pos == self.snake.head or self.fruit.pos in self.snake.body

    def adjust_bounds(self, head):
        head.x %= self.shape.x
        head.y %= self.shape.y

    def change_dir(self, dir: str):
        if (self.dir == "u" and dir == "d") or (self.dir == "d" and dir == "u") or (self.dir == "l" and dir == "r") or (self.dir == "r" and dir == "l"):
            return
        self.dir = dir

    def update(self, dt):
        self.step()

    def end_game(self, dt):
        self.snake.die()
        self.fruit.rot()
        self.game_over_text = Label(f"Game over, score: {self.score}",\
                                    font_name=FONT, font_size=BLOCK_SIZE,\
                                    x=WIDTH*BLOCK_SIZE//2, y=HEIGHT*BLOCK_SIZE//2,\
                                    anchor_x='center', anchor_y='center',\
                                    batch=self.batch)


