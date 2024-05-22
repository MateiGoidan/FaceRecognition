import cv2

# Using a set of images create the training set for a specific person

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

face_id = input("\n enter user id end press <return> ==>  ")
count = 0

print(
    "\n ATTENTION!: For the following picturtes press [y] in order to save the 'face' or [n] to discard it\n\n"
)

for i in range(1, 4):
    path = "rawdata/Eliza" + str(i) + ".jpg"
    image = cv2.imread(path)
    # Check if the image is loaded successfully
    if image is None:
        print(f"ERROR: Image at path {path} could not be loaded.")
        continue

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,  # Gray sclae the imag
        scaleFactor=1.2,  # How much the image size is reduced
        minNeighbors=5,  # Number of neighbors each candidate rectangle should have
        minSize=(20, 20),  # The minimum rectangle size to be considered a face
    )

    if faces is ():
        print("ERROR: No face detected!")

    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Face Detection", image)

        while True:
            k = cv2.waitKey(10) & 0xFF  # Press 'ESC' for exiting video
            if k == ord("y"):
                # Save the captured image into the datasets folder
                count += 1
                cv2.imwrite(
                    "dataset/User." + str(face_id) + "." + str(count) + ".jpg",
                    gray[y : y + h, x : x + w],
                )
                break
            elif k == ord("n"):
                break

    cv2.destroyAllWindows()
