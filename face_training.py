import os
import cv2
from PIL import Image
import numpy as np
import pickle
from tkinter import messagebox

def train_model():
    dataset_path = os.path.join(r"C:\Users\Rix\Desktop\AI NLP\FaceRecognition", 'dataset')
    trainer_path = os.path.join(r"C:\Users\Rix\Desktop\AI NLP\FaceRecognition", 'trainer', 'trainer.yml')
    labels_path = os.path.join(r"C:\Users\Rix\Desktop\AI NLP\FaceRecognition", 'trainer', 'labels.pickle')

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    if os.path.exists(trainer_path) and os.path.exists(labels_path):
        recognizer.read(trainer_path)
        with open(labels_path, 'rb') as f:
            labels_dict = pickle.load(f)
        current_id = max(labels_dict.values()) + 1
    else:
        labels_dict = {}
        current_id = 0

    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def getImagesAndLabels(path, current_id, labels_dict):
        faceSamples = []
        ids = []

        for root, dirs, files in os.walk(path):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                if dir_name not in labels_dict:
                    labels_dict[dir_name] = current_id
                    current_id += 1
                id_ = labels_dict[dir_name]
                for file in os.listdir(dir_path):
                    if file.endswith(".jpg"):
                        imagePath = os.path.join(dir_path, file)
                        print(f"[INFO] Processing file: {imagePath}")
                        PIL_img = Image.open(imagePath).convert("L")  # grayscale
                        img_numpy = np.array(PIL_img, "uint8")
                        faces = detector.detectMultiScale(img_numpy)

                        for (x, y, w, h) in faces:
                            faceSamples.append(img_numpy[y:y + h, x:x + w])
                            ids.append(id_)

        return faceSamples, ids

    faces, ids = getImagesAndLabels(dataset_path, current_id, labels_dict)
    recognizer.train(faces, np.array(ids))
    if not os.path.exists(os.path.dirname(trainer_path)):
        os.makedirs(os.path.dirname(trainer_path))
    recognizer.write(trainer_path)

    with open(labels_path, 'wb') as f:
        pickle.dump(labels_dict, f)

    messagebox.showinfo("Info", "Training complete. Model and labels saved.")
