
import numpy as np
from VALID_MOVES import valid_moves
#Genrate with AI
def BFS(maze, start):
    rows, cols = maze.shape
    visited = np.full((rows, cols), False, dtype=bool)
    path_matrix = np.full((rows, cols), -1)

    queue = [(start, 0)]
    visited[start] = True
    path_matrix[start] = 0

    while queue:
        current_node, distance = queue.pop(0)

        for neighbor in valid_moves(maze, current_node):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, distance + 1))
                path_matrix[neighbor] = distance + 1

    return path_matrix
