from pyglet.math import Vec2
from pyglet.graphics import Batch
from src.game.Map import Map
from src.game.Fruit import Fruit
from src.game.Snake import Snake
from src.solver.Astar import Astar
from conf.config import HEIGHT, WIDTH, BLOCK_SIZE, TEXT_COLOR, FONT
import pyglet
from pyglet.text import Label
from datetime import datetime

class Game:
    shape = Vec2(WIDTH, HEIGHT)
    solvers = {
        "Astar" : Astar
    }

    def __init__(self, solver: str):
        self.batch = Batch()
        self.map = Map(Game.shape, self.batch)
        self.snake = Snake(Game.shape, self.batch)
        self.fruit = Fruit(Game.shape, self.batch)

        self.dir = Vec2(0, 1)
        self.last_dir = Vec2(0, 1)

        self.score = 0
        self.over = False
        self.game_over_text = None

        self.solver= Game.solvers[solver](self.map.get_neighbours) if solver in Game.solvers else None
        self.solver_plan = self.solver.find_fruit_ex(self.snake, self.fruit) if self.solver else None

    def draw(self):
        self.batch.draw()

    def step(self):

        # input from player
        if not self.solver:
            # synchronizes adjusting of snake direction
            self.change_dir(self.last_dir)
            self.last_dir = self.dir
        else:
            self.dir = self.solver_plan if self.solver_plan else self.dir

        new_head = self.snake.get_new_head(self.dir)
        self.adjust_bounds(new_head)

        if self.snake.crashed(new_head):
            print("Snake crashed")
            print(f"New head: {new_head.x}, {new_head.y}")
            print(f"Old head: {self.snake.head.x}, {self.snake.head.y}")
            print(f"Tail: {self.snake.body}")
            self.over = True
            pyglet.clock.unschedule(self.update)
            pyglet.clock.schedule_once(self.end_game, 1)
        
        ate = self.ate(new_head)
        self.snake.move(new_head, ate)
        
        if ate:
            self.fruit.respawn()
            self.score += 1

        if self.solver:
            self.solver_plan = self.solver.find_fruit_ex(self.snake, self.fruit) if self.solver else None

    def ate(self, new_head):
        return self.fruit.pos == new_head or self.fruit.pos == self.snake.head or self.fruit.pos in self.snake.body

    def adjust_bounds(self, head):
        head.x %= self.shape.x
        head.y %= self.shape.y

    def change_dir(self, dir: str):
        if self.dir.dot(dir) == -1:
            self.dir = dir

    def update(self, dt):
        self.step()

    def end_game(self, dt):
        # https://stackoverflow.com/questions/4986662/taking-a-screenshot-with-pyglet-fixd
        pyglet.image.get_buffer_manager().get_color_buffer().save(f'sem/screenshots/{datetime.now()}.png')
        self.snake.die()
        self.fruit.rot()
        txt = f'Game over, score: {self.score}'
        self.game_over_text = Label(txt, font_name=FONT, font_size=BLOCK_SIZE//2,\
                                    x=WIDTH*BLOCK_SIZE//2, y=HEIGHT*BLOCK_SIZE//2,\
                                    anchor_x='center', anchor_y='center',\
                                    color=TEXT_COLOR, batch=self.batch)


