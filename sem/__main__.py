import pyglet
from pyglet.window import key
from pyglet.math import Vec2
from conf.config import WIN_WIDTH, WIN_HEIGHT
from src.game.Game import Game

window = pyglet.window.Window(WIN_WIDTH, WIN_HEIGHT, caption="Snakes, slow down")
game = Game(solver="Genetic")

@window.event
def on_draw():
    window.clear()
    game.draw()


pyglet.clock.schedule_interval(game.update, 1/10)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        game.dir = Vec2(0, 1)
    elif symbol == key.DOWN:
        game.dir = Vec2(0, -1)
    elif symbol == key.LEFT:
        game.dir = Vec2(-1, 0)
    elif symbol == key.RIGHT:
        game.dir = Vec2(1, 0)


if __name__ == '__main__':
    pyglet.app.run()

