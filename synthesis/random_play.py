import cv2

import config as c
import definitions as d
import util.video.keyframes as kf

def main():

    (cap, position_frame) = kf.source_video(c.absInputPath)

    window_name = d.random_play
    cv2.namedWindow(window_name, cv2.WINDOW_OPENGL)
    cv2.startWindowThread()

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

        # Terminate the program if window is closed
        if cv2.getWindowProperty(window_name, 0) == -1:
            cv2.destroyAllWindows()
            break

        # Terminate program if we get to the end of the video
        if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()