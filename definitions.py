import os
import numpy as np

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Decorative Strings
bar_line = "====================================================="
random_play = "Random Play Execution"
basic_random_play = "Unstructured Random Play Execution"
basic_loop_play = "Unstructured Loop Execution"
loop_play = "Standard Loop Execution"

# Error Strings
frame_not_ready = "Frame is not ready"

# Binomial Distribution
# This is defined for weights 1, 2 and 3
# Hard-coding it since we don't need other weight ranged beyond 1-3
bin_dis = np.matrix(
    [[0.0, 0.0, 0.5, 0.5, 0.0, 0.0],
     [0.0, 0.125, 0.375, 0.375, 0.125, 0.0],
     [0.03125, 0.15625, 0.3125, 0.3125, 0.15625, 0.03125]]
)
