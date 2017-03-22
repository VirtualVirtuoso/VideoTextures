# coding=utf-8
import numpy

import config as c
import definitions as d
import util.mathematics.matrix as matrix_util

"""
|-------------------------------------------------------------------------------
| Preserving Dynamics
|-------------------------------------------------------------------------------
|
| Scenes have implicit movement, and this movement can change between different
| parts of the video. Making transitions between different scene dynamics can
| leave us with unnatural jumps. This process takes into account the
| dynamics of a transition, and removes those which are unsuitable.
|
"""

def main():

    # Load the difference matrix from the previous step, transform it, then save it
    diff_matrix = matrix_util.load_matrix("differences")
    dynamic_matrix = preserve_dynamics(diff_matrix)
    matrix_util.save_matrix(dynamic_matrix, "dynamics")

    if c.displayVisualisations:
        matrix_util.display_matrix(dynamic_matrix, "Dynamic Preserved Matrix")

"""
| This function takes the difference matrix, and applies the notion of dynamics
| preservation. When making a transition from frame a to frame b, you take a weighted
| window of some of the neighbours of b on either side.
"""
def preserve_dynamics(matrix):
    num_adjacent = c.adjacentFrames
    (height, width) = matrix.shape

    # We have to define a buffer around the edge of the matrix, which we can then
    # sample, otherwise our neighbour analysis will go out of bounds
    start = 0 + num_adjacent
    end = height - num_adjacent
    size = height - (2 * num_adjacent)

    dynamic_matrix = numpy.zeros((size, size))

    for i in range(start, end):
        for j in range(start, end):
            dynamic_matrix[i - num_adjacent][j - num_adjacent] = \
                weighted_window(matrix, i, j, num_adjacent)

    return dynamic_matrix

"""
| This finds the cumulative weight across all of the neighbours in the
| weighted window. In terms of the matrix, it is a given number of cells
| to the top left or bottom right.
|
|     □
|       ■     Example where num_adjacent = 1
|         □
"""
def weighted_window(matrix, i, j, num_adjacent):
    cum_weight = 0.0

    for k in range(-num_adjacent, num_adjacent):
        current_term = get_weight(num_adjacent, k) * float(matrix[i + k][j + k])
        cum_weight += current_term

    return cum_weight

"""
| Small helper function to find the weights, using a binomial distribution (cells
| which are closer to the source cell should be given more weight
"""
def get_weight(num_adjacent, cell):
    weight = num_adjacent - 1
    index = cell + 3
    return d.BINOMIAL_DISTRIBUTION[weight, index]

if __name__ == "__main__":
    main()
