from pyglet.math import Vec2
from src.game.Snake import Snake
from src.game.Fruit import Fruit
from queue import PriorityQueue

class Astar:
    def __init__(self, get_neighbours):
        self.get_neighbours = get_neighbours 

    def reconstruct_path_ex(self, prev, current):
        while current in prev and prev[current] in prev:
            current = prev[current]
        return Vec2(current[0] - prev[current][0], current[1] - prev[current][1]) 

    def find_fruit_ex(self, snake: Snake, fruit: Fruit):
        toSee = PriorityQueue()
        prev = {}
        seen = set()
        taken = {tuple(body_part) for body_part in snake.body}
        
        goal = tuple(fruit.pos)
        heuristic = lambda x: abs(goal[0] - x[0]) + abs(goal[1] - x[1]) 
        initial_state = tuple(snake.head)
        toSee.put((heuristic(initial_state), initial_state))
        distance_from_start = {initial_state: 0}
        # snake is going to eat the fruit anyway
        if goal in taken or goal == initial_state:
            neighbours = [neighbour for neighbour in self.get_neighbours(Vec2(*initial_state)) if tuple(neighbour) not in taken] 
            return neighbours[0] - snake.head

        while not toSee.empty():
            distance, current_state = toSee.get()
            if current_state in seen:
                continue

            if current_state == goal:
                return self.reconstruct_path_ex(prev, current_state)

            seen.add(current_state)

            neighbours = [tuple(neighbour) for neighbour in self.get_neighbours(Vec2(*current_state)) if tuple(neighbour) not in taken] 
            for neighbour in neighbours:
                tentative_distance = distance_from_start[current_state] + 1
                if neighbour not in distance_from_start or tentative_distance < distance_from_start[neighbour]:
                    prev[neighbour] = current_state
                    distance_from_start[neighbour]  = tentative_distance
                    toSee.put((tentative_distance + heuristic(neighbour), neighbour))

        
