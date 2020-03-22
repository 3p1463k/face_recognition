import os
import datetime as dt
from picamera import PiCamera
from signal import pause
from time import sleep
destination = '/home/pi/video'
camera = PiCamera()
#sensor = MotionSensor(4)

def record_video():
    filename = os.path.join(destination, dt.datetime.now().strftime('%Y-%m-%d_%H.%M.%S.h264'))
    camera.start_preview()
    camera.start_recording(filename)

def finish_video():
    camera.stop_recording()
    camera.stop_preview()

for i in range(1):
	record_video
	sleep(60)
	finish_video
	pause()