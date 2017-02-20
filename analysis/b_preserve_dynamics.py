import numpy
import math

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
    adjacent_frames = c.adjacentFrames
    (height, width) = matrix.shape
    dynamic_matrix = numpy.zeros((height, width))

    for i in range(0, height):
        for j in range(0, width):
            dynamic_matrix[i][j] = weighted_window(matrix, i, j, adjacent_frames)

    return dynamic_matrix

def weighted_window(matrix, i, j, m):
    (height, width) = matrix.shape
    cum_prob = 0.0

    for k in range(-m, m - 1):
        i_index = i + k
        j_index = j + k

        if (0 < i_index < width - 1) and (0 < j_index < height - 1):
            current_term = get_weight(m, k) * float(matrix[i + k][j + k])
            cum_prob += current_term

    return cum_prob

def get_weight(w, m):
    weight = w - 1
    index = m + 3
    return d.bin_dis[weight, index]

if __name__ == "__main__":
    main()
