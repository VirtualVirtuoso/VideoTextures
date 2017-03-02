import copy
import numpy as np

import util.mathematics.matrix as matrix_util
import config as c

from scipy.signal import argrelextrema

def main():
    future_matrix = matrix_util.load_matrix("../data/output/probability_matrix.csv")
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

    matrix_util.save_matrix(future_matrix, "thresholded_matrix")

    if c.displayVisualisations:
        matrix_util.display_matrix(future_matrix, threshold_title)

def determine_local_maxima(matrix):
    thresholded_matrix = matrix
    (height, width) = matrix.shape

    # Go through each of the rows
    for i in range(0, height):
        maxima = argrelextrema(matrix[i], np.greater)[0]
        for j in range(0, width):
            if j not in maxima:
                matrix[i][j] = 0

    return thresholded_matrix



if __name__ == "__main__":
    main()
