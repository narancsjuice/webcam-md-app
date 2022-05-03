import cv2
# open webcam
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    check, frame = video.read()

    # change color to black & white
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Video Cap", gray_frame)

    key = cv2.waitKey(100)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()