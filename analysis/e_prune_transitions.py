import copy
import numpy as np

import util.mathematics.matrix as matrix_util
import config as c

from scipy.signal import argrelextrema

'''
|-------------------------------------------------------------------------------
| Pruning Transitions
|-------------------------------------------------------------------------------
|
| Once we have determined all the probabilities, we need to restrict what
| transitions we will use, by the quality of the given transition. Here
| I present two ways of selecting, using a global threshold (quality)
| and finding local maxima (so we don't have multiple indistinguish-
| able transitions).
|
'''

def main():
    future_matrix = matrix_util.load_matrix("probabilities")
    threshold_title = "Not thresholded..."

    # Determine Local Maxima
    if c.useLocalMaxima:
        future_matrix = determine_local_maxima(future_matrix)
        threshold_title = "Local Maxima"

    # Now Threshold
    if c.useThreshold:
        future_matrix = matrix_util.threshold_matrix(copy.copy(future_matrix), c.thresholdValue)
        if c.useLocalMaxima:
            threshold_title = "Local Maxima & Thresholded at " + str(c.thresholdValue)
        else:
            threshold_title = "Thresholded at " + str(c.thresholdValue)

    matrix_util.save_matrix(future_matrix, "thresholds")

    if c.displayVisualisations:
        matrix_util.display_matrix(future_matrix, threshold_title)

'''
| Very simple process which ensures that we only select the peaks of the distribution
| of probabilities, hence removing similar transitions.
'''
def determine_local_maxima(matrix):
    thresholded_matrix = matrix
    (height, width) = matrix.shape

    # Go through each of the rows
    for i in range(0, height):

        # Find the maxima of the given row
        maxima = argrelextrema(matrix[i], np.greater)[0]
        for j in range(0, width):

            # Set anything which isn't a maxima to 0
            if j not in maxima:
                matrix[i][j] = 0

    return thresholded_matrix

if __name__ == "__main__":
    main()
