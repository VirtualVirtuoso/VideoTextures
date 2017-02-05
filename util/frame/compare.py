import numpy.linalg

from scipy import average

def manhattan_norm(frame1, frame2):
    manhattan, euclidean = compare_frames(frame1, frame2)
    return manhattan


def euclidean_norm(frame1, frame2):
    manhattan, euclidean = compare_frames(frame1, frame2)
    return euclidean

def compare_frames(img1, img2):

    img_1_grayscale = to_grayscale(img1)
    img_2_grayscale = to_grayscale(img2)
    diff = img_1_grayscale - img_2_grayscale

    manhattan_norm_scalar = sum(abs(diff))
    euclidean_norm_scalar = numpy.linalg.norm(diff, 'fro')
    return [manhattan_norm_scalar, euclidean_norm_scalar]

def to_grayscale(frame):
    if len(frame.shape) == 3:
        return average(frame, -1)
    else:
        return frame

def normalize(frame):
    colour_range = frame.max() - frame.min()
    frame_min = frame.min()
    return ((frame - frame_min) * 255) / colour_range
