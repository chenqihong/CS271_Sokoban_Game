from collections import defaultdict

TotalTrainingTimes = 1000

Q_table = defaultdict(lambda: defaultdict(float))
QTableSaveDir = "Qtable.pickle"
TotalStepSize = 500
gamma = 0.9
learningRate = 0.35
step_size = 2
step_dict = {}
