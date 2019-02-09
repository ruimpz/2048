import pygame
from random import randint
import numpy as np

class Board():

    """4x4 2048 game board"""

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = np.zeros((board_size, board_size), int)


    def draw(self):
#        print()
#        for i in range(self.board_size):
#            print(self.board[i])
#        print()
        for i in range(self.board_size):
            for j in range(self.board_size):
                x_pos = j * 200
                y_pos = i * 200
                color = colors[self.board[i][j]]
                pygame.draw.rect(screen, color, [x_pos, y_pos, 200, 200])



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


clock = pygame.time.Clock()
tick_rate = 30
game_over = False

colors = {
    0: (60, 56, 54),
    2: (235, 219, 178),
    4: (251, 241, 199),
    8: (69, 133, 136),
    16: (142, 192, 124),
    32: (184, 187, 28),
    64: (250, 189, 47),
    128: (211, 134, 155),
    256: (251, 73, 52),
    512: 0,
    1024: 0,
    2048: 0
}

screen = pygame.display.set_mode((800,800))

board = Board(4)
board.get_piece()


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
   
    board.draw()
    pygame.display.update()
#    clock.tick(tick_rate)
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            board.move_left()
            board.get_piece()
        elif event.key == pygame.K_RIGHT:
            board.move_right()
            board.get_piece()
        elif event.key == pygame.K_UP:
            board.move_up()
            board.get_piece()
        elif event.key == pygame.K_DOWN:
            board.move_down()
            board.get_piece()
    
    pygame.time.delay(80)
pygame.quit()
quit()






#while True:
#    board.get_piece()
#    board.draw()
#
#    move = input()
#    if move == "a":
#        board.move_left()
#    if move == "s":
#        board.move_down()
#    if move == "d":
#        board.move_right()
#    if move == "w":
#        board.move_up()


