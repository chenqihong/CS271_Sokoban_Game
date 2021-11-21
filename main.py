"""
main.py: The main file of the project sokoban for CS271
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"

from constant_configuration import *
from base_implementation import *
from game_board_class import *
from pathfinding import *
from start_simulation_module import start_simulation
from base_implementation_v2 import *


def main(my_game_board: GameBoard) -> None:
    """
    The main program of the game
    @param my_game_board: The game board object
    @return: None
    """
    global BaseEpsilon, simulation_choices_list
    for current_training_times in range(TotalTrainingTimes):
        BaseEpsilon -= 0.1 * current_training_times
        simulation_result = start_simulation(my_game_board)
        update_UTC_table(simulation_result)
        simulation_choices_list = list()
        my_game_board = read_input(input_str)

    print("All Training Are Done")
    file_to_write = open(UCTSaveDir, 'wb')
    pickle.dump(UCT_table, file_to_write)
    print("Done saving the UCT table to file")


if __name__ == '__main__':
    input_str = "sokoban01.txt"
    board = read_input(input_str)
    main(board)

