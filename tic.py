from collections import deque
import copy

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def print_board(self):
        print("\n")
        for i, row in enumerate(self.board):
            print(f" {row[0]} | {row[1]} | {row[2]} ")
            if i < 2:
                print("-----------")
        print("\n")
    
    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '
    
    def make_move(self, row, col, player):
        if self.is_valid_move(row, col):
            self.board[row][col] = player
            return True
        return False
    
    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))
    
    def get_available_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves
    
    def bfs_best_move(self, player):
        """Find best move using BFS"""
        opponent = 'X' if player == 'O' else 'O'
        queue = deque()
        
        # Enqueue all possible first moves
        for move in self.get_available_moves():
            board_copy = copy.deepcopy(self.board)
            queue.append((board_copy, move, 0))  # (board_state, first_move, depth)
        
        best_move = None
        best_score = float('-inf')
        move_scores = {}
        
        while queue:
            board_state, first_move, depth = queue.popleft()
            
            # Create temporary game with this board state
            temp_game = TicTacToe()
            temp_game.board = board_state
            
            winner = temp_game.check_winner()
            
            # Evaluate terminal states
            if winner == player:
                score = 10 - depth  # Prefer faster wins
                if first_move not in move_scores or score > move_scores[first_move]:
                    move_scores[first_move] = score
                continue
            elif winner == opponent:
                score = -10 + depth  # Prefer delaying losses
                if first_move not in move_scores or score > move_scores[first_move]:
                    move_scores[first_move] = score
                continue
            elif temp_game.is_board_full():
                score = 0  # Draw
                if first_move not in move_scores or score > move_scores[first_move]:
                    move_scores[first_move] = score
                continue
            
            # Limit search depth to avoid excessive computation
            if depth >= 6:
                if first_move not in move_scores:
                    move_scores[first_move] = 0
                continue
            
            # Determine whose turn it is at this depth
            turn = player if depth % 2 == 0 else opponent
            
            # Generate next moves
            for move in temp_game.get_available_moves():
                new_board = copy.deepcopy(board_state)
                new_board[move[0]][move[1]] = turn
                queue.append((new_board, first_move, depth + 1))
        
        # Choose move with best score
        if move_scores:
            best_move = max(move_scores, key=move_scores.get)
        else:
            # Fallback to first available move
            available = self.get_available_moves()
            best_move = available[0] if available else None
        
        return best_move
    
    def play(self):
        print("Welcome to Tic Tac Toe!")
        print("You are X, AI is O")
        print("Enter row and column (0-2) separated by space")
        
        while True:
            self.print_board()
            
            if self.current_player == 'X':
                # Human player
                try:
                    row, col = map(int, input("Your move (row col): ").split())
                    if not self.make_move(row, col, 'X'):
                        print("Invalid move! Try again.")
                        continue
                except (ValueError, IndexError):
                    print("Invalid input! Enter row and column (0-2)")
                    continue
            else:
                # AI player using BFS
                print("AI is thinking...")
                move = self.bfs_best_move('O')
                if move:
                    self.make_move(move[0], move[1], 'O')
                    print(f"AI plays: {move[0]} {move[1]}")
            
            # Check for winner
            winner = self.check_winner()
            if winner:
                self.print_board()
                if winner == 'X':
                    print("Congratulations! You won!")
                else:
                    print("AI wins!")
                break
            
            # Check for draw
            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break
            
            # Switch player
            self.current_player = 'O' if self.current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
