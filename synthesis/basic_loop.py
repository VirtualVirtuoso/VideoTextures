import cv2

import config as c
import definitions as d
import util.video.keyframes as kf

"""
|-------------------------------------------------------------------------------
| Basic Loop
|-------------------------------------------------------------------------------
|
| This is the most trivial execution. Once you reach the end of the video, you
| begin back at the beginning. This is similar to the gif image format.
|
"""

def main():

    # Load the video and the frame we're currently at
    (cap, position_frame) = kf.source_video(c.absInputPath)

    # Generate the output window
    window_name = d.basic_loop_play
    cv2.namedWindow(window_name, cv2.WINDOW_OPENGL)
    cv2.startWindowThread()

    # Keep reading the frames, and outputting them
    while True:
        flag, frame = cap.read()

        if flag:
            cv2.imshow(window_name, frame)
            position_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
        else:
            cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, position_frame - 1)
            print d.frame_not_ready
            cv2.waitKey(1000)

        # Terminate the program if ESC is pressed
        if cv2.waitKey(10) == 27:
            cv2.destroyAllWindows()
            break

        # Terminate the program if the window is closed
        if cv2.getWindowProperty(window_name, 0) == -1:
            cv2.destroyAllWindows()
            break

        # If we get to the end of the video, start again from the beginning
        if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
            cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, 0)



if __name__ == "__main__":
    main()
