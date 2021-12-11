from collections import defaultdict
import os

TotalTrainingTimes = 3000

Q_table = defaultdict(lambda: defaultdict(float))
QTableSaveDir = "Qtable.pickle"
TotalStepSize = 1000
gamma = 0.9
learningRate = 0.35
step_size = 2
step_dict = {}
bfs_dict = {}
