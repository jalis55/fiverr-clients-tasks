"""
Tic Tac Toe Player
"""
import copy
import math
from queue import Empty

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[ EMPTY for j in range(3)] for i in range(3)]


board = initial_state()

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numO = 0
    numX = 0
    FirstPlayer = None
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == O:
                numO += 1
            if board[i][j] == X:
                numX += 1
    return X if numO == numX else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possact = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board [i][j] == Empty:
                possact.add((i, j))
    return possact


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardcopy = copy.deepcopy(board)
    boardcopy[action[0]][action[1]] = player(board)
    return boardcopy
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        wonO = True
        wonX = True
        for j in range(3):
            if board[i][j] == O or board[i][j] == EMPTY:
                wonX = False
            if board[i][j] == X or board[i][j] == EMPTY:
                wonO = False
        if wonX:
            return X
        if wonO:
            return O

    for j in range(3):
        wonO = True
        wonX = True
        for i in range(3):
            if board[i][j] == X or board[i][j] == EMPTY:
                wonO = False
            if board[i][j] == O or board[i][j] == EMPTY:
                wonX = False
        if wonX:
            return X
        if wonO:
            return O

    diag1 = ''
    diag2 = ''
    j = 2

    for i in range(3):
      diag1 += str(board[i][i])
      diag2 += str(board[i][j])
      j -= 1

    if diag1 == 'XXX' or diag2 == 'XXX':
      return X
    elif diag1 == 'OOO' or diag2 == 'OOO':
      return O


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for row in board:
        for item in row:
            if item == Empty:
                return False
    return True   

    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    resB = winner(board)
    return 1 if resB == X else -1 if resB == O else 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    Max = float("-inf")
    Min = float("-inf")

    return Max_Value(board, Max, Min)[1] if player(board) ==1 else Min_Value(board, Max, Min)[1]



def Max_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None]
    v = float('-inf')
    for action in actions(board):
        test = Min_Value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]

def Min_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None]
    v = float('-inf')
    for action in actions(board):
        test = Max_Value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]