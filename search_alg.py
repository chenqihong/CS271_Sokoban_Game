"""
Search algorithms that can be used for the sokoban solver.
Includes:

Breadth first search - Find all possible paths to the given box location
                     - Check if path to box is blocked, if blocked, ignore box
                     - Find reachable boxes only

A* search - Find and use shortest possible path from start to goal node
            while also avoiding obstacles/walls
            -- May not be as useful

"""

from game_board_class import *
import collections


def is_out_of_bounds(board_size, position):
    """
    :param board_size: Dimensions of board
    :param position: Position to check
    :return: Whether the given position is out of board or not
    """
    if position[0] > board_size[0] or position[1] > board_size[1]:
        return True
    return False


def get_neighbors(board:GameBoard, position):
    """
    :param board: current board state
    :param position: coordinate on grid
    :return: neighbors: a list of neighboring coordinates for given position
    """
    possible_neighbors = [(position[0]+1, position[1]), (position[0]-1, position[1]),
                 (position[0], position[1]+1), (position[0], position[1]-1)]
    valid_neighbors = []

    # ignore walls when getting neighbors because cannot move to wall
    # make sure found neighbor is inside the bounds of the game board
    for neighbor in possible_neighbors:
        if neighbor not in board.wall_coordinate_list and \
                not is_out_of_bounds(board_size=board.get_dimension(), position=neighbor):
            valid_neighbors.append(neighbor)

    return valid_neighbors


def get_accessible_boxes(board:GameBoard):
    # Do BFS path search on each box location
    # If there is no path for box then it cannot be reached
    # Not considering paths that include moving boxes (edge case)
    pass



def bfs(board: GameBoard, box_location):
    """
    :param board: Current game board state
    :return:
    """
    # Use Nodes to trace path
    pass






