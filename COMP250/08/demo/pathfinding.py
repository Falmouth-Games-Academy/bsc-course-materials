import pygame
import heapq
import map

def reconstruct_path(node):
    path = []
    while node is not None:
        path.insert(0, node)
        node = node.came_from
    return path


def a_star_search(the_map, screen, visualise=False):
    for node in the_map.nodes.values():
        try:
            del node.g
            del node.came_from
        except AttributeError:
            pass

    queue = [(0 + map.euclidean_distance(the_map.start.pos, the_map.goal.pos), the_map.start)]
    the_map.start.g = 0
    the_map.start.came_from = None
    visited = set()

    while len(queue) > 0:
        (distance, current_node) = heapq.heappop(queue)
        visited.add(current_node)

        if current_node is the_map.goal:
            return reconstruct_path(current_node)

        for edge in current_node.edges:
            if edge.to_node not in visited:
                distance_so_far = current_node.g + edge.length

                try:
                    current_g = edge.to_node.g
                except AttributeError:
                    current_g = 1000000

                if distance_so_far < current_g:
                    edge.to_node.came_from = current_node
                    distance_to_goal = map.euclidean_distance(edge.to_node.pos, the_map.goal.pos)
                    edge.to_node.g = distance_so_far
                    heapq.heappush(queue, (distance_so_far + distance_to_goal, edge.to_node))

        if visualise:
            screen.fill((255, 255, 255))
            the_map.draw(screen)

            for distance, node in queue:
                node.draw(screen, (255, 0, 0), 6)

            current_node.draw(screen, (0, 255, 0), 12)

            pygame.display.flip()
            pygame.event.get()


def pull_string(the_map, path):
    i = 0
    while i+2 < len(path):
        if the_map.is_unobstructed(path[i].pos, path[i+2].pos):
            del path[i+1]
        else:
            i += 1


def get_path_length(path):
    length = 0
    for i in range(1, len(path)):
        length += map.euclidean_distance(path[i-1].pos, path[i].pos)
    return length
