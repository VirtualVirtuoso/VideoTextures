import cv2
import numpy
import os

import util.video.keyframes as keyframes
import util.frame.compare as compare
import config as c
import definitions as d

frameCount = 0

# This is the first pre-processing step we use to determine the similarities between
# each frame of the video. We then store this in a matrix, which we can then turn into
# probabilities and threshold in the next step.
def main():
    print d.bar_line
    print "OpenCV version :  {0}".format(cv2.__version__)
    print d.bar_line
    print ""
    print "Determining similarities between frames..."
    input_matrix = os.path.join(d.ROOT_DIR, c.inputPath)
    build_similarity_matrix(input_matrix)

def build_similarity_matrix(video):

    # We create two video objects, each of which will scan one frame
    video_1 = cv2.VideoCapture(video)
    video_2 = cv2.VideoCapture(video)

    # We then determine the number of frames, so we can iterate to that point
    global frameCount
    frameCount = keyframes.count_frames(video)

    print "We have ", frameCount, " frames to process. Skipping ", c.skipFrames - 1, " frames at a time..."
    print ""

    # Instantiate the matrix in which we will determine the similarities
    height = (frameCount / c.skipFrames) - 1
    width = (frameCount / c.skipFrames) - 1
    sim_matrix = numpy.zeros((height, width))

    # Go through each of the frames, and find their similarity with others
    for x in range(0, frameCount - 1, c.skipFrames):
        print "Analyzing frame ", x + 1, "/", frameCount, " ..."

        video_1.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, x + 1)
        (x_success, frame_x) = video_1.read()

        for y in range(0, frameCount - 1, c.skipFrames):
            video_2.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, y + 1)
            (y_success, frame_y) = video_2.read()

            # We make our comparison based on the Euclidean (L2) norm
            sim_matrix[x / c.skipFrames, y / c.skipFrames] = compare.euclidean_norm(frame_x, frame_y)

    # Save this to a file, so we can process the results later
    print "Saved output to 'data/output/difference_matrix.csv'... "
    numpy.savetxt("../data/output/difference_matrix.csv", sim_matrix, delimiter=",")

    return sim_matrix

if __name__ == "__main__":
    main()