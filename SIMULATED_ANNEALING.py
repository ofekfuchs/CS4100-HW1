
import sys
import numpy as np
from BFS import BFS
from ASTAR import ASTAR
from HILLDESCENT import energyfunction
import math
import random
def SIMULATED_ANNEALING(maze, start_cell, goal_state, iterations, T, decay):
    best_maze = maze.copy()
    best_energy = energyfunction(maze, start_cell, goal_state)

    current_maze = maze.copy()
    current_energy = best_energy

    for _ in range(iterations):
        new_energy = energyfunction(current_maze, start_cell, goal_state)

        # If the new configuration is better, accept the change
        if new_energy < current_energy:
            current_energy = new_energy
            # Update the best solution if needed
            if new_energy < best_energy:
                best_energy = new_energy
                best_maze = current_maze.copy()
        else:
            # Accept the change with a probability based on the temperature
            probability = math.exp((current_energy - new_energy) / T)
            if random.random() < probability:
                current_energy = new_energy

        # Decrease the temperature
        T *= decay

    return best_maze, best_energy

