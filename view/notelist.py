import tkinter as tk
from tkinter import ttk


class NoteListUi:

    def __init__(self, frame, add_note, save_note_with_title, remove_note_with_title, select_note):
        self.frame = frame

        self.note_list = tk.Listbox(self.frame, width=30, height=15)
        self.note_list.select_note = select_note
        self.note_list.bind('<<ListboxSelect>>', self.on_click_note_list)

        self.menu_frame = ttk.Labelframe(self.frame)
        self.menu_frame.pack()
        self.create_button = tk.Button(self.menu_frame, text="Create", command=add_note)
        self.create_button.pack(side="left")
        self.update_button = tk.Button(self.menu_frame, text="Update", command=lambda: self.on_click_update_button(save_note_with_title))
        self.update_button.pack(side="left")
        self.remove_button = tk.Button(self.menu_frame, text="Remove", command=lambda: self.on_click_remove_button(remove_note_with_title))
        self.remove_button.pack(side="left")
        
        self.note_list.pack()


    def on_click_update_button(self, update_note_with_title):
        update_note_with_title(self.note_list.get(tk.ACTIVE))


    def on_click_remove_button(self, remove_note_with_title):
        remove_note_with_title(self.note_list.get(tk.ACTIVE))


    def on_click_note_list(self, event):
        if self.note_list.curselection():
            self.note_list.select_note(self.note_list.get(self.note_list.curselection()))