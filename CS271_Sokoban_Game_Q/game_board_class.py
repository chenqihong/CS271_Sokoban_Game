"""
game_board_class.py: The GameBoard class file of the project sokoban for CS271
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"


class GameBoard:
    def __init__(self, board_dimension: tuple, num_wall: int, wall_coordinate: list, num_box: int, box_coordinate: list,
                 num_storage: int, storage_coordinate: list, agent_coordinate: tuple) -> None:

        self.rows, self.columns = board_dimension
        self.number_walls = num_wall
        self.wall_coordinate_list = wall_coordinate
        self.wall_coordinate_list_copy = tuple(wall_coordinate)

        self.number_boxes = num_box
        self.box_coordinate_list = box_coordinate
        self.box_coordinate_list_copy = tuple(box_coordinate)

        self.number_storages = num_storage
        self.storage_coordinate_list = storage_coordinate
        self.storage_coordinate_list_copy = tuple(storage_coordinate)

        self.player_row_coordinate, self.player_column_coordinate = agent_coordinate
        self.player_row_coordinate_copy, self.player_column_coordinate_copy = agent_coordinate
        self.state_value_table = set()
        self.box_state_value_table = set()
        self.update_state_value_table()
        self.box_state_value_table = set()

    def get_dimension(self):
        return self.rows, self.columns

    def reset_board(self):
        self.box_coordinate_list = list(self.box_coordinate_list_copy)
        self.wall_coordinate_list = list(self.wall_coordinate_list_copy)
        self.storage_coordinate_list = list(self.storage_coordinate_list_copy)
        self.player_row_coordinate, self.player_column_coordinate = self.player_row_coordinate_copy, self.player_column_coordinate_copy

    def is_wall(self, coordinate: tuple) -> bool:
        return coordinate in self.wall_coordinate_list

    def is_box(self, coordinate: tuple) -> bool:
        return coordinate in self.box_coordinate_list

    def is_storage(self, coordinate: tuple) -> bool:
        return coordinate in self.storage_coordinate_list

    def get_current_player_coordinate(self) -> tuple:
        return self.player_row_coordinate, self.player_column_coordinate

    def update_current_player_coordinate(self, move: str) -> None:
        if move == 'U':
            self.player_row_coordinate -= 1
        elif move == 'D':
            self.player_row_coordinate += 1
        elif move == "L":
            self.player_column_coordinate -= 1
        elif move == 'R':
            self.player_column_coordinate += 1
        if (self.player_row_coordinate, self.player_column_coordinate) in self.box_coordinate_list:
            self.update_box_coordinate(move, self.player_row_coordinate, self.player_column_coordinate)

    def update_box_coordinate(self, box_move_dir: str, box_current_coordinate_x: int,
                              box_current_coordinate_y: int) -> None:
        old_box_coordinate = (box_current_coordinate_x, box_current_coordinate_y)
        if box_move_dir == 'U':
            box_current_coordinate_x -= 1
        elif box_move_dir == 'D':
            box_current_coordinate_x += 1
        elif box_move_dir == "L":
            box_current_coordinate_y -= 1
        elif box_move_dir == 'R':
            box_current_coordinate_y += 1
        new_box_coordinate = (box_current_coordinate_x, box_current_coordinate_y)
        self.box_coordinate_list.remove(old_box_coordinate)
        self.box_coordinate_list.append(new_box_coordinate)

    def is_end_game(self):
        return sorted(self.box_coordinate_list) == sorted(self.storage_coordinate_list)

    def is_box_reach_storage(self, box_coordinate_x, box_coordinate_y):
        return (box_coordinate_x, box_coordinate_y) in self.storage_coordinate_list

    def teleportation(self, x_coordinate, y_coordinate):
        self.player_row_coordinate = x_coordinate
        self.player_column_coordinate = y_coordinate

    def is_any_box_reach_end(self):
        return any(x in self.storage_coordinate_list for x in self.box_coordinate_list)

    def get_number_box_done(self):
        count = 0
        for box_coordinate in self.box_coordinate_list:
            if box_coordinate in self.storage_coordinate_list:
                count += 1
        return count

    def get_all_boxes_position(self):
        return self.box_coordinate_list

    def update_state_value_table(self):
        for row in range(1, self.rows + 1):
            for col in range(1, self.columns + 1):
                if not self.is_storage((row, col)) and (self.is_wall((row, col)) or (
                        (self.is_wall((row + 1, col)) and self.is_wall((row, col + 1))) or (
                        self.is_wall((row + 1, col)) and self.is_wall((row, col - 1))) or (
                                self.is_wall((row - 1, col)) and self.is_wall((row, col + 1))) or (
                                self.is_wall((row - 1, col)) and self.is_wall((row, col - 1))))):
                    self.state_value_table.add((row, col))
        for row in range(1, self.rows + 1):
            for col in range(1, self.columns + 1):
                if not self.is_storage((row, col)) and (
                        ((row, col + 1) in self.state_value_table) + ((row, col - 1) in self.state_value_table) + (
                        (row + 1, col) in self.state_value_table) + ((row - 1, col) in self.state_value_table)) > 2:
                    self.state_value_table.add((row, col))

    def update_box_state_value_table(self):
        self.box_state_value_table = set()
        temp_table = self.state_value_table | set(self.box_coordinate_list)
        for row in range(1, self.rows + 1):
            for col in range(1, self.columns + 1):
                if not self.is_storage((row, col)) and (
                        ((row, col + 1) in temp_table) + ((row, col - 1) in temp_table) +
                        ((row + 1, col) in temp_table) + ((row - 1, col) in temp_table)) == 4:
                    self.box_state_value_table.add((row, col))
        return self.box_state_value_table
