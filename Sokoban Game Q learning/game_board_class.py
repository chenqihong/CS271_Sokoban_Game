class GameBoard:
    def __init__(self, board_dimension: tuple, wall_coordinate: frozenset, box_coordinate: set,
                 storage_coordinate: frozenset, player_coordinate: tuple) -> None:

        self.rows, self.columns = board_dimension
        self.walls = wall_coordinate
        self.boxes = list(box_coordinate)
        self.storages = storage_coordinate
        self.player_row, self.player_col = player_coordinate
        self.state_value_table = self.make_state_value_table()

    def get_player(self) -> tuple:
        return self.player_row, self.player_col

    def move_player(self, x, y):
        self.player_row, self.player_col = x, y

    def update_player(self, move: str) -> None:
        if move == 'U':
            self.player_row -= 1
        elif move == 'D':
            self.player_row += 1
        elif move == "L":
            self.player_col -= 1
        elif move == 'R':
            self.player_col += 1
        if self.get_player() in self.boxes:
            self.update_box(move)

    def update_box(self, box_move_dir: str) -> None:
        box_x, box_y = self.get_player()
        if box_move_dir == 'U':
            box_x -= 1
        elif box_move_dir == 'D':
            box_x += 1
        elif box_move_dir == "L":
            box_y -= 1
        elif box_move_dir == 'R':
            box_y += 1
        self.boxes.remove(self.get_player())
        self.boxes.append((box_x, box_y))

    def is_end_game(self):
        return sorted(self.boxes) == sorted(self.storages)

    def is_box_reach_storage(self, box_coordinate_x, box_coordinate_y):
        return (box_coordinate_x, box_coordinate_y) in self.storages



    def is_any_box_reach_end(self):
        return any(x in self.storages for x in self.boxes)

    def get_number_box_done(self):
        count = 0
        for box_coordinate in self.boxes:
            if box_coordinate in self.storages:
                count += 1
        return count

    def make_state_value_table(self):
        state_value_table = set()
        for row in range(1, self.rows + 1):
            for col in range(1, self.columns + 1):
                if (row, col) not in self.storages and ((row, col) in self.walls or (
                        ((row + 1, col) in self.walls and (row, col + 1) in self.walls) or (
                        (row + 1, col) in self.walls and (row, col - 1) in self.walls) or (
                                (row - 1, col) in self.walls and (row, col + 1) in self.walls) or (
                                (row - 1, col) in self.walls and (row, col - 1) in self.walls))):
                    state_value_table.add((row, col))
        for row in range(1, self.rows + 1):
            for col in range(1, self.columns + 1):
                if (row, col) not in self.storages and (
                        ((row, col + 1) in state_value_table) + ((row, col - 1) in state_value_table) + (
                        (row + 1, col) in state_value_table) + ((row - 1, col) in state_value_table)) > 2:
                    state_value_table.add((row, col))
        return state_value_table
