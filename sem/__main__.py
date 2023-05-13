import pyglet
from pyglet.window import key
from pyglet.math import Vec2
from conf.config import WIN_WIDTH, WIN_HEIGHT
from src.game.Game import Game

solvers = {'0': 'Astar', '1': 'Genetic'}
heuristics = {'0': 'Manhattan', '1': 'Euclidean', '2': 'Manhattan++'}
if __name__ == "__main__":
    solver = None
    heuristic = None
    while solver not in ['0', '1', '2']:
        solver = input('''Choose a solver:
        0 - A*
        1 - Genetic
        2 - Play the game myself\n''')
    solver = solvers[solver] if solver in solvers else None

    if solver == 'Astar':
        while heuristic not in ['0', '1', '2']:
            heuristic = input('''Choose a heuristic:
        0 - Manhattan
        1 - Euclidean
        2 - Manhattan++\n''')
        heuristic = heuristics[heuristic]

window = pyglet.window.Window(WIN_WIDTH, WIN_HEIGHT, caption="Snakes, slow down")
game = Game(solver=solver, heuristic=heuristic)
@window.event
def on_draw():
    if game.over:
        pyglet.clock.unschedule(game.update)
        pyglet.clock.schedule_once(game.end_game, 1)
        game.over = False
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

