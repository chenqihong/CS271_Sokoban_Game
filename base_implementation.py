"""
base_implementation.py: The base_implementation file of the project sokoban for CS271 for game board object only
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"


from constant_configuration import *
from game_board_class import *


def is_corner(current_coordinate, total_rows, total_columns, my_game_board_object):
    row_coordinate, column_coordinate = current_coordinate
    up_coordinate = row_coordinate -1, column_coordinate
    if row_coordinate + 1 <= total_rows:
        down_coordinate = row_coordinate + 1, column_coordinate
    else:
        down_coordinate = row_coordinate, column_coordinate
    left_coordinate = row_coordinate, column_coordinate - 1
    if column_coordinate + 1 <= total_columns:
        right_coordinate = row_coordinate, column_coordinate + 1
    else:
        right_coordinate = row_coordinate, column_coordinate
    if my_game_board_object.is_this_wall(left_coordinate[0], left_coordinate[1]) and my_game_board_object.is_this_wall(up_coordinate[0], up_coordinate[1]) and my_game_board_object.is_this_wall(right_coordinate[0], right_coordinate[1]):
        return True
    if my_game_board_object.is_this_wall(left_coordinate[0], left_coordinate[1]) and my_game_board_object.is_this_wall(right_coordinate[0], right_coordinate[1]) and my_game_board_object.is_this_wall(down_coordinate[0], down_coordinate[1]):
        return True
    if my_game_board_object.is_this_wall(left_coordinate[0], left_coordinate[1]) and my_game_board_object.is_this_wall(up_coordinate[0], up_coordinate[1]):
        return True
    if my_game_board_object.is_this_wall(right_coordinate[0], right_coordinate[1]) and my_game_board_object.is_this_wall(up_coordinate[0], up_coordinate[1]):
        return True

    if my_game_board_object.is_this_wall(left_coordinate[0], left_coordinate[1]) and my_game_board_object.is_this_wall(down_coordinate[0], down_coordinate[1]):
        return True
    if my_game_board_object.is_this_wall(right_coordinate[0],right_coordinate[1]) and my_game_board_object.is_this_wall(down_coordinate[0], down_coordinate[1]):
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


def is_influenced(non_mark_row, non_mark_column,total_rows, total_columns, my_game_board_object):
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
    print("up = ", up_coordinate, " left = ", left_coordinate, " down = ", down_coordinate, " right = ", right_coordinate)
    if (my_game_board_object.is_this_wall(up_coordinate[0], up_coordinate[1]) or state_value_table[up_coordinate] == -1) and (my_game_board_object.is_this_wall(left_coordinate[0], left_coordinate[1]) or state_value_table[left_coordinate] == -1):
        return True
    if (my_game_board_object.is_this_wall(up_coordinate[0], up_coordinate[1]) or state_value_table[
        up_coordinate] == -1) and (
            my_game_board_object.is_this_wall(right_coordinate[0], right_coordinate[1]) or state_value_table[
        right_coordinate] == -1):
        return True

    if (my_game_board_object.is_this_wall(down_coordinate[0], down_coordinate[1]) or state_value_table[down_coordinate] == -1) and (my_game_board_object.is_this_wall(left_coordinate[0], left_coordinate[1]) or state_value_table[left_coordinate] == -1):
        return True
    if (my_game_board_object.is_this_wall(down_coordinate[0], down_coordinate[1]) or state_value_table[
        down_coordinate] == -1) and (
            my_game_board_object.is_this_wall(right_coordinate[0], right_coordinate[1]) or state_value_table[
        right_coordinate] == -1):
        return True


def update_between_state_value_table(my_game_board_object):
    total_rows, total_columns = my_game_board_object.get_dimension()
    for current_row_count in range(1, total_rows+1):
        all_marked_row_block = get_all_marked_row_blocks(current_row_count)
        non_marked_row_blocks = find_all_nonmarked_row_blocks(all_marked_row_block, total_columns, current_row_count)
        print("for current row = ", current_row_count, " nonremarked row blocks = ", non_marked_row_blocks)
        for non_mark_row, non_mark_column in non_marked_row_blocks:
            if my_game_board_object.is_this_storage(non_mark_row, non_mark_column):
                continue
            if is_influenced(non_mark_row, non_mark_column,total_rows, total_columns, my_game_board_object):
                state_value_table[(non_mark_row, non_mark_column)] = -1



def update_corner_state_value_table(my_game_board_object: GameBoard):
    total_rows, total_columns = my_game_board_object.get_dimension()
    for current_row_count in range(1, total_rows+1):
        for current_column_count in range(1, total_columns+1):
            current_coordinate = (current_row_count, current_column_count)
            if my_game_board_object.is_this_wall(current_row_count, current_column_count):
                state_value_table[current_coordinate] = -1
            if is_corner(current_coordinate, total_rows, total_columns, my_game_board_object):
                if not my_game_board_object.is_this_storage(current_row_count, current_column_count):
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


def convert_to_coordinate_list(line_list: list) -> list:
    """
    Convert the given line to a list of tuples
    @param line_list: The list extracted from the line of input file
    @return: [(x_pos, y_pos), (x_pos1, y_pos1)]
    """
    coordinate_list = list()
    for i in range(0, len(line_list), 2):
        coordinate_list.append((line_list[i], line_list[i+1]))
    return coordinate_list


def extract_input_line(line: str, input_type: str) -> tuple:
    """
    Given a line in the input file, extract the info.
    @param line: The current line in input file
    @param input_type: The type for current line
    @return: game board information
    """
    line_list = line.split(" ")
    line_list = [int(x) for x in line_list]
    if input_type == "size_map":
        height, weight = line_list
        return int(height), int(weight)
    elif input_type == "wall_info":
        number_walls = line_list[0]
        all_walls_coordinates = convert_to_coordinate_list(line_list[1:])
        return number_walls, all_walls_coordinates
    elif input_type == "box_info":
        number_boxes = line_list[0]
        all_boxes_coordinates = convert_to_coordinate_list(line_list[1:])
        return number_boxes, all_boxes_coordinates
    elif input_type == "storage_info":
        number_storages = line_list[0]
        all_storages_coordinates = convert_to_coordinate_list(line_list[1:])
        return number_storages, all_storages_coordinates
    elif input_type == "player_pos":
        x_pos, y_pos = line_list
        return x_pos, y_pos
    else:
        return "Error", "Error"


def read_input(input_file_dir: str) -> GameBoard:
    """
    Read the input from the input file dir
    @param input_file_dir: the dir of the input file
    @return: GameBoard object
    """
    with open(input_file_dir, 'r') as f:
        for line_count, line in enumerate(f):
            input_type = input_conversion_dict[line_count]
            line = line.strip()
            if input_type == "size_map":
                board_dimension = extract_input_line(line, input_type)
            elif input_type == "wall_info":
                number_walls, wall_coordinate_list = extract_input_line(line, input_type)
            elif input_type == "box_info":
                number_boxes, boxes_coordinate_list = extract_input_line(line, input_type)
            elif input_type == "storage_info":
                number_storages, storage_coordinate_list = extract_input_line(line, input_type)
            elif input_type == "player_pos":
                player_coordinate = extract_input_line(line, input_type)
    my_game_board = GameBoard(board_dimension, number_walls, wall_coordinate_list, number_boxes, boxes_coordinate_list,
                              number_storages, storage_coordinate_list, player_coordinate)
    return my_game_board


def test_game(my_game_board: GameBoard) -> None:
    """Test Game with the command"""
    move_collections = ['None', 'L', 'U', 'U', 'U', 'U', 'R', 'U', 'U']
    for move in move_collections:
        my_game_board = make_move(move, my_game_board)



