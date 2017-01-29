import cv2
import numpy
import util.video.keyframes as keyframes
import util.frame.compare as compare

def main():
    print "Determining similarities between frames..."
    build_similarity_matrix("data/shorter.mov")

def build_similarity_matrix(video):
    video_1 = cv2.VideoCapture(video)
    video_2 = cv2.VideoCapture(video)

    frame_count = keyframes.count_frames(video)

    sim_matrix = numpy.zeros((frame_count, frame_count))

    # Go through each of the frames, and find their similarity with others
    for x in range(0, frame_count - 1):
        print "Analyzing frame ", x + 1, "/", frame_count, " ..."

        video_1.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, x + 1)
        (x_success, frame_x) = video_1.read()

        for y in range(0, frame_count - 1):
            video_2.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, y + 1)
            (y_success, frame_y) = video_2.read()

            sim_matrix[x, y] = compare.euclidean_norm(frame_x, frame_y)


    print "Saved output to 'data/output/difference_matrix.csv'... "
    numpy.savetxt("data/output/difference_matrix.csv", sim_matrix, delimiter=",")

    return sim_matrix

if __name__ == "__main__":
    main()