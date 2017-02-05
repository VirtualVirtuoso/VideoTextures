import cv2

def count_frames(video):
    cap = cv2.VideoCapture(video)
    length = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    return length

def get_frame(video, frame_no):
    cap = cv2.VideoCapture(video)
    frame_rate = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    print "Framerate: ", frame_rate
    frame_time = 1000.0 * frame_no / frame_rate
    cap.set(cv2.cv.CV_CAP_PROP_POS_MSEC, frame_time)

    (success, frame) = cap.read()
    return frame
