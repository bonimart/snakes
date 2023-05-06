import pyglet
from pyglet.window import key
from conf.config import WIN_WIDTH, WIN_HEIGHT
from src.game.Game import Game

window = pyglet.window.Window(WIN_WIDTH, WIN_HEIGHT)
game = Game()

@window.event
def on_draw():
    window.clear()
    game.draw()

# @window.event
# def on_key_press(symbol, modifiers):
#     if symbol == key.SPACE:
#         game.fruit.respawn()

if __name__ == '__main__':
    pyglet.app.run()

