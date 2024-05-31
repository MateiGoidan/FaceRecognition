import cv2

# Test for a specific image if the model can correctly detect the face
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Load the image for detecting the face
image = cv2.imread('C:/Users/Rix/Desktop/AI NLP/FaceRecognition/rawdata/User.5.2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Get the ROI
faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Tuple

# Check for errors
if faces == ():
    print("Error: No face detected!")
    quit()

# Draw the rectangle on the face
for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Face Detection", image)
    while True:
        k = cv2.waitKey(10) & 0xFF  # Press 'ESC' for exiting video
        if k == 27:
            break

# Cleanup
cv2.destroyAllWindows()
