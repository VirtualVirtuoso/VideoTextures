from numpy.random import choice
import numpy

import config as c

def main():

    choices = numpy.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    choice_labels = generate_choices(choices)

    chosen_frame = choose_frame(choices, choice_labels, 1)
    print chosen_frame


def choose_frame(choices, choice_labels, frame_number):
    distribution = determine_distribution(choices, frame_number)
    return weighted_choices(choice_labels, distribution)

def weighted_choices(choice_entries, normalized_entries):
    return choice(choice_entries, 1, p=normalized_entries)

def generate_choices(matrix):

    (height, width) = matrix.shape
    choices = numpy.zeros((1, width))

    for i in range(1, width + 1):
        choices[0][i - 1] = i

    return choices[0, :]

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

if __name__ == "__main__":
    main()

