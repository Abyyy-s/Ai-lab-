from collections import deque

PLAYER, AI, EMPTY = "O", "X", ""

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])

def check_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6), (1,4,7),(2,5,8), (0,4,8),(2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != EMPTY: return board[a]
    return "Draw" if EMPTY not in board else None

def bfs_best_move(board):
    queue = deque([(board, True)]) # (state, is_AI_turn)
    while queue:
        state, is_AI_turn = queue.popleft()
        result = check_winner(state)
        if result == AI: return True
        if result in [PLAYER, "Draw"]: continue
        for move in [i for i in range(9) if state[i] == EMPTY]:
            new_state = state[:]
            new_state[move] = AI if is_AI_turn else PLAYER
            queue.append((new_state, not is_AI_turn))
        if is_AI_turn: return move # AI makes the move
    return None

def play():
    board = [EMPTY] * 9
    while True:
        print_board(board)
        move = int(input("Enter position (0-8): "))
        if board[move] != EMPTY: continue
        board[move] = PLAYER
        if check_winner(board): break
        ai_move = bfs_best_move(board)
        if ai_move is not None: board[ai_move] = AI
        if check_winner(board): break
        print_board(board)
    print("Result:", check_winner(board))

play()