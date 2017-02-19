import numpy
import math

import config as c
import util.mathematics.matrix as matrix_util

def main():
    probability_matrix = matrix_util.load_matrix("../data/output/probability_matrix.csv")
    dynamic_matrix = preserve_dynamics(probability_matrix)
    matrix_util.save_matrix(dynamic_matrix, "dynamic_matrix")

    if c.displayVisualisations:
        matrix_util.display_matrix(dynamic_matrix, "Dynamic Preserved Matrix")

def preserve_dynamics(matrix):
    return "Boop"

if __name__ == "__main__":
    main()