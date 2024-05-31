import tkinter as tk
from tkinter import ttk
from threading import Thread
from image_data_gather import collect_images, get_user_id
from face_training import train_model
from face_recognizer import recognize_faces
from styles import apply_styles

def create_main_ui():
    root = tk.Tk()
    root.title("Face Recognition System")
    root.geometry("500x400")

    apply_styles(root)

    main_frame = ttk.Frame(root, padding="10")
    main_frame.pack(fill='both', expand=True)

    title_label = ttk.Label(main_frame, text="Face Recognition System", font=('Helvetica', 18, 'bold'))
    title_label.pack(pady=20)

    collect_button = ttk.Button(main_frame, text="Collect Images", command=lambda: [get_user_id(), Thread(target=collect_images).start()])
    collect_button.pack(pady=10)

    train_button = ttk.Button(main_frame, text="Train Model", command=lambda: Thread(target=train_model).start())
    train_button.pack(pady=10)

    recognize_button = ttk.Button(main_frame, text="Recognize Faces", command=recognize_faces)
    recognize_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_main_ui()
