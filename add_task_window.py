import tkinter as tk
from controller import Controller

class AddTaskWindow(tk.Toplevel):
    def __init__(self, controller, main_window):
        super().__init__()
        self.title("Add Task")
        self.geometry("450x300")
        self.controller = controller
        self.main_window = main_window
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, width=3, height=3, font=("Arial", 14),  text="Title")
        self.title_label.pack()
        self.description = tk.Text(self, width=35, height=5, font=("Arial", 14))
        self.description.pack()
        self.space_label = tk.Label(self, height=1)
        self.space_label.pack()
        self.button_add = tk.Button(self, width=8, height=2, font=("Arial", 12),  text="Add Task", command = self.send_task)
        self.button_add.pack()

    def send_task(self):
        task = self.description.get("1.0", tk.END)
        self.controller.add_task(task, "Awaiting")
        self.main_window.update_task_list()
        self.destroy()



##





