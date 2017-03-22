import numpy
import math
import config as c

import util.mathematics.matrix as matrix_util

'''
|-------------------------------------------------------------------------------
| Determining Probabilities
|-------------------------------------------------------------------------------
|
| Arguably the most simple step, we map the distances found to probabilities.
| At this stage, we don't normalise the matrix, however this occurs later
| the process when we're loading the videos
|
'''

def main():

    # Config option which allows us to skip the future cost processing. Useful for comparing
    # results
    if c.skipFutureCosts:
        distance_matrix = matrix_util.load_matrix("dynamics")
    else:
        distance_matrix = matrix_util.load_matrix("futurecosts")

    prob_matrix = create_probability_matrix(distance_matrix)
    matrix_util.save_matrix(prob_matrix, "probabilities")

    if c.displayVisualisations:
        matrix_util.display_matrix(prob_matrix, "Determined Probabilities")

'''
| The paper suggests mapping the distances determined earlier to probabilities using
| the exponential function, in particular P_{ij} \propto exp(-D_{i+1,j}/\sigma)
| Here, sigma is defined to be a mapping constant, which is suggested to be a small
| multiple of the average D_{ij} values
'''
def create_probability_matrix(distance_matrix):

    # Here, sigma is the mean * 6
    sigma = float(distance_matrix.mean()) * c.sigmaMult
    (height, width) = distance_matrix.shape

    # Initialise the matrix
    prob_matrix = numpy.zeros((height - 1, width - 1))

    # Determine each of the probabilities
    for x in range(0, height - 1):
        for y in range(0, width - 1):
            prob_matrix[x][y] = math.exp((-distance_matrix[x + 1][y]) / sigma)

    return prob_matrix

if __name__ == "__main__":
    main()
