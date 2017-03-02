import numpy
import math

import config as c
import util.mathematics.matrix as matrix_util


def main():
    dynamic_matrix = matrix_util.load_matrix("../data/output/dynamic_matrix.csv")
    future_cost_matrix = generate_future_cost_matrix(dynamic_matrix)
    matrix_util.save_matrix(future_cost_matrix, "future_cost_matrix")

    if c.displayVisualisations:
        matrix_util.display_matrix(future_cost_matrix, "Generated Future Costs")


def generate_future_cost_matrix(dynamic_matrix):
    (height, width) = dynamic_matrix.shape

    future_cost_matrix = numpy.zeros((height, width))

    # This matrix is used as a buffer between previous results. If the change in an iteration
    # is 0, then it means that the process has converged
    last_matrix = numpy.zeros((height, width))

    # We initialise with D''ij = (D'ij)^p
    for i in range(1, height):
        for j in range(0, width):
            future_cost_matrix[i][j] = math.pow(dynamic_matrix[i-1][j], c.qualityExponent)

    # Continue until an iteration does not change the matrix
    while True:

        for i in range(height - 1, 0, -1):
            for j in range(0, width - 1):

                # Determine the (D'_ij)^p term
                future_cost_base = math.pow(dynamic_matrix[i][j], c.qualityExponent)

                # Determine the row minimum m_j = min_k D''_jk
                k_min = find_row_minimum(future_cost_matrix, j)

                future_cost_summation = c.futureCostAlpha * k_min
                future_cost_matrix[i][j] = future_cost_base + future_cost_summation

        if (future_cost_matrix == last_matrix).all():
            break
        else:
            last_matrix = future_cost_matrix

    return future_cost_matrix

def find_row_minimum(matrix, row):
    (height, width) = matrix.shape
    row_min = matrix[row][0]

    for k in range(0, width - 1):
        if matrix[row][k] < row_min:
            row_min = matrix[row][k]

    return row_min



if __name__ == "__main__":
    main()

