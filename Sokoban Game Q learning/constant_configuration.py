from collections import defaultdict

TotalTrainingTimes = 1000

Q_table = defaultdict(lambda: defaultdict(float))
QTableSaveDir = "Qtable.pickle"
TotalStepSize = 10000
gamma = 0.85
learningRate = 0.35

