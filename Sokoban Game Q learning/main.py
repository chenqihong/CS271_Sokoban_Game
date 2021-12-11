from base_implementation import *
from training_module import training
from evaluate_module import evaluate
from constant_configuration import *
from tqdm import tqdm
from copy import deepcopy


def train(board):
    for current_training_time in tqdm(range(TotalTrainingTimes)):
        BaseEpsilon = 1 - (1/TotalTrainingTimes) * current_training_time
        training(deepcopy(board), BaseEpsilon)


if __name__ == '__main__':
    fail_list = []
    for file in os.listdir("input_files"):
        if not file.startswith("sokoban"):
            continue
        dir = "input_files/" + file
        board = read_input(dir)
        train(board)
        print(file + " Success" if evaluate(board) else fail_list.append(dir))
        step_dict = {}
        bfs_dict = {}
    print(fail_list)
