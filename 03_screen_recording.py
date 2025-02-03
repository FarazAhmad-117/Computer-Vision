# Making a screen recorder

import cv2 as c
import pyautogui as p
import numpy as np

# Create resolution
rs = p.size()

# filename in which store recording
# fn = input("Please enter any filename and Path")

fn = "/output/screen_recording.avi"

# Fix the frame rate
fps = 20.0

fourcc = c.VideoWriter_fourcc(*"XVID")
output = c.VideoWriter(fn, fourcc, fps, rs)


# Create a recording module
c.namedWindow("Live_Recording", c.WINDOW_NORMAL)
c.resizeWindow("Live_Recording", (700, 400))


while True:
    # Capture frame-by-frame
    img = p.screenshot()
    f = np.array(img)
    f = c.cvtColor(f, c.COLOR_BGR2BGR)
    output.write(f)
    c.imshow("Live_Recording", f)
    if c.waitKey(1) & 0xFF == ord("q"):
        break

output.release()
c.destroyAllWindows()
