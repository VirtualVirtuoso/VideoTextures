import config as c
import numpy as np
import gui.directed_graph as dg

import util.mathematics.matrix as matrix

def main():
    threshold_matrix = matrix.load_matrix("../data/output/thresholded_matrix.csv")
    cost_matrix = matrix.load_matrix("../data/output/dynamic_matrix.csv")

    loops = find_loops(threshold_matrix, cost_matrix)
    dg.plot_loops(loops)
    # build_transition_table(loops)

def build_transition_table(loops):
    width = len(loops)
    height = c.maxCompoundDistance

    transition_table = []
    for i in range(0, height):
        row = []
        for j in range(0, width):
            row.append([])
        transition_table.append(row)

    for combo_length in range(0, height):
        for transition in range(0, width):
            if loops[transition][2] == combo_length:
                loop = loops[transition]
                transition_table[combo_length][transition] = [loop[0], loop[1], int(loop[3])]

    for i in range(0, height):
        print transition_table[i]

def find_overlaps(transition, loops):
    print "Hello"

def find_loops(threshold_matrix, weight_matrix):
    (height, width) = threshold_matrix.shape
    loops = []

    for i in range(2, height):
        for j in range(1, i):
            if threshold_matrix[i][j] != 0:
                loops.append([i, j, abs(i - j), weight_matrix[i][j]])

    # for i in range(0, len(loops)):
    #     print "Loop " + str(i + 1) + "\tStart: " + str(loops[i][0]) + "\tEnd: " \
    #           + str(loops[i][1]) + "\t\tDistance: " + str(loops[i][2]) + "\tCost: " + str(loops[i][3])

    return loops


if __name__ == "__main__":
    main()
