import heapq
import numpy as np
from VALID_MOVES import valid_moves
def H_score(node, goal, n):
    # Manhattan distance between current node and goal state
    manhattan_distance = abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    # H score is the Manhattan distance divided by the largest possible jump value
    heuristic = manhattan_distance / (n-1)
    return heuristic
#Genrate with AI
def ASTAR(maze, start, goal):
    # Priority queue for A* search
    open_set = [(0, start)]  # (f_score, node)
    closed_set = set()

    # Data structures to store path information
    g_scores = {start: 0}
    came_from = {start: None}

    while open_set:
        _, current_node = heapq.heappop(open_set)

        if current_node == goal:
            # Reconstruct the path
            path = [current_node]
            while came_from[current_node] is not None:
                current_node = came_from[current_node]
                path.append(current_node)
            return len(path) - 1, path[::-1]

        closed_set.add(current_node)

        for neighbor in valid_moves(maze, current_node):
            if neighbor in closed_set:
                continue

            tentative_g_score = g_scores[current_node] + maze[current_node[0], current_node[1]]

            if neighbor not in [node[1] for node in open_set] or tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                f_score = tentative_g_score + H_score(neighbor, goal, maze.shape[0])
                heapq.heappush(open_set, (f_score, neighbor))
                came_from[neighbor] = current_node
    return 0, []  # Return 0 length and an empty path if no path is found
