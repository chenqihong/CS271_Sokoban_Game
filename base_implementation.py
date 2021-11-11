"""
base_implementation.py: The base_implementation file of the project sokoban for CS271
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"


from constant_configuration import *
from game_board_class import *


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



