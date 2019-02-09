import pygame
from random import randint
import numpy as np

class Board():

    """4x4 2048 game board"""

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = np.zeros((board_size, board_size), int)


    def draw(self):
        print()
        for i in range(self.board_size):
            print(self.board[i])
        print()


    def get_piece(self):
        piece = 2
        while True:
            x_pos = randint(0, 3)
            y_pos = randint(0, 3)
            if self.board[x_pos][y_pos] == 0:
                self.board[x_pos][y_pos] = piece
                break
   

    def proc_line(self, l):
        a, b = -1, -1
        result = []
        for i in range(self.board_size):
            if l[i] != 0: 
                if a == -1:
                    a = l[i]
                else:
                    b = l[i]
                    if a == b:
                        result.append(2 * a)
                        a = -1
                    else:
                        result.append(a)
                        a = b
        if a != -1:
            result.append(a)
        lenght = len(result)
        if lenght < self.board_size:
            for i in range(self.board_size - lenght):
                result.append(0)
        return result


    def move_left(self):
        for index, l in enumerate(self.board):
            self.board[index] = self.proc_line(l)


    def move_right(self):
        for index, l in enumerate(self.board):
            self.board[index] = self.proc_line(l[::-1])[::-1]


    def move_up(self):
        t = np.array(self.board).transpose()
        for index, l in enumerate(t):
            t[index] = self.proc_line(l)
        self.board = t.transpose()


    def move_down(self):
        t = np.array(self.board).transpose()
        for index, l in enumerate(t):
            t[index] = self.proc_line(l[::-1])[::-1]
        self.board = t.transpose()



board = Board(4)
board.get_piece()

while True:
    board.get_piece()
    board.draw()
    move = input()
    if move == "a":
        board.move_left()
    if move == "s":
        board.move_down()
    if move == "d":
        board.move_right()
    if move == "w":
        board.move_up()


