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


def start_simulation(my_game_board: GameBoard, BaseEpsilon: float) -> None:
    """
    This function starts the simulation
    @param my_game_board: The game board object
    @return: True if simulation success False otherwise
    """
    global total_number_boxes_done
    for current_step in range(TotalStepSize):
        all_bfs_path = bfs(my_game_board)  # get all paths

        all_box_choices = list(all_bfs_path.keys())
        if not all_box_choices:
            simulation_choices_list.append((selected_box_coordinate, action, -20))
            return

        policy = decide_policy(list(all_bfs_path.keys()), BaseEpsilon)  # 0 = random, 1 = greedy

        if policy:
            selected_box_coordinate, action = get_greedy_choice(all_bfs_path)
        else:
            selected_box_coordinate, action = random.choice(all_box_choices)

        next_to_board_coordinate_x, next_to_board_coordinate_y = all_bfs_path[(selected_box_coordinate, action)][-2]
        my_game_board.teleportation(next_to_board_coordinate_x, next_to_board_coordinate_y)

        my_game_board.update_current_player_coordinate(action)

        if my_game_board.is_any_box_reach_end():
            number_boxes_done_now = my_game_board.get_number_box_done()
            if number_boxes_done_now > total_number_boxes_done:
                reward = 350
                total_number_boxes_done = number_boxes_done_now
            else:
                if simulation_choices_list.count((selected_box_coordinate, action)) > 2:
                    reward = simulation_choices_list.count((selected_box_coordinate, action)) * -5
                else:
                    reward = -5
        elif my_game_board.is_end_game():
            reward = 1000
        elif simulation_choices_list.count((selected_box_coordinate, action)) > 2:
            reward = simulation_choices_list.count((selected_box_coordinate, action)) * -5
        else:
            reward = -5
        simulation_choices_list.append((selected_box_coordinate, action, reward))
        if my_game_board.is_end_game() or total_number_boxes_done == 3:
            return
    return
