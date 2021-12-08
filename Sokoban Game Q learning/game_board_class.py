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
        # print("gg")
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
        return set(self.boxes) == self.storages

    def is_any_box_reach_end(self):
        return not self.storages.isdisjoint(self.boxes)

    def get_number_box_done(self):
        return len(self.storages.intersection(self.boxes))

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

    def BFS(self):
        """
        Returns all possible paths to location from player position
        :param board: Current game board state
        :return: all possible paths avoiding walls and other boxes
                    to box location
        """
        final_paths = []
        for box in self.boxes:
            queue = [[self.get_player()]]
            while queue:
                path = queue.pop()
                pos = path[-1]
                if pos == box:
                    final_paths.append(path)
                    continue
                goal = self.boxes.copy()
                goal.remove(box)
                for neighbor in [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]:
                    if not (neighbor[0] > self.rows or neighbor[1] > self.columns) and neighbor not in self.walls and neighbor not in goal and neighbor not in path:
                        new_path = list(path)
                        new_path.append(neighbor)
                        queue.append(new_path)
        results = dict()
        for path in final_paths:
            next = (path[-1][0], path[-1][1] + 1)
            if path[-2][0] - path[-1][0] == 1:
                next = (path[-1][0] - 1, path[-1][1])
            elif path[-2][0] - path[-1][0] == -1:
                next = (path[-1][0] + 1, path[-1][1])
            elif path[-2][1] - path[-1][1] == 1:
                next = (path[-1][0], path[-1][1] - 1)

            if not (next in self.walls or next in self.boxes or next in self.state_value_table):
                direction = 'R'
                if path[-2][0] - path[-1][0] == 1: direction = 'U'
                elif path[-2][0] - path[-1][0] == -1: direction = 'D'
                elif path[-2][1] - path[-1][1] == 1: direction = 'L'
                results[(path[-1], direction)] = path
        return results