from pi_video_stream import PiVideoStream
import time
import cv2

# created a *threaded *video stream, allow the camera sensor to warmup
vs = PiVideoStream().start()
time.sleep(2.0)

while True:
    # convert img as Array
    image = vs.read()
    # kind of 'wait for key'
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    # Show image
    cv2.imshow("Camera", image)
    
vs.stop()
