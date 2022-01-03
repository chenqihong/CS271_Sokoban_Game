from collections import defaultdict

TotalTrainingTimes = 180000

Q_table = defaultdict(lambda: defaultdict(float))
QTableSaveDir = "Qtable.pickle"
TotalStepSize = 500
gamma = 0.85
learningRate = 0.45
step_size = 2
step_dict = {}
bfs_dict = {}
