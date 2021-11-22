"""
start_simulation_module.py:
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"

import time

from constant_configuration import *
from game_board_class import *
from pathfinding import *
from base_implementation_v2 import *
from time import sleep


def start_simulation(my_game_board: GameBoard) -> None:
    """
    This function starts the simulation
    @param my_game_board: The game board object
    @return: True if simulation success False otherwise
    """

    for current_step in range(TotalStepSize):
        # start = time.time()
        all_bfs_path = bfs(my_game_board)  # get all paths
        # end = time.time()
        # print("find all paths takes: ", end - start)
        all_box_choices = list(all_bfs_path.keys())
        if not all_box_choices:
            simulation_choices_list.append((selected_box_coordinate, action, -2000))
            return
        # start = time.time()
        policy = decide_policy(list(all_bfs_path.keys()))  # 0 = random, 1 = greedy
        # end = time.time()
        # print("decide policy takes: ", end - start)
        # start = time.time()
        if policy:
            selected_box_coordinate, action = get_greedy_choice(all_bfs_path)
        else:
            selected_box_coordinate, action = random.choice(all_box_choices)
        # end = time.time()
        # print("make decision takes: ", end - start)

        next_to_board_coordinate_x, next_to_board_coordinate_y = all_bfs_path[(selected_box_coordinate, action)][-2]
        my_game_board.teleportation(next_to_board_coordinate_x, next_to_board_coordinate_y)
        # start = time.time()
        my_game_board.update_current_player_coordinate(action)
        # end = time.time()
        # print("make move takes: ", end - start)
        if my_game_board.is_any_box_reach_end():
            reward = 10
        elif my_game_board.is_end_game():
            reward = 1000
        else:
            reward = -1
        simulation_choices_list.append((selected_box_coordinate, action, reward))
        if my_game_board.is_end_game():
            return

    return
