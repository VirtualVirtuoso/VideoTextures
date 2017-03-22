import numpy.linalg

from scipy import average

"""
|-------------------------------------------------------------------------------
| Frame Util
|-------------------------------------------------------------------------------
|
| A collection of utilities which allow us to manipulate frames, and compare
| them to one another
|
"""

"""
| Returns the Manhattan distance between two gray frames
"""
def manhattan_norm(frame1, frame2):
    manhattan, euclidean = compare_frames(frame1, frame2)
    return manhattan

"""
| Returns the Euclidean distance between two gray frames
"""
def euclidean_norm(frame1, frame2):
    manhattan, euclidean = compare_frames(frame1, frame2)
    return euclidean

"""
| Returns the Manhatten and Euclidean distance between two given frames
"""
def compare_frames(img1, img2):

    img_1_grayscale = to_grayscale(img1)
    img_2_grayscale = to_grayscale(img2)
    diff = img_1_grayscale - img_2_grayscale

    manhattan_norm_scalar = sum(abs(diff))
    euclidean_norm_scalar = numpy.linalg.norm(diff, 'fro')
    return [manhattan_norm_scalar, euclidean_norm_scalar]

"""
| Converts a frame to grayscale
"""
def to_grayscale(frame):
    if len(frame.shape) == 3:
        return average(frame, -1)
    else:
        return frame

"""
| Normalises the colour of the given frame
"""
def normalize(frame):
    colour_range = frame.max() - frame.min()
    frame_min = frame.min()
    return ((frame - frame_min) * 255) / colour_range
