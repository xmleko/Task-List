import tkinter as tk
from add_task_window import AddTaskWindow
from tkinter import Button
from controller import Controller

class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("630x490")
        self.title("Task List")
        self.controller = Controller()
        self.create_labels()
        self.button_add_task()

    def create_labels(self):
        self.number_label = tk.Label(self, text="#")
        self.number_label.grid(row = 0, column = 0, padx=20, pady=120)
        self.task_name_label = tk.Label(self, text="Task Name")
        self.task_name_label.grid(row = 0, column = 1, padx=50, pady=120)
        self.status_label = tk.Label(self, text="Status")
        self.status_label.grid(row = 0, column = 2, padx=50, pady=120)
        self.edit_label = tk.Label(self, text="Edit")
        self.edit_label.grid(row = 0, column = 3, padx=50, pady=120)
        self.remove_label = tk.Label(self, text="Remove")
        self.remove_label.grid(row = 0, column = 4, padx=50, pady=120)

    def button_add_task(self):
        self.button_add = Button(self, text="Add Task", width=10, height=3, command=self.open_add_task_window)
        self.button_add.place(x=20, y=20)

    def open_add_task_window(self):
        add_task_window = AddTaskWindow(self.controller)


