import copy
import numpy
import math
import config

from gui.frame_chooser import create_matrix_visualization

import util.mathematics.matrix as matrix

# The purpose of this script is to take the existing similarity matrix, and then determine
# a thresholded probability of whether or not a jump should happen. We then save this to a
# file which is then read by the synthesis
def main():

    # Load the distance matrix from the file
    distance_matrix = matrix.load_matrix_from_file("../data/output/future_cost_matrix.csv")

    # Find the probabilities, threshold them, and then save them to a file
    prob_matrix = create_probability_matrix(distance_matrix)

    numpy.savetxt("../data/output/probability_matrix.csv", prob_matrix, delimiter=",")

    create_visualisations(prob_matrix)


# This is for the purposes of visualising the matrices produced by this stage. This is
# useful because it both allows far easier debugging, but also acts as a visual aid for
# demonstrating this system
def create_visualisations(prob_matrix):

    # Map probabilities to gray pixels
    grayscale_prob_matrix = prob_matrix * 255

    # Show the normal distance matrix
    show_matrix_gui(grayscale_prob_matrix, "Probabilities Matrix")


# The paper suggests mapping the distances determined earlier to probabilities using
# the exponential function, in particular P_{ij} \propto exp(-D_{i+1,j}/\sigma)
# Here, sigma is defined to be a mapping constant, which is suggested to be a small
# multiple of the average D_{ij} values
def create_probability_matrix(distance_matrix):

    # Here, sigma is the mean * 6
    sigma = float(distance_matrix.mean()) * config.sigmaMult
    (height, width) = distance_matrix.shape

    # Initialise the matrix
    prob_matrix = numpy.zeros((height - 1, width - 1))

    # Determine each of the probabilities
    for x in range(0, height - 1):
        for y in range(0, width - 1):
            prob_matrix[x][y] = math.exp((-distance_matrix[x + 1][y]) / sigma)

    return prob_matrix



def show_matrix_gui(displayed_matrix, title):
    create_matrix_visualization(displayed_matrix, title)

if __name__ == "__main__":
    main()
