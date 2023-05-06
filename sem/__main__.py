import pyglet
from pyglet.window import key
from conf.config import WIN_WIDTH, WIN_HEIGHT
from src.game.Game import Game
from random import choice

window = pyglet.window.Window(WIN_WIDTH, WIN_HEIGHT)
game = Game()

@window.event
def on_draw():
    window.clear()
    game.draw()

def update(dt):
    game.step()

pyglet.clock.schedule_interval(update, 1/10)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        game.dir = "u"
    elif symbol == key.DOWN:
        game.dir = "d"
    elif symbol == key.LEFT:
        game.dir = "l"
    elif symbol == key.RIGHT:
        game.dir = "r"


if __name__ == '__main__':
    pyglet.app.run()

