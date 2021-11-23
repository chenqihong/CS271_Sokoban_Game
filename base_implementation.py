"""
base_implementation.py: The base_implementation file of the project sokoban for CS271 for game board object only
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"

from constant_configuration import *
from game_board_class import *


def is_corner(current_coordinate, total_rows, total_columns, my_game_board_object):
    row_coordinate, column_coordinate = current_coordinate
    up_coordinate = row_coordinate - 1, column_coordinate
    if row_coordinate + 1 <= total_rows:
        down_coordinate = row_coordinate + 1, column_coordinate
    else:
        down_coordinate = row_coordinate, column_coordinate
    left_coordinate = row_coordinate, column_coordinate - 1
    if column_coordinate + 1 <= total_columns:
        right_coordinate = row_coordinate, column_coordinate + 1
    else:
        right_coordinate = row_coordinate, column_coordinate
    if my_game_board_object.is_this_wall(left_coordinate[0], left_coordinate[1]) and my_game_board_object.is_this_wall(
            up_coordinate[0], up_coordinate[1]) and my_game_board_object.is_this_wall(right_coordinate[0],
                                                                                      right_coordinate[1]):
        return True
    if my_game_board_object.is_this_wall(left_coordinate[0], left_coordinate[1]) and my_game_board_object.is_this_wall(
            right_coordinate[0], right_coordinate[1]) and my_game_board_object.is_this_wall(down_coordinate[0],
                                                                                            down_coordinate[1]):
        return True
    if my_game_board_object.is_this_wall(left_coordinate[0], left_coordinate[1]) and my_game_board_object.is_this_wall(
            up_coordinate[0], up_coordinate[1]):
        return True
    if my_game_board_object.is_this_wall(right_coordinate[0],
                                         right_coordinate[1]) and my_game_board_object.is_this_wall(up_coordinate[0],
                                                                                                    up_coordinate[1]):
        return True

    if my_game_board_object.is_this_wall(left_coordinate[0], left_coordinate[1]) and my_game_board_object.is_this_wall(
            down_coordinate[0], down_coordinate[1]):
        return True
    if my_game_board_object.is_this_wall(right_coordinate[0],
                                         right_coordinate[1]) and my_game_board_object.is_this_wall(down_coordinate[0],
                                                                                                    down_coordinate[1]):
        return True
    return False


def get_all_marked_row_blocks(current_row_count):
    all_marked_row_blocks = list()
    for key in state_value_table:
        if key[0] == current_row_count:
            all_marked_row_blocks.append(key)
    return all_marked_row_blocks


def find_all_nonmarked_row_blocks(all_marked_row_block, total_columns, current_row):
    nonmarked_row_blocks = list()
    for current_column in range(1, total_columns + 1):
        if (current_row, current_column) not in all_marked_row_block:
            nonmarked_row_blocks.append((current_row, current_column))
    return nonmarked_row_blocks


def is_influenced(non_mark_row, non_mark_column, total_rows, total_columns, my_game_board_object):
    print("non_mark_row, non_mark_column = ", non_mark_row, non_mark_column)
    if non_mark_row + 1 <= total_rows:
        down_coordinate = non_mark_row + 1, non_mark_column
    else:
        down_coordinate = non_mark_row, non_mark_column
    up_coordinate = non_mark_row - 1, non_mark_column

    if non_mark_column + 1 <= total_columns:
        right_coordinate = non_mark_row, non_mark_column + 1
    else:
        right_coordinate = non_mark_row, non_mark_column
    left_coordinate = non_mark_row, non_mark_column - 1
    print("up = ", up_coordinate, " left = ", left_coordinate, " down = ", down_coordinate, " right = ",
          right_coordinate)
    if (my_game_board_object.is_this_wall(up_coordinate[0], up_coordinate[1]) or state_value_table[
        up_coordinate] == -1) and (
            my_game_board_object.is_this_wall(left_coordinate[0], left_coordinate[1]) or state_value_table[
        left_coordinate] == -1):
        return True
    if (my_game_board_object.is_this_wall(up_coordinate[0], up_coordinate[1]) or state_value_table[
        up_coordinate] == -1) and (
            my_game_board_object.is_this_wall(right_coordinate[0], right_coordinate[1]) or state_value_table[
        right_coordinate] == -1):
        return True

    if (my_game_board_object.is_this_wall(down_coordinate[0], down_coordinate[1]) or state_value_table[
        down_coordinate] == -1) and (
            my_game_board_object.is_this_wall(left_coordinate[0], left_coordinate[1]) or state_value_table[
        left_coordinate] == -1):
        return True
    if (my_game_board_object.is_this_wall(down_coordinate[0], down_coordinate[1]) or state_value_table[
        down_coordinate] == -1) and (
            my_game_board_object.is_this_wall(right_coordinate[0], right_coordinate[1]) or state_value_table[
        right_coordinate] == -1):
        return True


def update_between_state_value_table(my_game_board_object):
    total_rows, total_columns = my_game_board_object.get_dimension()
    for current_row_count in range(1, total_rows + 1):
        all_marked_row_block = get_all_marked_row_blocks(current_row_count)
        non_marked_row_blocks = find_all_nonmarked_row_blocks(all_marked_row_block, total_columns, current_row_count)
        print("for current row = ", current_row_count, " nonremarked row blocks = ", non_marked_row_blocks)
        for non_mark_row, non_mark_column in non_marked_row_blocks:
            if my_game_board_object.is_this_storage(non_mark_row, non_mark_column):
                continue
            if is_influenced(non_mark_row, non_mark_column, total_rows, total_columns, my_game_board_object):
                state_value_table[(non_mark_row, non_mark_column)] = -1


def update_corner_state_value_table(my_game_board_object: GameBoard):
    total_rows, total_columns = my_game_board_object.get_dimension()
    for current_row_count in range(1, total_rows + 1):
        for current_column_count in range(1, total_columns + 1):
            current_coordinate = (current_row_count, current_column_count)
            if my_game_board_object.is_this_wall(current_row_count, current_column_count):
                state_value_table[current_coordinate] = -1
            if is_corner(current_coordinate, total_rows, total_columns, my_game_board_object):
                if not my_game_board_object.is_this_storage(current_coordinate):
                    state_value_table[current_coordinate] = -1


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
            wall_coordinate.add((int(walls[i + 1]), int(walls[i])))

        for i in range(1, int(boxes[0]) * 2, 2):
            boxes_coordinate.add((int(boxes[i + 1]), int(boxes[i])))

        for i in range(1, int(storages[0]) * 2, 2):
            storage_coordinate.add((int(storages[i + 1]), int(storages[i])))

        player_coordinate = tuple([int(x) for x in f.readline().split(" ")])
    board = GameBoard(board_dimension, wall_coordinate, boxes_coordinate, storage_coordinate, player_coordinate)
    return board
