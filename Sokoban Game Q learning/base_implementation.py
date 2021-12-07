from constant_configuration import *
from game_board_class import *
from random import random


def read_input(input_file_dir: str) -> GameBoard:
    """
    Read the input from the input file dir
    @param input_file_dir: the dir of the input file
    @return: GameBoard object
    """
    with open(input_file_dir, 'r') as f:
        board_dimension = tuple([int(x) for x in f.readline().split(" ")])
        walls = f.readline().split()
        boxes = f.readline().split()
        storages = f.readline().split()
        wall_coordinate = set()
        boxes_coordinate = set()
        storage_coordinate = set()
        for i in range(1, int(walls[0]) * 2, 2):
            wall_coordinate.add((int(walls[i]), int(walls[i + 1])))

        for i in range(1, int(boxes[0]) * 2, 2):
            boxes_coordinate.add((int(boxes[i]), int(boxes[i + 1])))

        for i in range(1, int(storages[0]) * 2, 2):
            storage_coordinate.add((int(storages[i]), int(storages[i + 1])))

        player_coordinate = tuple([int(x) for x in f.readline().split(" ")])

    board = GameBoard(board_dimension, frozenset(wall_coordinate), boxes_coordinate, frozenset(storage_coordinate),
                      player_coordinate)
    return board


def decide_policy(BaseEpsilon: float, current_state) -> int:
    """
    Determines the policy: random or greedy
    @param BaseEpsilon: used to determine which policy to go for.
    @return: 0 if random, 1 if greedy
    """
    if current_state not in Q_table:
        return 0
    # All boxes have some Q values
    random_val = random()
    if BaseEpsilon > random_val:
        return 0
    return 1


def get_greedy_choice(current_state: str, all_reachable_boxes: list) -> tuple:
    """
    This function finds the greedy choice of the box
    @param current_state:
    @param all_reachable_boxes: (2,3)
    @return: ((x,y), U)
    """
    temp_dict = defaultdict(float)
    for reachable_box, action in all_reachable_boxes:
        if (reachable_box, action) in Q_table[current_state]:
            temp_dict[(reachable_box, action)] = Q_table[current_state][(reachable_box, action)]
    return max(temp_dict, key=temp_dict.get)


def update_Q_Value(current_state, selected_box_coordinate, action, reward, next_state):
    Q_predict = Q_table[current_state][(selected_box_coordinate, action)]
    if next_state in Q_table:
        Q_target = reward + gamma * (max(Q_table[next_state].values()))
    else:
        Q_target = reward
    Q_table[current_state][(selected_box_coordinate, action)] += learningRate * (Q_target - Q_predict)


def calculate_reward(my_game_board: GameBoard, picked_box_action_list, selected_box_coordinate, action, all_selections,
                     total_number_boxes_done):
    if my_game_board.is_any_box_reach_end():
        number_boxes_done_now = my_game_board.get_number_box_done()
        if number_boxes_done_now > total_number_boxes_done:
            reward = 500
            total_number_boxes_done = number_boxes_done_now
        else:
            if picked_box_action_list.count((selected_box_coordinate, action)) > 2:
                reward = picked_box_action_list.count((selected_box_coordinate, action)) * (-5)
            else:
                reward = -5
    elif not all_selections:
        reward = -5000
    elif my_game_board.is_end_game():
        reward = 5000
    elif picked_box_action_list.count((selected_box_coordinate, action)) > 2:
        reward = picked_box_action_list.count((selected_box_coordinate, action)) * (-5)
    else:
        reward = -5
    return reward, total_number_boxes_done
