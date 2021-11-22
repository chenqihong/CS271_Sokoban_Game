"""
base_implementation_v2.py: The base_implementation file of the project sokoban for CS271 for training only
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"

from constant_configuration import *
from game_board_class import *


def decide_policy(all_reachable_boxes: list) -> int:
    """
    Determines the policy: random or greedy
    @param all_reachable_boxes: list of tuples (box_pos, last_move_to_that_box)
    @return: 0 if random, 1 if greedy
    """
    for box_pos, action in all_reachable_boxes:
        if (box_pos, action) not in UCT_table:
            return 0

    # All boxes have some UCT values
    if BaseEpsilon > 0.3:
        return 0
    return 1


def get_greedy_choice(all_bfs_path: defaultdict) -> tuple:
    """
    This function finds the greedy choice of the box
    @param all_bfs_path: {((x,y), U): (3/5)}
    @return: ((x,y), U)
    """
    temp_UCT_table_dict = defaultdict(float)
    for coordinate, action in all_bfs_path:
        temp_UCT_table_dict[(coordinate, action)] = UCT_table[(coordinate, action)]
    return max(temp_UCT_table_dict, key=temp_UCT_table_dict.get)


def update_UTC_table() -> None:
    """
    Update the UCT table for all nodes along the path based on the simulation result
    @return: None
    """
    G = 0
    simulation_choices_list.reverse()
    for count in range(len(simulation_choices_list)):
        node_coordinate, action, reward = simulation_choices_list[count]
        state_action = node_coordinate, action
        G += gamma ** count * reward
        if state_action in UCT_table:
            returns[state_action].append(G)
        else:
            returns[state_action] = [G]

        UCT_table[state_action] = sum(returns[state_action])/len(returns[state_action])




