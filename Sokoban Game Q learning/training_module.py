from pathfinding import *
from base_implementation import *
from random import choice


def training(my_game_board: GameBoard, BaseEpsilon: float) -> None:
    """
    This function performances the training
    :param my_game_board:
    :param BaseEpsilon:
    :return:
    """
    total_number_boxes_done = 0
    picked_box_action_list = []
    all_bfs_path = bfs(my_game_board)
    all_selections = list(all_bfs_path.keys())
    # from gui import Graph
    # g = Graph(my_game_board)
    for current_step in range(TotalStepSize):
        # g.update()
        box_position = list(tuple(my_game_board.boxes))
        current_state = str(my_game_board.get_player()) + str(box_position)
        if not all_selections:
            return
        policy = decide_policy(BaseEpsilon, current_state)  # 0 = random, 1 = greedy
        if policy:
            selected_box_coordinate, action = get_greedy_choice(current_state, all_selections)
        else:
            selected_box_coordinate, action = choice(all_selections)

        next_to_board_coordinate_x, next_to_board_coordinate_y = all_bfs_path[(selected_box_coordinate, action)][-2]
        my_game_board.move_player(next_to_board_coordinate_x, next_to_board_coordinate_y)
        my_game_board.update_player(action)
        next_state = str(my_game_board.get_player()) + str(my_game_board.boxes)

        all_bfs_path = bfs(my_game_board)
        all_selections = list(all_bfs_path.keys())
        reward, total_number_boxes_done = calculate_reward(my_game_board, picked_box_action_list,
                                                           selected_box_coordinate, action, all_selections,
                                                           total_number_boxes_done)
        picked_box_action_list.append((selected_box_coordinate, action))
        update_Q_Value(current_state, selected_box_coordinate, action, reward, next_state)
