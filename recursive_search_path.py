# set recursion limit
from path import add_state_to_path, print_path
from maze_puzzle import next_states, is_goal, get_start_state, print_state
from os import stat
import sys

from prim_maze_generator import print_maze
sys.setrecursionlimit(10**6)

# solver


def recursive_search(state, closed, path):
    board = state[0]
    currentPos = state[1]

    if state in closed:
        return False

    closed.append(state)
    new_path = add_state_to_path(path, state)

    if is_goal(state):
        return new_path

    open = next_states(state)
    for next_state in open:
        result = recursive_search(next_state, closed, new_path)
        if result != False:
            return result

    return False


# run the solver
start_state = get_start_state()

closed = []

result = recursive_search(start_state, closed, [])
print_maze(start_state[0])
if result == False:
    print_maze(start_state)
    print("not solvable")
else:
    print_path(result, print_state)
