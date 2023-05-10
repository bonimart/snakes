from pyglet.math import Vec2
from src.game.Snake import Snake
from src.game.Fruit import Fruit
from queue import PriorityQueue
from math import sqrt

class AstarSolver:
    heuristics = {
        "Manhattan" : lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1]),
        "Euclidean" : lambda x, y: math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
    }
    def __init__(self, get_neighbours, heuristic="Manhattan"):
        self.get_neighbours = get_neighbours 
        self.heuristic = self.heuristics[heuristic]

    def reconstruct_path(self, prev, current):
        while current in prev and prev[current] in prev:
            current = prev[current]
        return Vec2(current[0] - prev[current][0], current[1] - prev[current][1]) 

    def find_fruit(self, snake: Snake, fruit: Fruit):
        toSee = PriorityQueue()
        prev = {}
        seen = set()
        taken = {tuple(body_part) for body_part in snake.body}
        
        goal = tuple(fruit.pos)
        tail = tuple(snake.body[-1]) if snake.body else tuple(snake.head)
        heuristic = lambda x: self.heuristic(x, goal)
        initial_state = tuple(snake.head)
        toSee.put((heuristic(initial_state), initial_state))
        distance_from_start = {initial_state: 0}
        # snake is going to eat the fruit anyway
        if goal in taken or goal == initial_state:
            neighbours = [tuple(neighbour) for neighbour in self.get_neighbours(Vec2(*initial_state)) if tuple(neighbour) not in taken]
            if not neighbours: return None
            neighbours.sort(key=heuristic)
            return Vec2(*(neighbours[0])) - snake.head

        while not toSee.empty():
            distance, current_state = toSee.get()
            if current_state in seen:
                continue

            if current_state == goal:
                return self.reconstruct_path(prev, current_state)

            seen.add(current_state)

            neighbours = [tuple(neighbour) for neighbour in self.get_neighbours(Vec2(*current_state)) if tuple(neighbour) not in taken] 
            for neighbour in neighbours:
                tentative_distance = distance_from_start[current_state] + 1
                if neighbour not in distance_from_start or tentative_distance < distance_from_start[neighbour]:
                    prev[neighbour] = current_state
                    distance_from_start[neighbour]  = tentative_distance
                    toSee.put((tentative_distance + heuristic(neighbour), neighbour))

        neighbours = [tuple(neighbour) for neighbour in self.get_neighbours(Vec2(*initial_state)) if tuple(neighbour) not in taken]
        if not neighbours:
            return None
        neighbours.sort(key=heuristic)
        return Vec2(*(neighbours[0])) - snake.head
