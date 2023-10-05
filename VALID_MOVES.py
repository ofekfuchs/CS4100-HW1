def valid_moves(maze, node):
    moves = []
    row, col = node

    # Check move to the right
    if col - maze[row, col] >= 0:
        moves.append((row, col - maze[row, col]))

    # Check move to the left
    if col + maze[row, col] < maze.shape[1]:
        moves.append((row, col + maze[row, col]))

    # Check move down
    if row - maze[row, col] >= 0:
        moves.append((row - maze[row, col], col))

    # Check move up
    if row + maze[row, col] < maze.shape[0]:
        moves.append((row + maze[row, col], col))

    return moves
