"""
constant_configuration.py: The constant configuration file of the project sokoban for CS271
"""

__author__ = "Qi Hong Chen"
__copyright__ = "Copyright 2021, The game of Sokoban game project"

from collections import defaultdict
import pickle
import random
import time

input_conversion_dict = {0: "size_map", 1: "wall_info", 2: "box_info", 3: "storage_info", 4: "player_pos"}
ALL_LEGAL_MOVES = ['U', 'D', 'L', 'R']
state_value_table = defaultdict(int)
TotalTrainingTimes = 1200

simulation_choices_list = []
UCT_table = defaultdict(float)

UCTSaveDir = "UTC_Table.pickle"
TotalStepSize = 60
gamma = 0.84
returns = defaultdict(list)
total_number_boxes_done = 0

