"""
evaluate_module.py:
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"

from constant_configuration import *
from base_implementation_v2 import *
from pathfinding import *


def evaluate(my_game_board):
    for i in range(20000):
        all_bfs_path = bfs(my_game_board)  # get all paths
        all_box_choices = list(all_bfs_path.keys())
        if not all_box_choices:
            return False

        selected_box_coordinate, action = get_greedy_choice(all_bfs_path)

        next_to_board_coordinate_x, next_to_board_coordinate_y = all_bfs_path[(selected_box_coordinate, action)][-2]
        my_game_board.teleportation(next_to_board_coordinate_x, next_to_board_coordinate_y)
        my_game_board.update_current_player_coordinate(action)
        if my_game_board.is_end_game():
            return True
    return False