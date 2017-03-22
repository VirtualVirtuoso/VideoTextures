from numpy.random import choice
import numpy

import config as c

"""
|-------------------------------------------------------------------------------
| Weighted Choice Utility
|-------------------------------------------------------------------------------
|
| This utility allows us to take a matrix, and make weighted choices over its
| normalised entries
|
"""

"""
| Given the matrix of choices, and a given frame, returns a choice for which
| frame will be displayed next, based on the transition probabilities
"""
def choose_frame(choices, choice_labels, frame_number):
    distribution = determine_distribution(choices, frame_number)
    return weighted_choices(choice_labels, distribution)

"""
|
"""
def weighted_choices(choice_entries, normalized_entries):
    return choice(choice_entries, 1, p=normalized_entries)

"""
|
"""
def generate_choices(matrix):

    (height, width) = matrix.shape
    choices = numpy.zeros((1, width))

    for i in range(1, width + 1):
        choices[0][i - 1] = i

    return choices[0, :]

"""
| Takes a frame, and finds the probability distribution for the available
| transitions
"""
def determine_distribution(matrix, frame):

    (height, width) = matrix.shape
    clipped_matrix = numpy.zeros((1, width))

    for i in range(0, width):
        if i <= frame:
            clipped_matrix[0][i] = 0
        else:
            clipped_matrix[0][i] = matrix[int(frame), i]

    normalized_row = normalize_row(clipped_matrix[0, :])

    return normalized_row

"""
| Takes a row, and ensures that the union of all probabilities is 1
"""
def normalize_row(row):
    width = row.size

    normalized_row = numpy.zeros((1, width), numpy.float64)

    total = row.sum()

    if total == 0:

        # If we allow strict future, then we will hit dead ends and terminate
        if c.strictFuture:
            normalized_row[0][width - 1] = 1
        else:
            for i in range(0, width):
                normalized_row[0][i] = 1 / float(width)
    else:
        for i in range(0, width):
            normalized_row[0][i] = row[i] / float(total)


    return normalized_row[0, :]

