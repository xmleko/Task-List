import tkinter as tk
from add_task_window import AddTaskWindow
from delete_task_window import DeleteTaskWindow
from edit_task_window import EditTaskWindow
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
        self.button_add = tk.Button(self, text="Add Task", width=20, height=3, command=self.open_add_task_window)
        self.button_add.place(x=230, y=20)

    def update_task_list(self):
        for widget in self.grid_slaves():
            if int(widget.grid_info()["row"]) > 0:
                widget.grid_forget()

        for index, task in enumerate(self.controller.tasks):
            self.number = tk.Label(self, text=str(1 + index))
            self.number.grid(row=1+index, column=0, padx=20, pady=1)
            self.task_name = tk.Label(self, text=task["name"].strip())
            self.task_name.grid(row=1+index, column=1, padx=50, pady=1)
            self.status = tk.Label(self, text=task["status"])
            self.status.grid(row=1+index, column=2, padx=50, pady=1)
            self.edit = tk.Button(self, text="Edit", command= lambda:self.open_edit_task_window(index))
            self.edit.grid(row=1+index, column=3, padx=50, pady=1)
            self.remove = tk.Button(self, text="Delete", command= lambda:self.open_delete_task_window(index))
            self.remove.grid(row=1+index, column=4, padx=50, pady=1)

    def open_add_task_window(self):
        open = AddTaskWindow(self.controller, self)

    def open_edit_task_window(self, index):
        open = EditTaskWindow(self, index, self.controller)
    def open_delete_task_window(self, index):
        open = DeleteTaskWindow(self, index, self.controller)



