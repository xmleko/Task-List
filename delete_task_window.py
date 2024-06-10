import tkinter as tk
class DeleteTaskWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Delete Task")
        self.geometry("400x270")

