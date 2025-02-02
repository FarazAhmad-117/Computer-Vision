import cv2

"""
cap = cv2.VideoCapture("./sample.mp4")

print("cap", cap)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (600, 400))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)
    cv2.imshow("frame", frame)
    k = cv2.waitKey(2)
    if k == ord("q") & 0xFF:
        break

cap.release()
cv2.destroyAllWindows()
"""

# Now capture video from the web camera and save it to the storage

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not access the webcam!")
    exit()

# Define codec and create VideoWriters
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("./output/output.avi", fourcc, 20.0, (600, 400))
output_g = cv2.VideoWriter("./output/output_g.avi", fourcc, 20.0, (600, 400))

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Error: Failed to read frame!")
        break

    # Resize and flip the frame
    frame = cv2.resize(frame, (600, 400))
    frame = cv2.flip(frame, 1)

    # Convert to grayscale & back to BGR
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # Write to video files
    output.write(frame)
    output_g.write(gray_bgr)

    # Display frames
    cv2.imshow("gray", gray)
    cv2.imshow("frame", frame)

    # Quit on 'q' key press
    k = cv2.waitKey(20) & 0xFF
    if k == ord("q"):
        break

# Release resources
cap.release()
output.release()
output_g.release()
cv2.destroyAllWindows()
