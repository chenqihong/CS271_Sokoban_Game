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
    board = read_input("benchmarks\sokoban90.txt")
    all_selections = list(board.BFS().keys())
    print("all selections = ", all_selections)
    # print(simulate(board, all_selections[0], 1))
    # print(simulate(board, all_selections[1], 1))
    # max = 0
    # result = []
    # for selection in all_selections:
    #     score = simulate(board, (selection, board.BFS()[selection]), 1)
    #     if score > max:
    #         result = [selection]
    #         max = score
    #     elif score == max:
    #         result.append(selection)
    # print("result = ", result)


    train(board)
    print("Success" if evaluate(board) else "Fail")
