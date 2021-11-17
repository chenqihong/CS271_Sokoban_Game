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


def get_neighbors(board: GameBoard, position, goal):
    """
    :param board: current board state
    :param position: coordinate on grid
    :return: neighbors: a list of neighboring coordinates for given position
    """
    possible_neighbors = [(position[0] + 1, position[1]), (position[0] - 1, position[1]),
                          (position[0], position[1] + 1), (position[0], position[1] - 1)]
    valid_neighbors = []

    box = board.box_coordinate_list.copy()
    box.remove(goal)

    # ignore walls when getting neighbors because cannot move to wall
    # make sure found neighbor is inside the bounds of the game board
    for neighbor in possible_neighbors:
        if neighbor not in board.wall_coordinate_list and neighbor not in box and \
                not is_out_of_bounds(board_size=board.get_dimension(), position=neighbor):
            valid_neighbors.append(neighbor)

    return valid_neighbors


def get_accessible_boxes(board: GameBoard):
    # Do BFS path search on each box location
    # If there is no path for box then it cannot be reached
    # Not considering paths that include moving boxes (edge case)
    pass


def bfs(board: GameBoard, box_location):
    """
    Returns all possible paths to location from player position
    :param box_location: Location of box to be reached
    :param board: Current game board state
    :return: all possible paths avoiding walls and other boxes
                to box location
    """
    # Use Nodes to trace path
    final_paths = []
    start_pos = board.get_current_player_coordinate()
    queue = [[start_pos]]
    while queue:
        cur_path = queue.pop()
        cur_pos = cur_path[-1]

        if cur_pos == box_location:
            final_paths.append(cur_path)
            continue
        for neighbor in get_neighbors(board, cur_pos, box_location):
            if neighbor not in cur_path:
                new_path = list(cur_path)
                new_path.append(neighbor)
                queue.append(new_path)
    return final_paths