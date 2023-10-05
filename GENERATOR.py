
from BFS import BFS
import numpy as np


def generator(k):
	#intial the board
	init_board = np.random.randint(1, k, (k, k))
	#Create random for start call and goal state
	start_cell = (np.random.randint(k), np.random.randint(k))
	goal_state = (np.random.randint(k), np.random.randint(k))
	#Check if the start call and the goal state is diffrent
	while start_cell == goal_state:
		goal_state = (np.random.randint(k), np.random.randint(k))
	#the maze for the goal state to 0.
	init_board[goal_state[0]][goal_state[1]] = 0

	return init_board, start_cell, goal_state

def generator_pathcheck(k):
     fleg = True
     while fleg:
         # Generate a random maze and start/goal states
         init_board, start_cell, goal_state = generator(k)

         # Use BFS to check if there is a valid path
         path_matrix = BFS(init_board, start_cell)

         # Check if there is a valid path from start to goal
         if path_matrix[goal_state[0], goal_state[1]] != -1:
             return init_board, start_cell, goal_state
