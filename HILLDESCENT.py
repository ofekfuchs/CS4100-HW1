import sys
import numpy as np
from BFS import BFS
from ASTAR import ASTAR
from copy import deepcopy

def energyfunction(maze, start, goal):
    # find the short path
    astar_path = ASTAR(maze, start, goal)
    # BFS to find unreachable cells
    bfs_matrix = BFS(maze, start)
    # Count the number of unreachable cells
    unreachable_cells = np.count_nonzero(bfs_matrix == -1)
    # Return the sum of the shortest path length and the number of unreachable cells
    return len(astar_path[1]) - 1 + unreachable_cells

#Genrate with AI
def HILLDESCENT(maze, start_cell, goal_state, iterations):
	best_maze = maze.copy()
	best_energy = energyfunction(best_maze, start_cell, goal_state)

	for i in range(iterations):
		current_maze = deepcopy(best_maze)

		# Pick a random non-goal state
		row, col = goal_state
		while (row, col) == goal_state:
			row = np.random.randint(maze.shape[0])
			col = np.random.randint(maze.shape[1])

		# Change its jump value to a different random value
		current_maze[row, col] = np.random.randint(1, maze.shape[1])

		# Calculate energy for the current maze
		current_energy = energyfunction(current_maze, start_cell, goal_state)

		# If the energy decreases, retain the updated value
		if current_energy < best_energy:
			best_maze = current_maze
			best_energy = current_energy

	return best_maze, best_energy

def HILLDESCENT_RANDOM_RESTART(maze, start_cell, goal_state, iterations, num_searches):
    best_maze = maze.copy()
    best_energy = float('inf')  # Initialize with positive infinity initially

    for i in range(num_searches):
        current_maze, current_energy = HILLDESCENT(maze, start_cell, goal_state, iterations)

        # If the current energy is better than the best so far, update the best solution
        if current_energy < best_energy:
            best_maze = current_maze
            best_energy = current_energy

    return best_maze, best_energy

def HILLDESCENT_RANDOM_UPHILL(maze, start_cell, goal_state, iterations, probability):
    best_maze = maze.copy()
    best_energy = float('inf')  # Initialize with positive infinity initially

    for _ in range(iterations):
        current_maze = deepcopy(maze)
        current_energy = energyfunction(current_maze, start_cell, goal_state)

        # Choose a random non-goal state
        row, col = np.random.choice(range(current_maze.shape[0])), np.random.choice(range(current_maze.shape[1]))
        while (row, col) == goal_state:
            row, col = np.random.choice(range(current_maze.shape[0])), np.random.choice(range(current_maze.shape[1]))
        current_maze[row, col] = np.random.randint(1, current_maze[row, col] + 1)

        new_energy = energyfunction(current_maze, start_cell, goal_state)

        # Retain the change if the new state decreases the energy function or with a probability
        if new_energy < current_energy or np.random.rand() < probability:
            current_energy = new_energy

        # Update the best solution if the current energy is better
        if current_energy < best_energy:
            best_maze = current_maze
            best_energy = current_energy

    return best_maze, best_energy
