import config as c
import numpy as np
import gui.directed_graph as dg

import util.mathematics.matrix as matrix
import util.mathematics.loop_overlap as overlap

MAX_INT = 2147483647

def main():
    threshold_matrix = matrix.load_matrix("thresholds")
    cost_matrix = matrix.load_matrix("dynamics")

    loops = find_loops(threshold_matrix, cost_matrix)
    dg.plot_loops(loops)

    if c.buildTable:
        build_transition_table(loops)

def build_transition_table(loops):
    # A loop has the structure:
    # 0 - From
    # 1 - To
    # 2 - Distance
    # 3 - Cost

    N = len(loops)
    L = c.maxCompoundDistance

    # The transition table is a cube, where the first two dimensions are transition vs
    # maximum compound loop. The third dimension is from, to and cost respectively.
    # We instantiate this transition table here
    tt = np.zeros(L, N, (L * 2) + 1)

    # Create the first row of the table
    for cell in range(0, N):
        loop = loops[cell]
        if loop[2] == 1:
            tt[0][cell] = [loop[3], loop[0], loop[1]]

    # Generate the remaining rows of the table
    for i in range(1, L):
        for j in range(0, N):
            column = [row[j] for row in tt]
            min_cost = MAX_INT
            min_found_col = -1
            min_found_row = -1
            min_row = -1

            # Go from the cell up through the column until the top
            for k in range(len(column), 0, -1):
                compound_loop = tt[k][j][1:]
                compound_loop = np.reshape(compound_loop, (2, len(compound_loop) / 2))
                compound_loop_cost = tt[k][j][0]
                compound_loop_len = sum(compound_loop[1][:] - compound_loop[0][:])

                primitive_from = loops[j][0]
                primitive_to = loops[j][1]
                primitive_len = loops[j][2]
                primitive_cost = loops[j][3]

                # Add the primitive loop as a new one
                if compound_loop_len == 0 and i == primitive_len:
                    tt[i][j][0] = primitive_cost
                    tt[i][j][1] = primitive_from
                    tt[i][j][2] = primitive_to
                    break

                # The case where we want to append a primitive to a compound loop
                if compound_loop_len + primitive_len == i:
                    min_cost = primitive_cost + compound_loop_cost
                    tt[i][j][0] = min_cost
                    base_loop = np.nonzero(tt[k][j][1:])

                    new_loop = [base_loop, primitive_from, primitive_to]
                    tt[i][j][1:len(new_loop) + 1] = np.reshape(new_loop, (1, 1, len(new_loop)))

                # Combine compound loops of overlapping columns

                for m in range(0, N):
                    if overlap.check_loop_overlap(loops[m], compound_loop):
                        matched_len = i - compound_loop_len
                        matched_cost = tt[matched_len][m][0]
                        total_cost = matched_cost + compound_loop_cost

                        if matched_cost != 0 and total_cost < min_cost:
                            min_cost = total_cost
                            min_found_col = m
                            min_found_row = matched_len
                            min_row = k


            if min_found_col != -1:
                matched_loop = tt[min_found_row][min_found_col][1:]
                matched_loop_len = len(matched_loop)
                matched_loop = np.reshape(matched_loop, (1, matched_loop_len))
                base_loop = tt[min_row][j][1:]

                tt[i][j][0] = tt[min_found_row][min_found_col][0] + tt[min_row][j][0]
                base_loop_len = len(np.nonzero(base_loop))

                np.reshape(np.nonzero(base_loop), (2, len(np.nonzero(base_loop)) / 2))
                np.reshape(matched_loop, (2, len(tt[i][j][1:]) / 2))

                new_loop = [np.nonzero(base_loop), matched_loop[0:len(matched_loop) - base_loop_len]]
                tt[i][j][1:] = np.reshape(new_loop, (1, 1, len(new_loop)))

    for i in range(0, L):
        print tt[i]

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
