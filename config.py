# =====================================================================
# INTERESTING PARAMETERS
# =====================================================================

# Input {cars, clock-hands, clouds, manchester, mothecombe, row}
inputName = "manchester" 

# Similarities
skipFrames = 1
matrixBuffer = -1 # If using skipframes, should be 1, else -1

# Future Costs
qualityExponent = 2

# Thresholding
thresholdValue = 0.9 # Lower will allow more transitions
useLocalMaxima = True
useThreshold = True

# Preserving dynamics
adjacentFrames = 2

# GUI
colouringType = "Rainbow"  # Island, Rainbow or Gray

# Video Loops
buildTable = True  # Unfortunately not working right now

# =====================================================================
# INTERNAL PARAMETERS
# =====================================================================

# Similarities
inputPath = "data/input/" + inputName + ".mov"
absInputPath = "C:\Users\Struan\PycharmProjects\TestProject\data\input\\" + inputName + ".mov"

# Probabilities
sigmaMult = 2
skipFutureCosts = False

# Future Cost
futureCostAlpha = 0.995
strictFuture = False  # If we hit a dead-end, do we terminate?

# GUI
displayVisualisations = True
cellWidth = 2
fontSize = 6

# Video Loops
maxCompoundDistance = 10
