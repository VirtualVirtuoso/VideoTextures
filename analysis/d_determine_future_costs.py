import numpy
import math

import config as c
import util.mathematics.matrix as matrix_util


def main():
    probability_matrix = matrix_util.load_matrix("../data/output/probability_matrix.csv")
    future_cost_matrix = generate_future_cost_matrix(probability_matrix)
    matrix_util.save_matrix(future_cost_matrix, "future_cost_matrix")

    if c.displayVisualisations:
        matrix_util.display_matrix(future_cost_matrix, "Generated Future Costs")


def generate_future_cost_matrix(distance_matrix):
    (height, width) = distance_matrix.shape
    future_cost_matrix = numpy.zeros((height, width))
    last_matrix = numpy.zeros((height, width))

    for i in range(0, height):
        for j in range(0, width):
            future_cost_matrix[i][j] = math.pow(distance_matrix[i][j], c.qualityTradeOff)

    while True:

        for i in range(0, height - 1):
            for j in range(0, width - 1):
                future_cost_base = math.pow(distance_matrix[i][j], c.qualityTradeOff)

                k_min = future_cost_matrix[j][0]
                for k in range(0, height - 1):
                    if future_cost_matrix[j][k] < k_min:
                        k_min = future_cost_matrix[j][k]

                future_cost_summation = c.futureCostWeight * k_min
                future_cost_matrix[i][j] = future_cost_base + future_cost_summation

        if (future_cost_matrix == last_matrix).all():
            break
        else:
            last_matrix = future_cost_matrix

    return future_cost_matrix


if __name__ == "__main__":
    main()
