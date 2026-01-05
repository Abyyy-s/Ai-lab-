Open
tictac2.py
1 from collections import deque
2 3 4
PLAYER, AI, EMPTY = "O"
5 def print_board(board):
for i in range(0, 9, 3):
6
7
print(board[i:i+3])
co
9 def check_ winner(board):
wins = [(0,1,2),(3,4,5) ,(6,7,8),(0,3,6), (1,4,7),(2,5,8),(0,4,8),(2,4,6)]
10
for a, b, c in wins:
11
tf board[a] == board[b] == board[c] !- EMPTY: return board[a]
13 14 15 17 18 19 ANN
return "Draw" if EMPTY not in board else None
def bfs best_ move(board):
queue = deque([(board, True)]) # (state, is_AI_turn)
16
while queue:
queue.popleft()
state, is_AI_turn
result = check_winner(state)
if result -= AI: return True
20
if result in [PLAYER, "Draw"]: continue
for move in [i for i in range(9) if state[i] == EMPTY]:
new_state = state[:]
new_state[move] = AI if is_AI_turn else PLAYER
queue.append((new_state, not is_AI_turn))
if is_ AI_ turn: return move # AI makes the move
return None
28
29 def play():
O
*
[EMPTY]
30
board
while True:
print_board(board)
move = int(input("Enter position (0-8): "))
33 34 36 21 38
if board[move] != EMPTY: continue
PLAYER
board[move]
if check_winner(board): break
ai_move = bfs_best_move(board)
if ai_move is not None: board[ai_move] = AI
if check_winner(board): break
print_board(board)
print("Result:", check_winner(board))