import numpy as np
import board
import constants

class Connect4Board:
    def __init__ (self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows,cols))
        self.piece_count = 0
        self.current_player = 1

    def can_place(self, x, y):
        place = False
        lowest_pos = -1
        i=5
        while place == False and i >= 0: 
            if self.grid[i][x] == 0:
                place = True
                lowest_pos = i
                continue
            i-=1
        return place, lowest_pos

    def place_circle(self, x, y, screen):
        if self.current_player == 1:
            color = constants.RED
        else: 
            color = constants.BLUE
        board.drawCircle(screen, x, y, color)        
        
    def player_switch(self):
        if self.current_player == 1:
            self.current_player = 2
            # print("Switch to player 2!")
        else:
            self.current_player = 1
            # print("Switch to player 1!")

    def check_winner(self):
        board = self.grid
        winner = False

        rows = 6
        cols = 7
        for row in range(rows):
            for col in range(cols - 3):
                if board[row, col] == board[row, col + 1] == board[row, col + 2] == board[row, col + 3] != 0:
                    winner = True

        for col in range(cols):
            for row in range(rows - 3):
                if board[row, col] == board[row + 1, col] == board[row + 2, col] == board[row + 3, col] != 0:
                    winner = True

        for row in range(rows - 3):
            for col in range(cols - 3):
                if board[row, col] == board[row + 1, col + 1] == board[row + 2, col + 2] == board[row + 3, col + 3] != 0:
                    winner = True

        for row in range(3, rows):
            for col in range(cols - 3):
                if board[row, col] == board[row - 1, col + 1] == board[row - 2, col + 2] == board[row - 3, col + 3] != 0:
                    winner = True

        return winner

    def reset_board(self):
        self.grid = np.zeros((self.rows, self.cols))
        self.piece_count = 0
        self.current_player = 1
