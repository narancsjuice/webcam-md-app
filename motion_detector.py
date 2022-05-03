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

    # create difference and threshold frames
    delta_frame = cv2.absdiff(bg_frame, gray_frame)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=3)

    # find the contour
    (cntrs, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # if contour is bigger than 1000 pixels, draw rectangle for current frame
    for contour in cntrs:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0))

    # show frames
    cv2.imshow("Gray Frame", gray_frame)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(100)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()