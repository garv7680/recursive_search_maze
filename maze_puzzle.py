""" 
API
===
get_start_state: returns a random starting state
next_states: returns list of possible next states
is_goal: returns True if passed the goal state
print_state: pretty-prints a state
"""

from prim_maze_generator import generate_maze, print_maze


def is_goal(state):
    """defines the goal state"""
    board = state[0]
    goal = (board, (len(board)-1, board[-1].index('c')))
    return state == goal


def next_states(state):
    """ returns a list of all states reachable from
    the given state"""
    board = state
    currentPosy = board[1][0]
    currentPosx = board[1][1]
    board = board[0]

    #right, left, up, downm
    possibilities = [(currentPosy, currentPosx+1),
                     (currentPosy, currentPosx-1),
                     (currentPosy+1, currentPosx),
                     (currentPosy-1, currentPosx)]

    path = []
    boardSolved = board.copy()

    for item in possibilities:

        if (item[0] < 0 or item[1] < 0 or item[0] > len(board) or item[1] > len(board[0])):
            continue
        elif board[item[0]][item[1]] == "w":
            continue
        elif item in path:
            continue
        else:
            new_path = (board, (item))
            path.append(new_path)

    # return list of next states
    return path


def get_start_state():
    """ Gets the start state """

    # start board
    board = generate_maze(15, 15, True)
    startRow = 0
    # locate the start position

    startPos = board[startRow].index('c')
    # return the state
    return (board, (startPos, startRow))
#(goal,currentPos) = get_start_state()


def print_state(currentPosition):
    """Pretty-prints a state"""
    print(currentPosition)
