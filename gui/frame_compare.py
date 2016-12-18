import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np

def compare_frames(im1, im2):

    fig = plt.figure(1, (4., 4.))
    grid = ImageGrid(fig, 111,  # similar to subplot(111)
                     nrows_ncols=(1, 2),  # creates 2x2 grid of axes
                     axes_pad=0,  # pad between axes in inch.
                     )

    grid[0].imshow(im1)
    grid[1].imshow(im2)

    plt.show()