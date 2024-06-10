import tkinter as tk
from add_task_window import AddTaskWindow
from delete_task_window import DeleteTaskWindow
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

    def update_task_list(self):
        for index, task in enumerate(self.controller.tasks):
            self.number = tk.Label(self, text=str(1 + index))
            self.number.grid(row=1+index, column=0, padx=20, pady=1)
            self.task_name = tk.Label(self, text=task.strip())
            self.task_name.grid(row=1+index, column=1, padx=50, pady=1)
            self.status = tk.Label(self, text="Awaiting")
            self.status.grid(row=1+index, column=2, padx=50, pady=1)
            self.edit = tk.Button(self, text="Edit")
            self.edit.grid(row=1+index, column=3, padx=50, pady=1)
            self.remove = tk.Button(self, text="Delete", command= lambda:self.open_delete_task_window(index))
            self.remove.grid(row=1+index, column=4, padx=50, pady=1)

    def open_add_task_window(self):
        open = AddTaskWindow(self.controller, self)

    def open_edit_task_window(self):
        pass
    def open_delete_task_window(self, idx):
        open = DeleteTaskWindow()



