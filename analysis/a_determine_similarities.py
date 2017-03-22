import cv2
import numpy
import os
import math

import util.video.keyframes as keyframes
import util.frame.compare as compare
import config as c
import definitions as d
import util.mathematics.matrix as matrix_util

'''
|-------------------------------------------------------------------------------
| Determining Similarities
|-------------------------------------------------------------------------------
|
| This is the first pre-processing step we use to determine the similarities
| between each frame of the video. We then store this result in a matrix,
| which is needed for further computations while determining feasible
| transitions between frames.
|
'''

def main():

    print d.BAR_LINE
    print "OpenCV version :  {0}".format(cv2.__version__)
    print d.BAR_LINE
    print d.EMPTY_LINE
    print "Determining similarities between frames..."

    # Find the input path for the video, and build the difference matrix
    input_video_path = os.path.join(d.ROOT_DIR, c.inputPath)
    diff_matrix = build_difference_matrix(input_video_path)

    # Save this to a file, so we can process the results later
    print "Saved output to 'data/output/difference_matrix.csv'... "
    matrix_util.save_matrix(diff_matrix, "differences")

    # Optional visualisation for the matrix using the built in GUI
    if c.displayVisualisations:
        matrix_util.display_matrix(diff_matrix, "Difference Matrix")

'''
| This function takes an input video, and then compares each of the frames against every
| other frame. It considers each frame a two dimensional array, and then determines the
| Euclidean distance between the frames.
'''
def build_difference_matrix(video):

    # We create two video objects, each of which will scan one frame
    video_1 = cv2.VideoCapture(video)
    video_2 = cv2.VideoCapture(video)

    # We then determine the number of frames, so we can iterate to that point
    frame_count = keyframes.count_frames(video)

    print "We have ", frame_count, " frames to process. Skipping ", c.skipFrames - 1, " frames at a time..."
    print ""

    # Instantiate the matrix in which we will determine the similarities
    height = (frame_count / c.skipFrames) + c.matrixBuffer
    width = (frame_count / c.skipFrames) + c.matrixBuffer
    sim_matrix = numpy.zeros((height, width))

    # Go through each of the frames, and find their similarity with others
    for x in range(0, frame_count - 1, c.skipFrames):
        print "Analyzing frame ", x + 1, "/", frame_count, " ..."

        video_1.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, x + 1)
        (x_success, frame_x) = video_1.read()

        for y in range(0, frame_count - 1, c.skipFrames):
            video_2.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, y + 1)
            (y_success, frame_y) = video_2.read()

            adjusted_x = int(math.floor(x / c.skipFrames))
            adjusted_y = int(math.floor(y / c.skipFrames))

            # We make our comparison based on the Euclidean (L2) norm
            sim_matrix[adjusted_x, adjusted_y] = compare.euclidean_norm(frame_x, frame_y)

    return sim_matrix

if __name__ == "__main__":
    main()
