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

def source_video(path_of_video):
    cap = cv2.VideoCapture(path_of_video)

    while not cap.isOpened():
        cap = cv2.VideoCapture(path_of_video)
        cv2.waitKey(1000)
        print "Loading video..."

    position_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)

    return cap, position_frame
