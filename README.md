<h1>Webcam Motion Detection Project</h1>  

**Preview 0.1**

The goal of this project was to learn the basics of the OpenCV Library. 
The end result is an application that is capable of opening the first video input
device of the user and using it to capture frames.

The program also creates a green rectangle around objects entering the
frame. This capability is done by the capturing the first frame
and using it as a background. After which the program compares the
current frames (by modifying the frames into grayscale and creating
thresholds to reduce noise) to the background to check for differences.

The program then saves the timestamp of the objects entering and exiting
the frame to a .csv file.

**Known issues**
<ul>
<li>Timestamp start and end dates for objects need visualization</li>
</ul>

