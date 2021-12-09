from collections import defaultdict

TotalTrainingTimes = 200

Q_table = defaultdict(lambda: defaultdict(float))
QTableSaveDir = "Qtable.pickle"
TotalStepSize = 100
gamma = 0.9
learningRate = 0.35
step_size = 2
