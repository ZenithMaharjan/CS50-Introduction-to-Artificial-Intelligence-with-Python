"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                count += 1

    if count % 2 == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.add((i,j))

    return actions   

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
 
    current = player(board)

    new_board = deepcopy(board)
    i , j = action

    if board[i][j] != None:
        raise Exception
    else:
        new_board[i][j] = current

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for y in range(3):
        # Check horizontal lines
      if (board[y][0] == board[y][1] == board[y][2]) and (board[y][0] != EMPTY):
          return board[y][0]
        # check vertical lines
      if (board[0][y] == board[1][y] == board[2][y]) and (board[0][y] != EMPTY):
          return board[0][y]

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]) and board[1][1] != EMPTY:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY and winner(board) == None:
                    return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    res = winner(board)
    
    if res == X:
        return 1
    elif res == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -10
            for action in actions(board):
                minval = min_value(result(board, action))[0]
                if minval > v:
                    v = minval
                    optimal_move = action
            return v, optimal_move

    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = 10
            for action in actions(board):
                maxval = max_value(result(board, action))[0]
                if maxval < v:
                    v = maxval
                    optimal_move = action
            return v, optimal_move

    curr_player = player(board)

    if terminal(board):
        return None

    if curr_player == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]