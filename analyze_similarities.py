import copy
import numpy
import math
from gui.frame_chooser import create_matrix_visualization

from matplotlib import pyplot as plt

def main():
    sim_matrix = load_matrix_from_file("data/output/difference_matrix.csv")
    prob_matrix = create_probability_matrix(sim_matrix)
    normed_matrix = prob_matrix / prob_matrix.max(axis=1)
    gray_matrix = normed_matrix * 255

    threshold_value = 200
    threshold_title = "Thresholded at: ", threshold_value

    thresholded_matrix = threshold_matrix(copy.copy(gray_matrix), threshold_value)

    show_matrix_gui(gray_matrix, "Similarity between frames")
    show_matrix_gui(thresholded_matrix, threshold_title)

    plt.imshow(gray_matrix, interpolation='nearest')
    plt.show(block=False)

def threshold_matrix(matrix, threshold):
    thresholded_matrix = matrix
    low_value_indices = thresholded_matrix < threshold
    thresholded_matrix[low_value_indices] = 0
    return thresholded_matrix

def load_matrix_from_file(file_name):
    matrix = numpy.loadtxt(open(file_name, "rb"), delimiter=",")
    return matrix

def create_probability_matrix(matrix):

    sigma = float(matrix.mean())
    (height, width) = matrix.shape

    prob_matrix = numpy.zeros((height - 1, width - 1))

    for x in range(0, height - 1):
        for y in range(0, width - 1):
            prob_matrix[x][y] = math.exp((-matrix[x][y]) / sigma)

    return prob_matrix

def show_matrix_gui(matrix, title):
    create_matrix_visualization(matrix, title)

if __name__ == "__main__":
    main()
