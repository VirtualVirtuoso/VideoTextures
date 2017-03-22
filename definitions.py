import os
import numpy as np

"""
|-------------------------------------------------------------------------------
| Definitions
|-------------------------------------------------------------------------------
|
| Here we define reusable constants which shouldn't be changed by the end user
|
"""

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Decorative strings for console
BAR_LINE = "====================================================="
EMPTY_LINE = ""
SPACER = "                         "

# Names of modes
random_play = "Random Play Execution"
basic_random_play = "Unstructured Random Play Execution"
basic_loop_play = "Unstructured Loop Execution"
loop_play = "Standard Loop Execution"

# Analysis Launch Messages
similarities_clicked = "Determining Distances between Frames... (Might take a while)"
dynamics_clicked = "Taking into account dynamics of motion..."
future_clicked = "Determining Future Costs of Transitions..."
probabilities_clicked = "Turning Costs into Probabilities..."
prune_clicked = "Pruning Probability Matrix..."

# Synthesis Launch Messages
basic_random_clicked = "Generating Random Video..."
basic_loop_clicked = "Generating Looping Video..."
informed_random_clicked = "Generating Informed Random Video..."
video_loops_clicked = "Generating Video Loops..."

# Error strings
frame_not_ready = "Frame is not ready"

# Binomial Distribution
# This is defined for weights 1, 2 and 3
# Hard-coding it since we don't need other weight ranged beyond 1-3
BINOMIAL_DISTRIBUTION = np.matrix(
    [[0.0, 0.0, 0.5, 0.5, 0.0, 0.0],
     [0.0, 0.125, 0.375, 0.375, 0.125, 0.0],
     [0.03125, 0.15625, 0.3125, 0.3125, 0.15625, 0.03125]]
)

MAX_INT = 2147483647
