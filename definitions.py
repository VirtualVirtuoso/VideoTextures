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
