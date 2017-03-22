import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

"""
|-------------------------------------------------------------------------------
| Plot Row GUI Component
|-------------------------------------------------------------------------------
|
| This is a GUI component which is useful for demonstrations. When facing the
| Matrix Visualisation GUI, you can click on a row label, and it will show
| you a line graph of the row, and beneath it, the same row with maxima
| applied.
|
"""

"""
| Creates two plots, one of the magnitudes of the given row, and a second
| of the same row with local maxima applied
"""
def plot_matrix_row(matrix, row):
    row_num = row
    (height, width) = matrix.shape
    fig = plt.figure()
    row = matrix[row - 1]
    print row


    t1 = np.arange(0, width, 1)
    t2 = np.arange(0, width, 1)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, row[t1] / 255, 'bo', t2, row[t2] / 255, 'k')
    plt.title('Magnitude of row')

    maxima_row = determine_maxima(row)

    plt.subplot(212)
    plt.plot(t1, maxima_row[t1] / 255, 'ro', t2, maxima_row[t2] / 255, 'k')
    plt.title('Maxima of row')

    fig.canvas.set_window_title('Analysis of row ' + str(row_num))
    plt.show()

"""
| Takes a row, and removes any entry which isn't a local maxima
"""
def determine_maxima(row):
    processed_row = row
    maxima = argrelextrema(row, np.greater)[0]
    for i in range(0, len(processed_row)):
        if i not in maxima:
            processed_row[i] = 0
    return processed_row
