"""
base_implementation_v2.py: The base_implementation file of the project sokoban for CS271 for training only
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"

from constant_configuration import *
from game_board_class import *


def decide_policy(all_reachable_boxes: list, BaseEpsilon: float, current_state) -> int:
    """
    Determines the policy: random or greedy
    @param all_reachable_boxes: list of tuples (box_pos, last_move_to_that_box)
    @param BaseEpsilon: used to determine which policy to go for.
    @return: 0 if random, 1 if greedy
    """
    if current_state not in Q_table:
        return 0
    # All boxes have some Q values
    random_val = random()
    if BaseEpsilon > random_val:
        return 0
    return 1


def get_greedy_choice(current_state: str, all_reachable_boxes: list) -> tuple:
    """
    This function finds the greedy choice of the box
    @param current_state:
    @param all_reachable_boxes: (2,3)
    @return: ((x,y), U)
    """
    temp_dict = defaultdict(float)
    for reachable_box, action in all_reachable_boxes:
        if (reachable_box, action) in Q_table[current_state]:
            temp_dict[(reachable_box, action)] = Q_table[current_state][(reachable_box, action)]
    return max(temp_dict, key=temp_dict.get)


def update_Q_Value(current_state, selected_box_coordinate, action, reward, next_state):
    Q_predict = Q_table[current_state][(selected_box_coordinate, action)]
    if next_state in Q_table:
        Q_target = reward + gamma * ( max(Q_table[next_state].values() ) )
    else:
        Q_target = reward
    Q_table[current_state][(selected_box_coordinate, action)] += learningRate * (Q_target - Q_predict)




