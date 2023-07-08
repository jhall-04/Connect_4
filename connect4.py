import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
# Define game board
gameBoard = np.array([[0 for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)])


# Print game board
def printboard(board):
    for row in board:
        print(row)


# Insert peice and update game board
def insertpeice(column, board, player, players):
    i = 0
    while column > 7 or column < 0:
        print("Choose Available Column")
        column = int(input("Enter Column: ")) - 1
    while True:
        if board[0][column] in players:
            print("Choose Available Column")
            column = int(input("Enter Column: ")) - 1
        if board[i][column] == 0 and i != len(board) - 1:
            i += 1
        elif board[i][column] in players:
            board[i-1][column] = player
            return
        elif i == len(board) - 1:
            board[i][column] = player
            return


# Win check by Manuel Faysse stack overflow
horizontal_kernel = np.array([[1 for k in range(4)]])
vertical_kernel = np.transpose(horizontal_kernel)
diag1_kernel = np.eye(4, dtype=np.uint8)
diag2_kernel = np.fliplr(diag1_kernel)
detection_kernels = [horizontal_kernel, vertical_kernel, diag1_kernel, diag2_kernel]


def winning_move(board, player):
    for kernel in detection_kernels:
        if (convolve2d(board == player, kernel, mode="valid") == 4).any():
            return True
    return False
# End of help


currentPlayers = [1, 2]
turn = 0
while True:
    currentPlayer = currentPlayers[turn % 2]

    pc = int(input("Enter Column: ")) - 1
    insertpeice(pc, gameBoard, currentPlayer, currentPlayers)
    printboard(gameBoard)
    if winning_move(gameBoard, currentPlayer):
        print(f"Player {currentPlayer} wins")
        break
    turn += 1
