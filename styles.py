import tkinter as tk
from tkinter import ttk

def apply_styles(root):
    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 12), padding=10)
    style.configure('TLabel', font=('Helvetica', 14))
    root.option_add("*TButton*Font", "Helvetica 12")
    root.option_add("*TLabel*Font", "Helvetica 14")
    root.option_add("*TLabel*Foreground", "#333")
    root.option_add("*TButton*Foreground", "#333")
    root.option_add("*TButton*Background", "#EEE")
