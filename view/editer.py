import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


class EditerUi:

    def __init__(self, frame, clear_editer):
        self.frame = frame
        self.title_frame = ttk.Labelframe(self.frame)
        self.title_frame.pack(padx=10, pady=10)

        self.title = tk.Entry(self.title_frame)
        self.title.pack(side="left")
        self.clear_button = tk.Button(self.title_frame, text="Clear", command=clear_editer)
        self.clear_button.pack(side="left", padx=10, pady=10)

        self.scrolled_text = ScrolledText(self.frame)
        self.scrolled_text.pack(padx=10, pady=10, ipadx=55, ipady=120)