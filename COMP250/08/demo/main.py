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

    the_map = map.Map((MAP_WIDTH, MAP_HEIGHT), tiles, TILE_SIZE, include_diagonals=True)
    fitness = calculate_fitness(the_map)
    fitness_history = [fitness]
    temperature = 1.0

    while True:
        #for tile_index in range(len(tiles)):
            new_tiles = tiles[:]
            tile_index = random.randrange(len(new_tiles))
            if new_tiles[tile_index] == ' ':
                new_tiles[tile_index] = '*'
            elif new_tiles[tile_index] == '*':
                new_tiles[tile_index] = ' '
            new_map = map.Map((MAP_WIDTH, MAP_HEIGHT), new_tiles, TILE_SIZE, include_diagonals=True)
            new_fitness = calculate_fitness(new_map)

            temperature *= 0.99
            if new_fitness > fitness or random.uniform(0, 1) < temperature:
                tiles = new_tiles
                the_map = new_map
                fitness = new_fitness
                
                print("Temperature:", temperature)

                print("Current fitness:", fitness)
                path = get_path(the_map)
                draw_map_and_path(screen, the_map, path)

                fitness_history.append(fitness)
                plt.clf()
                plt.plot(range(len(fitness_history)), fitness_history)
                plt.show(block=False)
                plt.pause(0.001)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return


if __name__ == '__main__':
    main()
