import pygame
import math


# Constants
black = (0, 0, 0)
white = (255, 255, 255)
blue = (100, 100, 255)
red = (255, 100, 100)
purple = (200, 0, 255)
green = (100, 255, 100)
gray = (200, 200, 200)


def euclidean_distance(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def manhattan_distance(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    return abs(x2-x1) + abs(y2-y1)


def max_component_distance(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    return min(abs(x2-x1), abs(y2-y1))


class Node:
    def __init__(self, x, y):
        self.pos = (x, y)
        self.edges = []
    
    def __lt__(self, other):
        return id(self) < id(other)

    def draw(self, screen, colour, radius):
        x, y = self.pos
        rect = pygame.Rect(x - radius, y - radius, 2*radius, 2*radius)
        pygame.draw.ellipse(screen, colour, rect)


class Edge:
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        self.length = euclidean_distance(from_node.pos, to_node.pos)


class Map:
    def __init__(self, size, tile_list, tile_size, include_diagonals):
        self.tile_size = tile_size
        self.tiles = {}
        self.width, self.height = size
        
        valid_tiles = ' *SG'
        tile_list = [t for t in tile_list if t in valid_tiles]

        x = 0
        y = 0
        for tile in tile_list:
            self.tiles[x, y] = tile
            x += 1
            if x >= self.width:
                x = 0
                y += 1
        

        self.nodes = {}
        self.start = None
        self.goal = None
        for (x, y), tile in self.tiles.items():
            if tile != '*':
                node = Node((x+0.5) * tile_size, (y+0.5) * tile_size)
                self.nodes[x, y] = node
                if tile == 'S':
                    self.start = node
                elif tile == 'G':
                    self.goal = node

        for (x, y), node in self.nodes.items():
            for nx in range(x-1, x+2):
                for ny in range(y-1, y+2):
                    if nx == x and ny == y:
                        continue
                    if not include_diagonals and (nx != x and ny != y):
                        continue
                    try:
                        neighbour = self.nodes[nx, ny]
                    except KeyError:
                        continue
                    if self.is_unobstructed(node.pos, neighbour.pos):
                        edge = Edge(node, neighbour)
                        node.edges.append(edge)

    def draw(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                try:
                    tile = self.tiles[x, y]
                except KeyError:
                    continue

                if tile == '*':
                    colour = black
                elif tile == 'S':
                    colour = purple
                elif tile == 'G':
                    colour = green
                else:
                    colour = white

                pygame.draw.rect(screen, colour, pygame.Rect(x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size))

        for node in self.nodes.values():
            for edge in node.edges:
                pygame.draw.line(screen, gray, edge.from_node.pos, edge.to_node.pos, 1)

        for node in self.nodes.values():
            node.draw(screen, blue, 3)

    def is_unobstructed(self, p1, p2):
        for x,y in self.get_supercover_line(p1, p2):
            if self.tiles[x, y] == '*':
                return False
        return True

    def get_supercover_line(self, p1, p2):
        # Ported from http://eugen.dedu.free.fr/projects/bresenham/
        x1,y1 = p1
        x2,y2 = p2
        x1 = int(x1 / self.tile_size)
        y1 = int(y1 / self.tile_size)
        x2 = int(x2 / self.tile_size)
        y2 = int(y2 / self.tile_size)
        y = y1
        x = x1
        dx = x2 - x1
        dy = y2 - y1

        yield (x1, y1)  # first point
        # NB the last point can't be here, because of its previous point (which has to be verified)

        if dy < 0:
            ystep = -1
            dy = -dy
        else:
            ystep = 1

        if dx < 0:
            xstep = -1
            dx = -dx
        else:
            xstep = 1

        ddy = 2 * dy  # work with double values for full precision
        ddx = 2 * dx

        if ddx >= ddy:  # first octant (0 <= slope <= 1)
            # compulsory initialization (even for errorprev, needed when dx==dy)
            errorprev = error = dx  # start in the middle of the square
            for i in range(dx):  # do not use the first point (already done)
                x += xstep
                error += ddy
                if error > ddx:  # increment y if AFTER the middle ( > )
                    y += ystep
                    error -= ddx
                    # three cases (octant == right->right-top for directions below):
                    if error + errorprev < ddx:  # bottom square also
                        yield (x, y - ystep)
                    elif error + errorprev > ddx:  # left square also
                        yield (x - xstep, y)
                    else:  # corner: bottom and left squares also
                        yield (x, y - ystep)
                        yield (x - xstep, y)
                yield (x, y)
                errorprev = error
        else:  # the same as above
            errorprev = error = dy
            for i in range(dy):
                y += ystep
                error += ddx
                if error > ddy:
                    x += xstep
                    error -= ddy
                    if error + errorprev < ddy:
                        yield (x - xstep, y)
                    elif error + errorprev > ddy:
                        yield (x, y - ystep)
                    else:
                        yield (x - xstep, y)
                        yield (x, y - ystep)
                yield (x, y)
                errorprev = error
