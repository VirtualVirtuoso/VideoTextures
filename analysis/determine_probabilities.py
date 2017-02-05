import copy
import numpy
import math
import config
from gui.frame_chooser import create_matrix_visualization

from matplotlib import pyplot as plt



# The purpose of this script is to take the existing similarity matrix, and then determine
# a thresholded probability of whether or not a jump should happen. We then save this to a
# file which is then read by the synthesis
def main():

    # Load the distance matrix from the file
    distance_matrix = load_matrix_from_file("../data/output/difference_matrix.csv")

    # Find the probabilities, threshold them, and then save them to a file
    prob_matrix = create_probability_matrix(distance_matrix)
    thresholded_matrix = threshold_matrix(copy.copy(prob_matrix), config.thresholdValue)
    numpy.savetxt("../data/output/thresholded_matrix.csv", thresholded_matrix, delimiter=",")

    create_visualisations(prob_matrix, thresholded_matrix)



# This is for the purposes of visualising the matrices produced by this stage. This is
# useful because it both allows far easier debugging, but also acts as a visual aid for
# demonstrating this system
def create_visualisations(prob_matrix, thresholded_matrix):

    # Map probabilities to gray pixels
    grayscale_prob_matrix = prob_matrix * 255
    grayscale_thresholded_matrix = thresholded_matrix * 255

    # Show the normal distance matrix
    show_matrix_gui(grayscale_prob_matrix, "Distance Matrix")

    # Show the thresholded matrix
    threshold_title = "Thresholded at: ", config.thresholdValue
    show_matrix_gui(grayscale_thresholded_matrix, threshold_title)

    plt.imshow(grayscale_prob_matrix, interpolation='nearest')
    plt.show(block=False)



# The paper suggests mapping the distances determined earlier to probabilities using
# the exponential function, in particular P_{ij} \propto exp(-D_{i+1,j}/\sigma)
# Here, sigma is defined to be a mapping constant, which is suggested to be a small
# multiple of the average D_{ij} values
def create_probability_matrix(distance_matrix):

    # Here, sigma is the mean * 6
    sigma = float(distance_matrix.mean()) * 6
    (height, width) = distance_matrix.shape

    # Initialise the matrix
    prob_matrix = numpy.zeros((height - 1, width - 1))

    # Determine each of the probabilities
    for x in range(0, height - 1):
        for y in range(0, width - 1):
            prob_matrix[x][y] = math.exp((-distance_matrix[x + 1][y]) / sigma)

    return prob_matrix



# Here we take the probability matrix, and threshold it against a certain value.
def threshold_matrix(matrix, threshold):
    thresholded_matrix = matrix
    low_value_indices = thresholded_matrix < threshold
    thresholded_matrix[low_value_indices] = 0
    return thresholded_matrix

def normalize_by_rows(matrix):
    (height, width) = matrix.shape
    normalized_matrix = numpy.zeros((height, width))

    for x in range(0, height):
        row = matrix[x]
        euclidean_dist = numpy.atleast_1d(numpy.linalg.norm(row, 2, -1))
        euclidean_dist[euclidean_dist == 0] = 1
        normalized_matrix[x] = row / numpy.expand_dims(euclidean_dist, -1)

    return normalized_matrix

def load_matrix_from_file(file_name):
    matrix = numpy.loadtxt(open(file_name, "rb"), delimiter=",")
    return matrix

def show_matrix_gui(matrix, title):
    create_matrix_visualization(matrix, title)

if __name__ == "__main__":
    main()
