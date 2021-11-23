"""
constant_configuration.py: The constant configuration file of the project sokoban for CS271
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"

from collections import defaultdict
import pickle
from random import random, choice
from time import time


input_conversion_dict = {0: "size_map", 1: "wall_info", 2: "box_info", 3: "storage_info", 4: "player_pos"}
ALL_LEGAL_MOVES = ['U', 'D', 'L', 'R']
TotalTrainingTimes = 2000

Q_table = defaultdict(lambda: defaultdict(float))
QTableSaveDir = "Qtable.pickle"
TotalStepSize = 10000
gamma = 0.85
learningRate = 0.2

