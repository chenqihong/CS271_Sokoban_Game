from base_implementation import *
from training_module import training
from evaluate_module import evaluate
from constant_configuration import *
from tqdm import tqdm


def train(file):
    for current_training_time in tqdm(range(TotalTrainingTimes)):
        board = read_input(file)
        BaseEpsilon = 1 - 0.0001 * current_training_time
        training(board, BaseEpsilon)


if __name__ == '__main__':
    file = "sokoban01.txt"
    train(file)
    print("Success" if evaluate(read_input(file)) else "Fail")
