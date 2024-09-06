import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width=GetSystemMetrics(0)
height=GetSystemMetrics(1)

dim=(width,height)
f=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter("recorded.mp4",f,7.0,dim)
now_time=time.time()
dur=int(input("Enter no. of seconds you want to record the video: "))
end_time=now_time+dur

while True:
    image=pyautogui.screenshot()
    frame=np.array(image)
    frame_color=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output.write(frame_color)
    c_time=time.time()
    if c_time>end_time:
        break
output.release()
print("------Video Recorded Successfully-------")