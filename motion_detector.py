import cv2
import pandas
from datetime import datetime

# undefined variable to store the background
bg_frame = None

# open webcam
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# lists for storing the timestamp of objects entering/exiting the frame
status_list = [None, None]
timestamp_list = []
df = pandas.DataFrame(columns=["Start", "End"])

while True:
    check, frame = video.read()
    status = 0
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
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0))

    status_list.append(status)

    if status_list[-1] == 1 and status_list[-2] == 0:
        timestamp_list.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        timestamp_list.append(datetime.now())

    # show frames
    #cv2.imshow("Gray Frame", gray_frame)
    #cv2.imshow("Delta Frame", delta_frame)
    #cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(100)

    if key == ord('q'):
        if status == 1:
            timestamp_list.append(datetime.now())
        break

# mapping the timestamps to a dataframe
for i in range(0, len(timestamp_list), 2):
    df = df.append({"Start": timestamp_list[i], "End": timestamp_list[i+1]}, ignore_index=True)

df.to_csv("Timestamp.csv")
video.release()
cv2.destroyAllWindows()