"""
game_board_class.py: The GameBoard class file of the project sokoban for CS271
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"

class GameBoard:
    def __init__(self, board_dimension: tuple, wall_coordinate: set, box_coordinate: set, storage_coordinate: set, player_coordinate: tuple) -> None:



        self.height, self.weight = board_dimension
        self.wall_coordinate = wall_coordinate
        self.box_coordinate = box_coordinate
        self.storage_coordinate = storage_coordinate
        self.player_coordinate = player_coordinate
        self.recent_changed_box_coordinate = None

        self.wall_coordinate_copy = wall_coordinate.copy()
        self.box_coordinate_copy = box_coordinate.copy()
        self.storage_coordinate_copy = storage_coordinate.copy()
        self.player_coordinate_copy = player_coordinate

    def reset_board(self):
        self.box_coordinate = self.box_coordinate_copy.copy()
        self.wall_coordinate = self.wall_coordinate_copy.copy()
        self.storage_coordinate = self.storage_coordinate_copy.copy()
        self.player_coordinate = self.player_coordinate_copy

    def get_dimension(self):
        return self.height, self.weight

    def is_this_wall(self, coordinate_x: int, coordinate_y: int) -> bool:
        return (coordinate_x, coordinate_y) in self.wall_coordinate

    def is_this_box(self, coordinate_x: int, coordinate_y: int) -> bool:
        return (coordinate_x, coordinate_y) in self.box_coordinate

    def is_this_storage(self, coordinate: tuple) -> bool:
        return coordinate in self.storage_coordinate

    def get_current_player_coordinate(self) -> tuple:
        return self.player_coordinate

    def update_current_player_coordinate(self, move: str) -> None:
        if move == 'U':
            self.player_x_coordinate -= 1
        elif move == 'D':
            self.player_x_coordinate += 1
        elif move == "L":
            self.player_y_coordinate -= 1
        elif move == 'R':
            self.player_y_coordinate += 1
        if (self.player_x_coordinate, self.player_y_coordinate) in self.box_coordinate:
            self.update_box_coordinate(move, self.player_x_coordinate, self.player_y_coordinate)

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
        self.recent_changed_box_coordinate = new_box_coordinate
        self.box_coordinate.remove(old_box_coordinate)
        self.box_coordinate.add(new_box_coordinate)

    def is_end_game(self):
        # print("self.box_coordinate_list = ", self.box_coordinate_list)
        # print("self.storage_coordinate_list = ", self.storage_coordinate_list)
        return self.box_coordinate == self.storage_coordinate

    def is_box_reach_storage(self, box_coordinate_x, box_coordinate_y):
        return (box_coordinate_x, box_coordinate_y) in self.storage_coordinate_list

    def wall_boundary_check(self, up_coordinate: tuple, down_coordinate: tuple, left_coordinate: tuple,
                            right_coordinate: tuple) -> set:
        removal_move_set = set()
        if up_coordinate in self.wall_coordinate_list:
            removal_move_set.add("U")
        if down_coordinate in self.wall_coordinate_list:
            removal_move_set.add('D')
        if left_coordinate in self.wall_coordinate_list:
            removal_move_set.add("L")
        if right_coordinate in self.wall_coordinate_list:
            removal_move_set.add("R")
        return removal_move_set

    def is_surrounded_by_wall(self, box_new_coordinate: tuple):
        box_left_coordinate = box_new_coordinate[0], box_new_coordinate[1] - 1
        box_right_coordinate = box_new_coordinate[0], box_new_coordinate[1] + 1
        box_up_coordinate = box_new_coordinate[0] - 1, box_new_coordinate[1]
        box_down_coordinate = box_new_coordinate[0] + 1, box_new_coordinate[1]
        if box_up_coordinate in self.wall_coordinate_list and box_left_coordinate in self.wall_coordinate_list:
            return True
        if box_up_coordinate in self.wall_coordinate_list and box_right_coordinate in self.wall_coordinate_list:
            return True
        if box_down_coordinate in self.wall_coordinate_list and box_left_coordinate in self.wall_coordinate_list:
            return True
        if box_down_coordinate in self.wall_coordinate_list and box_right_coordinate in self.wall_coordinate_list:
            return True

    def box_stuck_check(self, up_coordinate: tuple, down_coordinate: tuple, left_coordinate: tuple,
                        right_coordinate: tuple, possible_moves_set: set) -> set:
        removal_move_set = set()
        if up_coordinate in self.box_coordinate_list and 'U' in possible_moves_set:
            up_coordinate_x, up_coordinate_y = up_coordinate
            up_up_coordinate = up_coordinate_x - 1, up_coordinate_y
            if up_up_coordinate in self.wall_coordinate_list:  # 抵着墙
                removal_move_set.add("U")
            if self.is_surrounded_by_wall(up_up_coordinate):  # 被墙包围了
                removal_move_set.add("U")
        if down_coordinate in self.box_coordinate_list and 'D' in possible_moves_set:
            down_coordinate_x, down_coordinate_y = down_coordinate
            down_down_coordinate = down_coordinate_x + 1, down_coordinate_y
            if down_down_coordinate in self.wall_coordinate_list:  # 抵着墙
                removal_move_set.add("D")
            if self.is_surrounded_by_wall(down_down_coordinate):  # 被墙包围了
                removal_move_set.add("D")
        if left_coordinate in self.box_coordinate_list and 'L' in possible_moves_set:
            left_coordinate_x, left_coordinate_y = left_coordinate
            left_left_coordinate = left_coordinate_x, left_coordinate_y - 1
            if left_left_coordinate in self.wall_coordinate_list:  # 抵着墙
                removal_move_set.add("L")
            if self.is_surrounded_by_wall(left_left_coordinate):  # 被墙包围了
                removal_move_set.add("L")
        if right_coordinate in self.box_coordinate_list and 'R' in possible_moves_set:
            right_coordinate_x, right_coordinate_y = right_coordinate
            right_right_coordinate = right_coordinate_x, right_coordinate_y + 1
            if right_right_coordinate in self.wall_coordinate_list:  # 抵着墙
                removal_move_set.add("R")
            if self.is_surrounded_by_wall(right_right_coordinate):  # 被墙包围了
                removal_move_set.add("R")
        return removal_move_set

    def get_all_possible_moves(self, player_coordinate_x: int, player_coordinate_y: int) -> list:
        possible_moves_set = {'U', 'D', 'L', 'R'}
        up_coordinate = player_coordinate_x - 1, player_coordinate_y
        down_coordinate = player_coordinate_x + 1, player_coordinate_y
        left_coordinate = player_coordinate_x, player_coordinate_y - 1
        right_coordinate = player_coordinate_x, player_coordinate_y + 1
        removal_move_set = self.wall_boundary_check(up_coordinate, down_coordinate, left_coordinate, right_coordinate)
        possible_moves_set = possible_moves_set.difference(removal_move_set)
        removal_move_set = self.box_stuck_check(up_coordinate, down_coordinate, left_coordinate, right_coordinate,
                                                possible_moves_set)
        possible_moves_set = possible_moves_set.difference(removal_move_set)
        return list(possible_moves_set)

    def get_all_boxes_position(self):
        return self.box_coordinate

    def get_recent_changed_box_coordinate(self):
        return self.recent_changed_box_coordinate

    def show_board(self):
        print()
        for i in self.board:
            for j in i:
                print(j, end=" ")
            print()

    def teleportation(self, x_coordinate, y_coordinate):
        self.player_x_coordinate = x_coordinate
        self.player_y_coordinate = y_coordinate

    def is_any_box_reach_end(self):
        return any(x in self.storage_coordinate for x in self.box_coordinate)

    def get_number_box_done(self):
        count = 0
        for box_coordinate in self.box_coordinate:
            if box_coordinate in self.storage_coordinate:
                count += 1
        return count