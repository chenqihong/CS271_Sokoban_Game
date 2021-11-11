"""
main.py: The main file of the project sokoban for CS271
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"

from constant_configuration import *
from base_implementation import *
from game_board_class import *


def test_game(my_game_board: GameBoard) -> None:
    """Test Game with the command"""
    move_collections = ['None', 'U', 'L', 'L', 'L']
    for move in move_collections:
        my_game_board = make_move(move, my_game_board)


if __name__ == '__main__':
    input_str = "sokoban01.txt"
    my_game_board_object = read_input(input_str)
    test_game(my_game_board_object)
