from collections import defaultdict

TotalTrainingTimes = 5000

Q_table = defaultdict(lambda: defaultdict(float))
QTableSaveDir = "Qtable.pickle"
TotalStepSize = 1000
gamma = 0.9
learningRate = 0.35

