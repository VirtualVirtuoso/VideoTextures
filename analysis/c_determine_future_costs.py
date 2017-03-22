import numpy
import math

import config as c
import util.mathematics.matrix as matrix_util

"""
|-------------------------------------------------------------------------------
| Determining Future Costs
|-------------------------------------------------------------------------------
|
| Some scenes have different 'stages', where there aren't meaningful transitions
| between these stages. This means that if we enter a later stage, we can be
| in the position where we are confined to one small part of the video.
| This method prevents us from becoming trapped in these small dead
| ends, by looking into the future with basic machine learning.
|
"""

def main():

    # Using the dynamics matrix, we then produce and save the future cost matrix
    dynamic_matrix = matrix_util.load_matrix("dynamics")
    future_cost_matrix = generate_future_cost_matrix(dynamic_matrix)
    matrix_util.save_matrix(future_cost_matrix, "futurecosts")

    if c.displayVisualisations:
        matrix_util.display_matrix(future_cost_matrix, "Generated Future Costs")

"""
| This function is dervied from a  method called Q-Learning. The idea corresponds
| to finding the best path through a graph with our costs on the edges. We take
| the costs found, and apply it to the minimum of the row in a matrix we
| update in each iteration. The function ends when our update matrix remains
| unchanged.
"""
def generate_future_cost_matrix(dynamic_matrix):
    (height, width) = dynamic_matrix.shape

    # This is the final output matrix, which is returned by the function
    future_cost_matrix = numpy.zeros((height, width))

    # This matrix is used as a buffer between previous results. If the change in an iteration
    # is 0, then it means that the process has converged
    last_matrix = numpy.zeros((height, width))

    # We initialise with D''ij = (D'ij)^p
    for i in range(1, height):
        for j in range(0, width):
            future_cost_matrix[i][j] = math.pow(dynamic_matrix[i - 1][j], c.qualityExponent)

    # Continue until an iteration does not change the matrix
    while True:

        for i in range(height - 1, 0, -1):
            for j in range(0, width - 1):

                # Determine the (D'_ij)^p term
                future_cost_base = math.pow(dynamic_matrix[i][j], c.qualityExponent)

                # Determine the row minimum m_j = min_k D''_jk
                k_min = matrix_util.find_row_minimum(future_cost_matrix, j)

                future_cost_summation = c.futureCostAlpha * k_min
                future_cost_matrix[i][j] = future_cost_base + future_cost_summation

        if (future_cost_matrix == last_matrix).all():
            break
        else:
            last_matrix = future_cost_matrix

    return future_cost_matrix

if __name__ == "__main__":
    main()

