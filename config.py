# Similarities
skipFrames = 1
inputName = "clock-hands"
inputPath = "data/input/" + inputName + ".mov"
absInputPath = "C:\Users\Struan\PycharmProjects\TestProject\data\input\\" + inputName + ".mov"

# Probabilities
sigmaMult = 2
skipFutureCosts = False

# Preserving dynamics
adjacentFrames = 2

# GUI
displayVisualisations = True
cellWidth = 2
fontSize = 6
colouringType = "Rainbow"  # Island, Rainbow or Gray

# Thresholding
thresholdValue = 0.9
useLocalMaxima = True
useThreshold = True

# Future Cost
qualityExponent = 2
futureCostAlpha = 0.995
strictFuture = False  # If we hit a dead-end, do we terminate?

# Video Loops
maxCompoundDistance = 100
