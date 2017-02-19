import copy
import numpy

import util.mathematics.matrix as matrix_util
import config as config

from gui.frame_chooser import create_matrix_visualization

def main():
    future_matrix = matrix_util.load_matrix_from_file("../data/output/future_cost_matrix.csv")
    thresholded_matrix = matrix_util.threshold_matrix(copy.copy(future_matrix), config.thresholdValue)

    numpy.savetxt("../data/output/thresholded_matrix.csv", thresholded_matrix, delimiter=",")

    threshold_title = "Thresholded at: ", config.thresholdValue

    thresholded_matrix /= numpy.max(numpy.abs(thresholded_matrix), axis=0)
    thresholded_matrix *= 255.0

    create_matrix_visualization(thresholded_matrix, threshold_title)

if __name__ == "__main__":
    main()