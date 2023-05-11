import cv2

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Open the default camera
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video capture")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame was successfully captured
    if not ret:
        print("Error reading video frame")
        break

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Write the frame to the output file
    out.write(frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture and writer objects
cap.release()
out.release()

# Close all windows
cv2.destroyAllWindows()