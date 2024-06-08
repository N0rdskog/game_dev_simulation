import numpy as np
from game_interface import GameInterface

class TicTacToe(GameInterface):
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = np.zeros((3, 3))
        self.current_winner = None

    def handle_event(self, event):
        row, col, player = event
        if self.board[row][col] == 0:
            self.board[row][col] = player
            if self.check_winner(row, col, player):
                self.current_winner = player
            return True
        return False

    def check_winner(self, row, col, player):
        if np.all(self.board[row, :] == player) or np.all(self.board[:, col] == player):
            return True
        if row == col and np.all(np.diag(self.board) == player):
            return True
        if row + col == 2 and np.all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False

    def update(self):
        pass  # No continuous state updates needed for Tic-Tac-Toe

    def get_state(self):
        return self.board.copy()

    def is_over(self):
        return self.current_winner is not None or np.all(self.board != 0)

    def get_winner(self):
        return self.current_winner