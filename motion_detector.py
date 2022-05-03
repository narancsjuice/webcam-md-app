import cv2

# undefined variable to store the background
bg_frame = None

# open webcam
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    check, frame = video.read()

    # change color to black & white and blur image to remove noise
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # capture first frame as background and restart loop
    if bg_frame is None:
        bg_frame = gray_frame
        continue

    # create a difference frame
    delta_frame = cv2.absdiff(bg_frame, gray_frame)

    cv2.imshow("Video Cap", gray_frame)
    cv2.imshow("Delta Frame", delta_frame)

    key = cv2.waitKey(100)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()