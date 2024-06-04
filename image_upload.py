import tkinter as tk
from tkinter import filedialog, messagebox
import face_recognition
from PIL import Image, ImageTk

def upload_and_recognize_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]
    )
    if not file_path:
        return

    try:
        image = face_recognition.load_image_file(file_path)
        face_locations = face_recognition.face_locations(image)

        if not face_locations:
            messagebox.showinfo("Result", "No faces found in the uploaded image.")
        else:
            messagebox.showinfo("Result", f"Found {len(face_locations)} face(s) in the uploaded image.")
            # Display the detected face
            display_detected_face(image, face_locations)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def display_detected_face(image, face_locations):
    image_window = tk.Toplevel()
    image_window.title("Detected Face")
    image_window.geometry("600x600")

    for face_location in face_locations:
        top, right, bottom, left = face_location
        # Crop the detected face
        face_image = image[top:bottom, left:right]
        # Convert the face image to a PIL Image
        pil_image = Image.fromarray(face_image)
        # Convert the PIL Image to a Tkinter-compatible image
        tk_image = ImageTk.PhotoImage(pil_image)

        panel = tk.Label(image_window, image=tk_image)
        panel.image = tk_image
        panel.pack()


def display_image(image_path):
    image_window = tk.Toplevel()
    image_window.title("Uploaded Image")
    image_window.geometry("600x600")

    img = Image.open(image_path)
    img = img.resize((500, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    panel = tk.Label(image_window, image=img)
    panel.image = img
    panel.pack()
