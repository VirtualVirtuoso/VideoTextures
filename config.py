import os

# Similarities
skipFrames = 1
inputFile = "clock-hands.mov"
inputPath = "data/input/" + inputFile
absInputPath = "C:\Users\Struan\PycharmProjects\TestProject\data\input\\" + inputFile

# Probabilities
sigmaMult = 2
skipFutureCosts = True

# Preserving dynamics
adjacentFrames = 2

# GUI
displayVisualisations = True
cellWidth = 2
fontSize = 6
colouringType = "Gray"  # Island, Rainbow or Gray

# Thresholding
thresholdValue = 0.78

# Future Cost
qualityExponent = 2
futureCostAlpha = 0.9
strictFuture = False  # If we hit a dead-end, do we terminate?


