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


def main(my_game_board: GameBoard):
    global picked_box_action_list
    start = time()
    for current_training_time in range(TotalTrainingTimes):
        print("Doing iteration: ", current_training_time)
        BaseEpsilon = 1 - 0.0001 * current_training_time
        training(my_game_board, BaseEpsilon)
        my_game_board.reset_board()
    end = time()
    print("Training total times: ", end - start)


if __name__ == '__main__':
    input_str = "sokoban02.txt"
    board = read_input(input_str)
    update_state_value_table(board)
    main(board)

    board.reset_board()
    if evaluate(board):
        print("Success ")
    else:
        print("Fail ")

