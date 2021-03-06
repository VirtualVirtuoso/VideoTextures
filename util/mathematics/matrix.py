import numpy
import config as c

from gui.frame_chooser import create_matrix_visualization

"""
|-------------------------------------------------------------------------------
| Matrix Utilities
|-------------------------------------------------------------------------------
|
| A collection of functions which are reused in different areas of the program.
| Functions include reading and writing matrices to files, displaying said
| matrices in the GUI, and other operations
|
"""

"""
| Takes a matrix, and sets any cell under a certain value to 0
"""
def threshold_matrix(matrix, threshold):
    thresholded_matrix = matrix
    low_value_indices = thresholded_matrix < threshold
    thresholded_matrix[low_value_indices] = 0
    return thresholded_matrix

"""
| Go through each of the rows, and normalises them
"""
def normalize_by_rows(matrix):
    (height, width) = matrix.shape
    normalized_matrix = numpy.zeros((height, width))

    for x in range(0, height):
        row = matrix[x]
        euclidean_dist = numpy.atleast_1d(numpy.linalg.norm(row, 2, -1))
        euclidean_dist[euclidean_dist == 0] = 1
        normalized_matrix[x] = row / numpy.expand_dims(euclidean_dist, -1)

    return normalized_matrix

"""
| Loads the matrix from the given matrix type folder
"""
def load_matrix(matrix_type):
    path = "C:/Users/Struan/PycharmProjects/TestProject/data/output/" + matrix_type + "/" + c.inputName + ".csv"
    matrix = numpy.loadtxt(open(path, "rb"), delimiter=",")
    return matrix

"""
| Saves the matrix under the given matrix type folder
"""
def save_matrix(matrix, matrix_type):
    path = "C:/Users/Struan/PycharmProjects/TestProject/data/output/" + matrix_type + "/" + c.inputName + ".csv"
    numpy.savetxt(path, matrix, delimiter=",")

"""
| Takes a matrix, and visualises it in the GUI
"""
def display_matrix(matrix, title):
    matrix_max = numpy.max(numpy.abs(matrix))
    if matrix_max > 0:
        matrix /= matrix_max
    matrix *= 255.0
    create_matrix_visualization(matrix, title)

"""
| Finds the smallest element in a given row
"""
def find_row_minimum(matrix, row):
    (height, width) = matrix.shape
    row_min = matrix[row][0]

    for k in range(0, width - 1):
        if matrix[row][k] < row_min:
            row_min = matrix[row][k]

    return row_min

