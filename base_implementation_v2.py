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
    if random.random() <= BaseEpsilon:
        return 0
    return 1


def get_greedy_choice(all_bfs_path: defaultdict) -> tuple:
    """
    This function finds the greedy choice of the box
    @param all_bfs_path: {((x,y), U): (3/5)}
    @return: ((x,y), U)
    """
    new_UCT_dict = defaultdict(float)
    for coordinate, action in all_bfs_path:
        win_games, total_games = UCT_table[(coordinate, action)]
        win_rate = win_games/total_games
        new_UCT_dict[(coordinate, action)] = win_rate
    return max(new_UCT_dict, key=new_UCT_dict.get)


