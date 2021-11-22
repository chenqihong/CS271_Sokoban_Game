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
from evaluate_module import evaluate


def main(my_game_board: GameBoard) -> None:
    """
    The main program of the game
    @param my_game_board: The game board object
    @return: None
    """
    global BaseEpsilon, simulation_choices_list
    start = time.time()
    for current_training_times in range(TotalTrainingTimes):
        print("Doing iteration: ", current_training_times)
        BaseEpsilon -= 0.001 * current_training_times
        start_simulation(my_game_board)
        update_UTC_table()
        simulation_choices_list = list()
        my_game_board = read_input(input_str)

    print("All Training Are Done")
    file_to_write = open(UCTSaveDir, 'wb')
    pickle.dump(UCT_table, file_to_write)
    print("Done saving the UCT table to file")
    end = time.time()
    print("Running Time: ", end-start)


if __name__ == '__main__':
    input_str = "sokoban01.txt"
    board = read_input(input_str)
    update_corner_state_value_table(board)
    main(board)

    print("UTC_Table = ", dict(UCT_table))
    board = read_input(input_str)
    print("Start evaluating")
    evaluation_result = evaluate(board)
    print("Result: ", evaluation_result)
