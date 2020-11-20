import cv2
vidcap = cv2.VideoCapture('video.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 0.5 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
#
# In cv2.VideoCapture(‘video.mp4’), we just have to mention the video name with it’s extension. Here my video name is “video.mp4”. You can set frame rate which is widely known as fps (frames per second). Here I set 0.5 so it will capture a frame at every 0.5 seconds, means 2 frames (images) for each second.
# It will save images with name as image1.jpg, image2.jpg and so on.


import cv2
import numpy as np
import os
from os.path import isfile, join
pathIn= './images/testing/'
pathOut = 'video.avi'
fps = 0.5
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
#for sorting the file names properly
files.sort(key = lambda x: x[5:-4])
files.sort()
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
#for sorting the file names properly
files.sort(key = lambda x: x[5:-4])
for i in range(len(files)):
    filename=pathIn + files[i]
    #reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)

    #inserting the frames into an image array
    frame_array.append(img)
out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()
# Explanation:
# Using this code we can generate video from Images (Frames). We have to add pathIn (path of the folder which contains all the images). I set framerate with 0.5 so it will take 2 images for 1 second.)
# It will generate output video in any format. (eg.: .avi, .mp4, etc.)
# !!! Please take care that all images are in sequence like image1.jpg, image2.jpg and so on.
