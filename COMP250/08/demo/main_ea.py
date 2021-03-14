import pygame
import random
import matplotlib.pyplot as plt

import map
import pathfinding


TILE_SIZE = 75
MAP_WIDTH = 10
MAP_HEIGHT = 10


def draw_map_and_path(screen, the_map, path):
    screen.fill((255, 255, 255))

    the_map.draw(screen)
    for i in range(1, len(path)):
        pygame.draw.line(screen, (0, 0, 0), path[i - 1].pos, path[i].pos, 6)

    pygame.display.flip()


def get_path(the_map):
    path = pathfinding.a_star_search(the_map, None)
    if path is None:
        path = []

    #pathfinding.pull_string(the_map, path)

    return path


def calculate_fitness(the_map):
    path = get_path(the_map)
    return pathfinding.get_path_length(path)


def get_fittest(population):
    fittest_map = None
    fittest_fitness = 0

    for tiles in population:
        the_map = map.Map((MAP_WIDTH, MAP_HEIGHT), tiles, TILE_SIZE, include_diagonals=True)
        fitness = calculate_fitness(the_map)
        if fittest_map is None or fitness > fittest_fitness:
            fittest_map = tiles
            fittest_fitness = fitness

    return (fittest_map, fittest_fitness)


def tournament_select(population):
    TOURNAMENT_SIZE = 10
    tournament = [random.choice(population) for i in range(TOURNAMENT_SIZE)]
    (fittest_map, fittest_fitness) = get_fittest(tournament)
    return fittest_map


def mutate(tiles):
    tiles = tiles[:]

    for i in range(10):
        index = random.randrange(len(tiles))
        if tiles[index] == ' ':
            tiles[index] = '*'
        elif tiles[index] == '*':
            tiles[index] = ' '

    return tiles


def main():
    # Initialise PyGame
    pygame.init()
    clock = pygame.time.Clock()

    window_width = MAP_WIDTH * TILE_SIZE
    window_height = MAP_HEIGHT * TILE_SIZE
    window_size = (window_width, window_height)

    # Create the screen
    screen = pygame.display.set_mode(window_size)

    # Initial map
    tiles = [' '] * (MAP_WIDTH * MAP_HEIGHT)
    tiles[0] = 'S'
    tiles[-1] = 'G'

    POPULATION_SIZE = 20

    population = [tiles[:] for n in range(POPULATION_SIZE)]

    fitness_history = []

    # map.Map((MAP_WIDTH, MAP_HEIGHT), tiles, TILE_SIZE, include_diagonals=True)

    while True:
        new_population = []

        population_fitness = [
            (calculate_fitness(map.Map((MAP_WIDTH, MAP_HEIGHT), tiles, TILE_SIZE, include_diagonals=True)), tiles)
            for tiles in population
            ]
        population_fitness.sort()

        #elite = population_fitness[-1:]
        #for (fitness, tiles) in elite:
        #    new_population.append(tiles)

        while len(new_population) < POPULATION_SIZE:
            parent = tournament_select(population)
            child = mutate(parent)
            new_population.append(child)

        (fittest_tiles, fittest_fitness) = get_fittest(new_population)
        fittest_map = map.Map((MAP_WIDTH, MAP_HEIGHT), fittest_tiles, TILE_SIZE, include_diagonals=True)

        print("Current fitness:", fittest_fitness)
        path = get_path(fittest_map)
        draw_map_and_path(screen, fittest_map, path)

        fitness_history.append(fittest_fitness)
        plt.clf()
        plt.plot(range(len(fitness_history)), fitness_history)
        plt.show(block=False)
        plt.pause(0.001)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        population = new_population

if __name__ == '__main__':
    main()
