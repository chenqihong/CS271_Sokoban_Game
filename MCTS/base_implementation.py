"""
base_implementation.py: The base_implementation file of the project sokoban for CS271 for game board object only
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"

from constant_configuration import *
from game_board_class import *

def update_state_value_table(board: GameBoard):
    total_rows, total_columns = board.get_dimension()
    for row in range(1, total_rows + 1):
        for col in range(1, total_columns + 1):
            if not board.is_storage(row, col) and (board.is_wall(row, col) or ((board.is_wall(row+1,col) and board.is_wall(row,col+1)) or (board.is_wall(row+1,col) and board.is_wall(row,col-1)) or (board.is_wall(row-1,col) and board.is_wall(row,col+1)) or (board.is_wall(row-1,col) and board.is_wall(row,col-1)))):
                state_value_table.add((row, col))
    for row in range(1, total_rows + 1):
        for col in range(1, total_columns + 1):
            if not board.is_storage(row, col) and (((row,col+1) in state_value_table) + ((row,col-1) in state_value_table)+((row+1,col) in state_value_table)+((row-1,col) in state_value_table)) > 2:
                state_value_table.add((row, col))
    return state_value_table

def make_move(command: str, my_game_board: GameBoard) -> GameBoard:
    """
    Make the move based on the given command
    @param command: legal moves such as up, down, left right
    @param my_game_board: the game board object
    @return: the updated game board
    """
    if command in ALL_LEGAL_MOVES:
        my_game_board.update_current_player_coordinate(command)
    print("<==============================================>")
    current_player_coordinate = my_game_board.get_current_player_coordinate()
    print("current agent coordinate = ", current_player_coordinate)
    possible_moves = my_game_board.get_all_possible_moves(current_player_coordinate[0], current_player_coordinate[1])
    print("possible moves: ", possible_moves)
    print("boxes pos newly affected = ", my_game_board.get_recent_changed_box_coordinate())
    return my_game_board


def read_input(input_file_dir: str) -> GameBoard:
    """
    Read the input from the input file dir
    @param input_file_dir: the dir of the input file
    @return: GameBoard object
    """
    with open(input_file_dir, 'r') as f:
        board_dimension = tuple([int(x) for x in f.readline().split(" ")])
        walls = f.readline().split()
        boxes = f.readline().split()
        storages = f.readline().split()
        wall_coordinate = set()
        boxes_coordinate = set()
        storage_coordinate = set()
        for i in range(1, int(walls[0]) * 2, 2):
            wall_coordinate.add((int(walls[i]), int(walls[i+1])))

        for i in range(1, int(boxes[0]) * 2, 2):
            boxes_coordinate.add((int(boxes[i]), int(boxes[i+1])))

        for i in range(1, int(storages[0]) * 2, 2):
            storage_coordinate.add((int(storages[i]), int(storages[i+1])))

        player_coordinate = tuple([int(x) for x in f.readline().split(" ")])

    board = GameBoard(board_dimension, wall_coordinate, boxes_coordinate, storage_coordinate, player_coordinate)
    return board
