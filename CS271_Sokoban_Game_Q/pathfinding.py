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
from constant_configuration import *


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


def get_direction(cord1, cord2):
    if cord1[0] - cord2[0] == 1: return 'U'
    if cord1[0] - cord2[0] == -1: return 'D'
    if cord1[1] - cord2[1] == 1: return 'L'
    if cord1[1] - cord2[1] == -1: return 'R'


def bfs(board: GameBoard):
    """
    Returns all possible paths to location from player position
    :param board: Current game board state
    :return: all possible paths avoiding walls and other boxes
                to box location
    """
    final_paths = []
    for box in board.get_all_boxes_position():
        # Use Nodes to trace path

        start_pos = board.get_current_player_coordinate()
        queue = [[start_pos]]
        while queue:
            cur_path = queue.pop()
            cur_pos = cur_path[-1]

            if cur_pos == box:
                final_paths.append(cur_path)
                continue
            for neighbor in get_neighbors(board, cur_pos, box):
                if neighbor not in cur_path:
                    new_path = list(cur_path)
                    new_path.append(neighbor)
                    queue.append(new_path)
    results = dict()
    for path in final_paths:
        if path[-2][0] - path[-1][0] == 1:
            next = (path[-1][0]-1, path[-1][1])
        elif path[-2][0] - path[-1][0] == -1:
            next = (path[-1][0]+1, path[-1][1])
        elif path[-2][1] - path[-1][1] == 1:
            next = (path[-1][0], path[-1][1]-1)
        elif path[-2][1] - path[-1][1] == -1:
            next = (path[-1][0], path[-1][1]+1)
        if not (board.is_wall(next) or board.is_box(next) or next in state_value_table):
            results[(path[-1], get_direction(path[-2], path[-1]))] = path
    return results
