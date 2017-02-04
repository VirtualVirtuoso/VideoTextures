import cv2
import numpy
import util.video.keyframes as keyframes
import util.frame.compare as compare

skipFrames = 5

# This is the first pre-processing step we use to determine the similarities between
# each frame of the video. We then store this in a matrix, which we can then turn into
# probabilities and threshold in the next step.
def main():
    print "Determining similarities between frames..."
    build_similarity_matrix("data/jurassic.mov")

def build_similarity_matrix(video):

    # We create two video objects, each of which will scan one frame
    video_1 = cv2.VideoCapture(video)
    video_2 = cv2.VideoCapture(video)

    # We then determine the number of frames, so we can iterate to that point
    frame_count = keyframes.count_frames(video)

    # Instantiate the matrix in which we will determine the similarities
    sim_matrix = numpy.zeros((frame_count / skipFrames, frame_count / skipFrames))

    # Go through each of the frames, and find their similarity with others
    for x in range(0, frame_count - 1, skipFrames):
        print "Analyzing frame ", x + 1, "/", frame_count, " ..."

        video_1.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, x + 1)
        (x_success, frame_x) = video_1.read()

        for y in range(0, frame_count - 1, skipFrames):
            video_2.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, y + 1)
            (y_success, frame_y) = video_2.read()

            # We make our comparison based on the Euclidean (L2) norm
            sim_matrix[x / skipFrames, y / skipFrames] = compare.euclidean_norm(frame_x, frame_y)

    # Save this to a file, so we can process the results later
    print "Saved output to 'data/output/difference_matrix.csv'... "
    numpy.savetxt("data/output/difference_matrix.csv", sim_matrix, delimiter=",")

    return sim_matrix

if __name__ == "__main__":
    main()