import cv2
import sys
import numpy

from scipy.spatial import distance
from scipy import average

def manhattan_norm(frame1, frame2):
    manhattan, euclidean = compare_frames(frame1, frame2)
    return manhattan


def euclidean_norm(frame1, frame2):
    manhattan, euclidean = compare_frames(frame1, frame2)
    return euclidean

def compare_frames(img1, img2):

    diff = to_grayscale(img1) - to_grayscale(img2)

    manhattan_norm = sum(abs(diff))
    euclidean_norm = numpy.linalg.norm(diff, 2)
    return (manhattan_norm, euclidean_norm)

def to_grayscale(frame):
    if len(frame.shape) == 3:
        return average(frame, -1)
    else:
        return frame

def normalize(frame):
    range = frame.max() - frame.min()
    frame_min = frame.min()
    return(frame - frame_min)*255/range
