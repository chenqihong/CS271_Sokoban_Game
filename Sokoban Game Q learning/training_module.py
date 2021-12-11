from base_implementation import *
from random import choice, random


def training(board, BaseEpsilon: float) -> None:
    """
    This function performances the training
    :param my_game_board:
    :param BaseEpsilon:
    :return:
    """
    total_number_boxes_done = 0
    picked_box_action_list = []
    repeated_action_list = []
    all_bfs_path = board.BFS()
    all_selections = list(all_bfs_path.keys())
    # from gui import Graph
    # g = Graph(my_game_board)
    for i in range(TotalStepSize):
        # g.update()
        current_state = board.get_state()

        if not all_selections:
            return
        if len(all_selections) > 1:
            if decide_policy(BaseEpsilon, current_state):
                selected_box, action = greedy_choice(current_state, all_selections)
            else:
                max_val = 0
                result_max = []
                result_all = []
                for selection in all_selections:
                    score = simulate(board, selection, step_size)
                    if score > max_val:
                        result_max = [selection]
                        max_val = score
                    elif score == max_val:
                        result_max.append(selection)
                    result_all.append(selection)
                if random() > 0.2:
                    selected_box, action = choice(result_max)
                else:
                    selected_box, action = choice(result_all)
        else:
            selected_box, action = all_selections[0]
        board.move_player(*all_bfs_path[(selected_box, action)][-2])
        board.update_player(action)
        next_state = board.get_state()
        state = board.get_state()
        if state in bfs_dict:
            all_bfs_path = bfs_dict[state]
        else:
            all_bfs_path = board.BFS()
        bfs_dict[state] = all_bfs_path
        all_selections = list(all_bfs_path.keys())
        reward, total_number_boxes_done = calculate_reward(board, picked_box_action_list,
                                                           selected_box, action, all_selections,
                                                           total_number_boxes_done)
        picked_box_action_list.append((selected_box, action))
        if len(repeated_action_list) == 2:
            first_box, second_box = repeated_action_list
            if first_box in board.storages and second_box not in board.storages and selected_box == first_box:
                reward = -300
            if first_box not in board.storages and second_box in board.storages and selected_box == first_box:
                reward = -300
            repeated_action_list = list()
        else:
            repeated_action_list.append(selected_box)
        update_Q_Value(current_state, selected_box, action, reward, next_state)
