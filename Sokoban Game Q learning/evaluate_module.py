from base_implementation import *


def evaluate(board):
    for i in range(1000):
        all_bfs_path = board.BFS()
        print("all bfs path = ", all_bfs_path)
        current_state = str(board.get_player()) + str(board.boxes)
        all_box_choices = list(all_bfs_path.keys())
        if not all_box_choices:
            return False

        selected_box, action = greedy_choice(current_state, all_box_choices)
        print("choosing box coordinate = ", selected_box, " action = ", action)
        board.move_player(*all_bfs_path[(selected_box, action)][-2])
        board.update_player(action)
        if board.is_end_game():
            return True
    return False