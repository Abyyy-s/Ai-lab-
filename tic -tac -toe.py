from collections import deque
import copy

# Print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

# Check if a player has won
def is_winner(board, player):
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Check if board is full
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Convert board to tuple (for visited set)
def board_to_tuple(board):
    return tuple(tuple(row) for row in board)

# Generate all possible next states
def generate_children(board, player):
    children = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                new_board = copy.deepcopy(board)
                new_board[i][j] = player
                children.append(new_board)

    return children

# BFS Algorithm
def bfs_tic_tac_toe():
    initial_board = [[' ' for _ in range(3)] for _ in range(3)]
    queue = deque()
    visited = set()

    # Each element: (board, current_player)
    queue.append((initial_board, 'X'))
    visited.add(board_to_tuple(initial_board))

    while queue:
        board, player = queue.popleft()

        # Goal test
        if is_winner(board, 'X'):
            print("X wins!")
            print_board(board)
            return

        if is_winner(board, 'O'):
            print("O wins!")
            print_board(board)
            return

        if is_full(board):
            continue

        # Switch player
        next_player = 'O' if player == 'X' else 'X'

        # Expand node
        for child in generate_children(board, player):
            board_key = board_to_tuple(child)

            if board_key not in visited:
                visited.add(board_key)
                queue.append((child, next_player))

    print("No winning state found.")

# Run BFS
bfs_tic_tac_toe()

