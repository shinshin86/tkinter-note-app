import tkinter as tk
import tkinter.messagebox as tkm
import signal
from tkinter import ttk, HORIZONTAL
from datetime import datetime
from view.notelist import NoteListUi
from view.editer import EditerUi
from model.db import init_db_table, create_note, get_all_note, remove_note, get_note, update_note


class App:

    def __init__(self, root):
        self.root = root
        root.title("Note app")
        root.geometry("1000x700")

        # Create PanedWindow.
        vertical_pane = ttk.PanedWindow(self.root, orient=HORIZONTAL)
        vertical_pane.grid(row=0, column=0, sticky="nsew")
        horizontal_pane = ttk.PanedWindow(vertical_pane, orient=HORIZONTAL)
        vertical_pane.add(horizontal_pane)

        note_list_frame = ttk.Labelframe(vertical_pane, text="Note List")
        vertical_pane.add(note_list_frame, weight=1)

        editer_frame = ttk.Labelframe(vertical_pane, text="Editer")
        vertical_pane.add(editer_frame, weight=1)

        self.notelist = NoteListUi(note_list_frame, self.add_note, self.update_note_with_title, self.remove_note_with_title, self.select_note)
        self.editer = EditerUi(editer_frame, self.clear_editer)

        self.get_note_list()

        # Handling of application termination.
        self.root.protocol('WM_DELETE_WINDOW', self.root.quit)
        self.root.bind('<Control-q>', self.root.quit)
        signal.signal(signal.SIGINT, self.root.quit)


    def clear_editer(self):
        self.editer.title.delete(0, tk.END)
        self.editer.scrolled_text.delete('1.0', tk.END)


    def refresh_note_list(self):
        note_list = get_all_note()

        self.notelist.note_list.delete(0, tk.END)
        for note in note_list:
            self.notelist.note_list.insert(tk.END, note['title'])


    def add_note(self):
        if self.editer.title.get() == "":
            tkm.showinfo("Create Error", "Title is required.")
            return

        create_note(self.editer.title.get(), self.editer.scrolled_text.get("1.0", tk.END))
        self.refresh_note_list()
        self.clear_editer()


    def update_note_with_title(self, title):
        if self.editer.title.get() == "":
            tkm.showinfo("Create Error", "Title is required.")
            return

        note_list = get_all_note()
        target_note = next((note for note in note_list if note["title"] == title), None)
        update_note(target_note["id"], self.editer.title.get(), self.editer.scrolled_text.get("1.0", tk.END))
        self.refresh_note_list()


    def get_note_list(self):
        note_list = get_all_note()

        for note in note_list:
            self.notelist.note_list.insert(tk.END, note['title'])


    def refresh_editer(self, note):
        self.clear_editer()
        self.editer.title.insert(tk.END, note["title"])
        self.editer.scrolled_text.insert(tk.END, note["text"])


    def select_note(self, title):
        note_list = get_all_note()
        target_note = next((note for note in note_list if note["title"] == title), None)
        note = get_note(target_note["id"])
        self.refresh_editer(note)


    def remove_note_with_title(self, title):
        note_list = get_all_note()
        target_note = next((note for note in note_list if note["title"] == title), None)

        if tkm.askokcancel("Remove note", "Remove note: " + target_note["title"]):
            remove_note(target_note["id"])
            self.refresh_note_list()


def main():
    init_db_table()
    root = tk.Tk()
    app = App(root)
    app.root.mainloop()


if __name__ == "__main__":
    main()