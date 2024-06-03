import cv2

<<<<<<< Updated upstream
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")

faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

font = cv2.FONT_HERSHEY_SIMPLEX

# Iniciate id counter
id = 0

# List of names related to the ids
names = ["None", "Matei", "Rachel", "Eliza", "Z", "W"]

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video widht
cam.set(4, 480)  # set video height

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y : y + h, x : x + w])

        # If confidence is less them 100 ==> "0" : perfect match
        if confidence < 100:
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow("camera", img)
    k = cv2.waitKey(10) & 0xFF  # Press 'ESC' for exiting video
    if k == 27:
        break

print("\n [INFO] Exiting Program and cleanup stuff")

# Cleanup
cam.release()
cv2.destroyAllWindows()
=======
def recognize_faces():
    try:
        print("Starting face recognition...")
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(r"C:\Users\User\Documents\GitHub\FaceRecognition\trainer\trainer.yml")

        with open(r"C:\Users\User\Documents\GitHub\FaceRecognition\trainer\labels.pickle", 'rb') as f:
            labels_dict = pickle.load(f)
            labels_dict = {v: k for k, v in labels_dict.items()}  # Invert the dictionary

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        font = cv2.FONT_HERSHEY_SIMPLEX
        cam = cv2.VideoCapture(0)
        cam.set(3, 640)  # set video width
        cam.set(4, 480)  # set video height

        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        while True:
            ret, img = cam.read()
            if not ret:
                print("Failed to capture image")
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
            )

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id_, confidence = recognizer.predict(gray[y:y + h, x:x + w])

                if confidence < 100:
                    name = labels_dict.get(id_, "Unknown")
                    confidence_text = f"  {round(100 - confidence)}%"
                else:
                    name = "Unknown"
                    confidence_text = f"  {round(100 - confidence)}%"

                cv2.putText(img, str(name), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
                cv2.putText(img, str(confidence_text), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

            cv2.imshow('camera', img)
            k = cv2.waitKey(10) & 0xFF  # Press 'ESC' for exiting video
            if k == 27:
                break

        cam.release()
        cv2.destroyAllWindows()
        print("Face recognition finished.")
    except Exception as e:
        print(f"An error occurred: {e}")
>>>>>>> Stashed changes
