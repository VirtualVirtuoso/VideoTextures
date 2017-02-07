import config as config
import determine_probabilities as probabilities
import numpy
import math

def main():

    probability_matrix = probabilities.load_matrix_from_file("../data/output/probability_matrix.csv")
    future_cost_matrix = generateFutureCostMatrix(probability_matrix)
    numpy.savetxt("../data/output/future_cost_matrix.csv", future_cost_matrix, delimiter=",")
    probabilities.show_matrix_gui(future_cost_matrix * 255, "Future Costs")


def generateFutureCostMatrix(probability_matrix):
    (height, width) = probability_matrix.shape
    future_cost_matrix = numpy.zeros((height - 1, width - 1))

    for x in range(0, height - 1):
        for y in range(0, width - 1):
            future_cost_base = math.exp(probability_matrix[x][y], config.qualityTradeOff)
            future_cost_summation = config.futureCostWeight * 1
            future_cost_matrix[x][y] = future_cost_base + future_cost_summation

    return future_cost_matrix

def determineMinimumFuture(probability_matrix):
    return "yay"


if __name__ == "__main__":
    main()

