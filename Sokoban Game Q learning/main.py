from base_implementation import *
from training_module import training
from evaluate_module import evaluate
from constant_configuration import *
from tqdm import tqdm
from copy import deepcopy


def train(board):
    for current_training_time in tqdm(range(TotalTrainingTimes)):
        BaseEpsilon = 1 - 0.0001 * current_training_time
        training(deepcopy(board), BaseEpsilon)


if __name__ == '__main__':
    board = read_input("sokoban02.txt")
    all_selections = list(board.BFS().keys())
    print(simulate(board, all_selections[1], 5))
    #train(board)
    #print("Success" if evaluate(board) else "Fail")
