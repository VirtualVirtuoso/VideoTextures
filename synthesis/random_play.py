import cv2

import config as c
import definitions as d
import util.video.keyframes as kf

import util.mathematics.matrix as matrix
import util.mathematics.weighted_choice as frame_chooser
import config as c

def main():

    (cap, position_frame) = kf.source_video(c.absInputPath)
    frame_probabilities = matrix.load_matrix("thresholds")
    choice_labels = frame_chooser.generate_choices(frame_probabilities)

    window_name = d.random_play
    cv2.namedWindow(window_name, cv2.WINDOW_OPENGL)
    cv2.startWindowThread()
    frameskip = c.skipFrames
    preserve_jump = frameskip
    next_frame = 0

    while True:
        flag, frame = cap.read()
        if flag:
            cv2.imshow(window_name, frame)
            position_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
        else:
            cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, position_frame - 1)
            print d.frame_not_ready
            cv2.waitKey(1000)

        if preserve_jump == 0:
            next_frame = find_random_frame(cap, frame_probabilities, choice_labels)
            preserve_jump = frameskip
        else:
            next_frame += 1
            preserve_jump -= 1

        cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, next_frame)
        cv2.waitKey(50)

        # Terminate the program if ESC is pressed
        if cv2.waitKey(10) == 27:
            cv2.destroyAllWindows()
            break

        # Terminate the program if window is closed
        if cv2.getWindowProperty(window_name, 0) == -1:
            cv2.destroyAllWindows()
            break

def find_random_frame(cap, matrix, choice_labels):
    frame_num = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)

    # TODO: This shouldn't be necessary if the row is normalised
    return frame_chooser.choose_frame(matrix, choice_labels, frame_num * c.skipFrames)

if __name__ == "__main__":
    main()
