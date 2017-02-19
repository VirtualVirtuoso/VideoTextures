import copy

import util.mathematics.matrix as matrix_util
import config as c

def main():
    future_matrix = matrix_util.load_matrix("../data/output/probability_matrix.csv")
    thresholded_matrix = matrix_util.threshold_matrix(copy.copy(future_matrix), c.thresholdValue)
    matrix_util.save_matrix(thresholded_matrix, "thresholded_matrix")

    if c.displayVisualisations:
        threshold_title = "Thresholded at: ", c.thresholdValue
        matrix_util.display_matrix(thresholded_matrix, threshold_title)

if __name__ == "__main__":
    main()
