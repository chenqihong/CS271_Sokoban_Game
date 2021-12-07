"""
main.py: The main file of the project sokoban for CS271
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban project Q learning version"

import time

from base_implementation import *
from game_board_class import *
from pathfinding import *
from training_module import training
from evaluate_module import evaluate
from constant_configuration import *
from tqdm import tqdm


def main(my_game_board: GameBoard):
    global picked_box_action_list
    for current_training_time in tqdm(range(TotalTrainingTimes)):
        BaseEpsilon = 1 - 0.0001 * current_training_time
        training(my_game_board, BaseEpsilon)
        my_game_board.reset_board()


if __name__ == '__main__':
    input_str = "sokoban02.txt"
    board = read_input(input_str)
    main(board)

    board.reset_board()
    if evaluate(board):
        print("Success")
    else:
        print("Fail")

