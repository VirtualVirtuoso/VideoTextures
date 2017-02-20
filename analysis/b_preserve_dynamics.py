import numpy

import config as c
import definitions as d
import util.mathematics.matrix as matrix_util

def main():

    probability_matrix = matrix_util.load_matrix("../data/output/difference_matrix.csv")
    dynamic_matrix = preserve_dynamics(probability_matrix)
    matrix_util.save_matrix(dynamic_matrix, "dynamic_matrix")

    if c.displayVisualisations:
        matrix_util.display_matrix(dynamic_matrix, "Dynamic Preserved Matrix")

def preserve_dynamics(matrix):
    a = c.adjacentFrames
    (height, width) = matrix.shape

    start = 0 + a
    end = height - a
    size = height - (2 * a)

    dynamic_matrix = numpy.zeros((size, size))

    for i in range(start, end):
        for j in range(start, end):
            dynamic_matrix[i - a][j - a] = weighted_window(matrix, i, j, a)

    return dynamic_matrix

def weighted_window(matrix, i, j, m):
    cum_prob = 0.0

    for k in range(-m, m):
        current_term = get_weight(m, k) * float(matrix[i + k][j + k])
        cum_prob += current_term

    return cum_prob

def get_weight(w, m):
    weight = w - 1
    index = m + 3
    return d.bin_dis[weight, index]

if __name__ == "__main__":
    main()
