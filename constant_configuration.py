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
# UCT_table =  {((7, 3), 'R'): -29.810963731041536, ((6, 3), 'D'): -29.79033643929524, ((5, 3), 'D'): -29.847335718373174, ((3, 5), 'R'): -29.784931932008618, ((4, 3), 'D'): -29.815785705586382, ((3, 4), 'R'): -29.76778035596955, ((3, 3), 'D'): -29.799691714243462, ((4, 3), 'U'): -29.806129089113593, ((3, 6), 'U'): -29.820059760084558, ((5, 3), 'U'): -29.825842978953716, ((4, 6), 'U'): -29.832841301702157, ((5, 6), 'U'): -30.776211863156373, ((6, 3), 'U'): -29.853138778263663, ((6, 4), 'L'): -29.798072582439527, ((6, 5), 'L'): -30.6986503042864, ((6, 7), 'U'): -29.8730174071148, ((3, 3), 'R'): -29.861859444793268, ((6, 6), 'R'): -29.80007789125653, ((3, 4), 'L'): -29.836124289860976, ((6, 5), 'R'): -29.82238234639343, ((6, 4), 'R'): -29.816285737754807, ((3, 5), 'L'): -29.727043096991224, ((6, 6), 'L'): -29.845915439487747, ((6, 3), 'R'): -29.790511628459374, ((3, 3), 'L'): -29.824175490066747, ((3, 2), 'U'): -29.834904053899063, ((5, 6), 'R'): -29.733612401050987, ((6, 6), 'U'): -29.79213943052606, ((5, 6), 'D'): -29.85693269218569, ((4, 6), 'D'): -29.71189650765669, ((3, 6), 'D'): -29.82434398618805, ((3, 6), 'L'): -29.727948376872188}

UCTSaveDir = "UTC_Table.pickle"
TotalStepSize = 40
gamma = 0.9
returns = defaultdict(list)
total_number_boxes_done = 0

