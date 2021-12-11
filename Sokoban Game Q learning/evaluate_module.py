from base_implementation import *


def evaluate(board):
    for i in range(1000):
        if board.is_end_game():
            return True
        all_bfs_path = board.BFS()
        all_box_choices = list(all_bfs_path.keys())
        if not all_box_choices:
            return False

        selected_box, action = greedy_choice(board.get_state(), all_box_choices)
        print("choosing box coordinate = ", selected_box, " action = ", action)
        board.move_player(*all_bfs_path[(selected_box, action)][-2])
        board.update_player(action)
        if board.is_end_game():
            return True
    return False
