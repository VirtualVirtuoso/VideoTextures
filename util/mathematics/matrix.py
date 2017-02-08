import numpy

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