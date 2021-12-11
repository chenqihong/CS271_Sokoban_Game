from base_implementation import *
from training_module import training
from evaluate_module import evaluate
from constant_configuration import *
from tqdm import tqdm
from copy import deepcopy


def train(board):
    for current_training_time in tqdm(range(TotalTrainingTimes)):
        BaseEpsilon = 1 - (1 / TotalTrainingTimes) * current_training_time
        training(deepcopy(board), BaseEpsilon)


if __name__ == '__main__':
    board = read_input("input_files/sokoban05b.txt")
    train(board)
    print("Success" if evaluate(board) else "fail")
