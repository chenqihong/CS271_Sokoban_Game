from constant_configuration import *
from game_board_class import *
from random import random
from copy import deepcopy


def read_input(file):
    with open(file, 'r') as f:
        dimension = tuple([int(x) for x in f.readline().split(" ")])
        wall_str = f.readline().split()
        box_str = f.readline().split()
        storage_str = f.readline().split()
        walls = set([(int(wall_str[i]), int(wall_str[i + 1])) for i in range(1, int(wall_str[0]) * 2, 2)])
        boxes = set((int(box_str[i]), int(box_str[i + 1])) for i in range(1, int(box_str[0]) * 2, 2))
        storages = set((int(storage_str[i]), int(storage_str[i + 1])) for i in range(1, int(storage_str[0]) * 2, 2))
        player = tuple([int(x) for x in f.readline().split(" ")])
    return GameBoard(dimension, frozenset(walls), boxes, frozenset(storages), player)


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


def greedy_choice(current_state: str, all_reachable_boxes: list) -> tuple:
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


def update_Q_Value(current_state, selected_box, action, reward, next_state):
    Q_predict = Q_table[current_state][(selected_box, action)]
    Q_target = reward + gamma * (max(Q_table[next_state].values())) if next_state in Q_table else reward
    Q_table[current_state][(selected_box, action)] += learningRate * (Q_target - Q_predict)


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


def simulate(board, action,step):
    path = board.BFS()[action]
    # print("passing action = ", action)
    if not action or not step:
        return 1
    board = deepcopy(board)
    board.move_player(*path[-2])
    board.update_player(action[1])
    result = 0
    bfs = list(board.BFS().keys())
    # print("bfs = ", bfs)
    for action in bfs:
        result += simulate(board, action, step-1)
    return result
