"""
start_simulation_module.py:
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"

from constant_configuration import *
from game_board_class import *
from pathfinding import *
from base_implementation_v2 import *


def start_simulation(my_game_board: GameBoard) -> bool:
    """
    This function starts the simulation
    @param my_game_board: The game board object
    @return: True if simulation success False otherwise
    """
    for current_step in range(TotalStepSize):
        all_bfs_path = bfs(my_game_board)  # get all paths

        filtered_box_choices = filter_box_choices(all_bfs_path)
        for filtered_box_coordinate, action in filtered_box_choices:
            del all_bfs_path[(filtered_box_coordinate, action)]
        all_box_choices = list(all_bfs_path.keys())
        if not all_box_choices:
            print("No more possible path")
            return False
        policy = decide_policy(list(all_bfs_path.keys()))  # 0 = random, 1 = greedy
        if policy:
            print("greedy policy")
            selected_box_coordinate, action = get_greedy_choice(all_bfs_path)
        else:
            print("random policy")
            selected_box_coordinate, action = random.choice(all_box_choices)
        next_to_board_coordinate_x, next_to_board_coordinate_y = all_bfs_path[(selected_box_coordinate, action)][-2]
        my_game_board.teleportation(next_to_board_coordinate_x, next_to_board_coordinate_y)
        my_game_board.update_current_player_coordinate(action)
        if my_game_board.is_end_game():
            return True
    if my_game_board.is_any_box_reach_end():
        return True
    return False
