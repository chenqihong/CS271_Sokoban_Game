from collections import defaultdict

TotalTrainingTimes = 300

Q_table = defaultdict(lambda: defaultdict(float))
QTableSaveDir = "Qtable.pickle"
TotalStepSize = 500
gamma = 0.9
learningRate = 0.35
step_size = 2
