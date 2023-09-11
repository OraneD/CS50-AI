"""
Tic Tac Toe Player
"""

import math
import copy

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
    number_X = 0
    number_O = 0
    for lst in board :
        for position in lst : 
            if position == "X" : 
                number_X += 1
            elif position == "O" : 
                number_O += 1
    if number_O < number_X :
        return "O"
    else :
        return "X"
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i,j))
    return actions_set




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_actions = actions(board)
    if action not in possible_actions:
        raise Exception("action not allowed")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board :
        if len(set(row)) == 1 :
            return row[0]
    
    for column in range(3):
        if len(set([row[column] for row in board])) == 1:
            return board[0][column]
    
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True

    for row in board:
        for cells in row:
            if cells == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
        
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0


def maxvalue(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    return v


def minvalue(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
    return v





def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
      return None

    best_action = None
    
    v_X = -math.inf
    v_O = math.inf
    
    if player(board) == X:
        for action in actions(board) :
            if v_X < minvalue(result(board,action)):
                v_X = minvalue(result(board,action))
                best_action = action
    
    elif player(board) == O :
        for action in actions(board) :
            if v_O > maxvalue(result(board, action)):
                v_O = maxvalue(result(board,action))
                best_action = action
    return best_action





    # faut d'abord récupérer les actions possibles
    # après faut trouver quelle action est la meilleure
    # faut se mettre comme si on était l'adversaire donc si je suis O
    # je me demande ce que X ferait après mon coup
