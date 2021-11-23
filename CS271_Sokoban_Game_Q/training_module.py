"""
training_module.py:
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"


from constant_configuration import *
from game_board_class import *
from pathfinding import *
from base_implementation_v2 import *


def training(my_game_board: GameBoard, BaseEpsilon: float) -> None:
    """
    This function performances the training
    :param my_game_board:
    :param BaseEpsilon:
    :return:
    """
    total_number_boxes_done = 0
    picked_box_action_list = []
    for current_step in range(TotalStepSize):
        box_position = list(tuple(my_game_board.get_all_boxes_position()))
        player_position = my_game_board.get_current_player_coordinate()
        current_state = str(player_position) + str(box_position)
        all_bfs_path = bfs(my_game_board)
        all_selections = list(all_bfs_path.keys())
        print("At pos = ", my_game_board.get_current_player_coordinate()," all bfs path = ", all_bfs_path)
        if not all_selections:
            return
        policy = decide_policy(all_selections, BaseEpsilon, current_state)  # 0 = random, 1 = greedy
        if policy:
            selected_box_coordinate, action = get_greedy_choice(current_state, all_selections)
        else:
            selected_box_coordinate, action = random.choice(all_selections)

        next_to_board_coordinate_x, next_to_board_coordinate_y = all_bfs_path[(selected_box_coordinate, action)][-2]
        my_game_board.teleportation(next_to_board_coordinate_x, next_to_board_coordinate_y)
        my_game_board.update_current_player_coordinate(action)

        next_state = str(my_game_board.get_current_player_coordinate()) + str(my_game_board.get_all_boxes_position())
        if my_game_board.is_any_box_reach_end():
            number_boxes_done_now = my_game_board.get_number_box_done()
            if number_boxes_done_now > total_number_boxes_done:
                reward = 100
                total_number_boxes_done = number_boxes_done_now
            else:
                if picked_box_action_list.count((selected_box_coordinate, action)) > 2:
                    reward = picked_box_action_list.count((selected_box_coordinate, action)) * (-5)
                else:
                    reward = -5
        elif my_game_board.is_end_game():
            reward = 1000
        elif picked_box_action_list.count((selected_box_coordinate, action)) > 2:
            reward = picked_box_action_list.count((selected_box_coordinate, action)) * -5
        else:
            reward = -5
        update_Q_Value(current_state, selected_box_coordinate, action, reward, next_state)



