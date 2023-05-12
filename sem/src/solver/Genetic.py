from pyglet.math import Vec2
from src.game.Snake import Snake
from src.game.Fruit import Fruit
import numpy as np
import random
from copy import copy, deepcopy
from conf.config import WIDTH, HEIGHT

POPULATION = 30
GENERATIONS = 100
MOVES = 5

CRASHED_PENALTY = 100
FRUIT_EATEN_BONUS = 5

MUTATION_PROBABILITY = 10e-2

TOURNAMENT_SELECTION_K = POPULATION//10

class GeneticSolver:
    crossover_methods = {

    }
    def __init__(self, get_neighbours, crossover_method=None):
        self.get_neighbours = get_neighbours
        self.heuristic = None
        self.moves = {
            0: lambda d: Vec2(-d.y, -d.x),
            1: lambda d: Vec2(d.y, d.x),
            2: lambda d: d
        }

    def fitness(self, genome, snake, dir):
        body = copy(snake.body)
        head = copy(snake.head)
        last_direction = dir
        crashed = False
        ate_fruit = False
        for gene in genome:
            last_direction = self.moves[gene](last_direction)
            new_head = head + last_direction
            new_head.x = new_head.x % WIDTH
            new_head.y = new_head.y % HEIGHT
            if new_head in body:
                crashed = True
                break
            if self.heuristic(new_head) == 0:
                ate_fruit = True
            body.insert(0, copy(head))
            body.pop()
            head = new_head

        
        return -(1-2*crashed)*self.heuristic(head) - CRASHED_PENALTY*crashed + ate_fruit*FRUIT_EATEN_BONUS

    def find_fruit(self, snake: Snake, fruit: Fruit, dir: Vec2):
        self.heuristic = lambda pos: min(WIDTH - abs(fruit.pos.x - pos.x), abs(fruit.pos.x - pos.x))  + min(HEIGHT - abs(fruit.pos.y - pos.y), abs(fruit.pos.y - pos.y))
        # https://courses.fit.cvut.cz/BI-ZUM/media/lectures/04-evolution-v5.0.pdf
        population = [(genome, self.fitness(genome, snake, dir)) for genome in self.generate_population()]
        for generation in range(GENERATIONS):
            new_population = []
            for i in range(POPULATION//2):
                p1 = self.tournament_selection(population)
                p2 = self.tournament_selection(population)
                o1, o2 = self.crossover(p1, p2)
                o1 = self.mutate(o1)
                o2 = self.mutate(o2)
                new_population.append((o1, self.fitness(o1, snake, dir)))
                new_population.append((o2, self.fitness(o2, snake, dir)))
            population = new_population

        final_genome = max(population, key=lambda x: x[1])
        print(final_genome[1])
        out = self.moves[final_genome[0][0]](dir)
        # print(out)
        return out



    def tournament_selection(self, population):
        random_selection = random.choices(population, k=TOURNAMENT_SELECTION_K)
        # return element with maximum fitness
        return max(random_selection, key=lambda x: x[1])[0]

    def generate_population(self):
        return [np.array([random.randint(0, 2) for i in range(MOVES)]) for j in range(POPULATION)]

    def crossover(self, a: np.array, b: np.array):
        x = np.array([random.choice([a[i], b[i]]) for i in range(len(a))])
        y = np.array([random.choice([a[i], b[i]]) for i in range(len(a))])
        return x, y
    
    def mutate(self, a: np.array):
        for i in range(MOVES):
            if random.random() < MUTATION_PROBABILITY:
                a[i] = 2 - a[i]
        return a
            
