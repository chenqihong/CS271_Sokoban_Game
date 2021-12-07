from base_implementation import *
from pathfinding import *


def evaluate(my_game_board):
    for i in range(1000):
        all_bfs_path = bfs(my_game_board)  # get all paths
        print("all bfs path = ", all_bfs_path)
        current_state = str(my_game_board.get_player()) + str(my_game_board.boxes)
        all_box_choices = list(all_bfs_path.keys())
        if not all_box_choices:
            return False

        selected_box_coordinate, action = get_greedy_choice(current_state, all_box_choices)
        print("choosing box coordinate = ", selected_box_coordinate, " action = ", action)
        next_to_board_coordinate_x, next_to_board_coordinate_y = all_bfs_path[(selected_box_coordinate, action)][-2]
        my_game_board.move_player(next_to_board_coordinate_x, next_to_board_coordinate_y)
        my_game_board.update_player(action)
        if my_game_board.is_end_game():
            return True
    return False
