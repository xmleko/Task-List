import tkinter as tk
from add_task_window import AddTaskWindow
from delete_task_window import DeleteTaskWindow
from edit_task_window import EditTaskWindow
from controller import Controller

class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("800x490")
        self.title("Task List")
        self.controller = Controller()
        self.resizable(False, False)
        self.button_add_task()
        self.create_task_list()
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.scrollbar.grid(row=1, column=6, rowspan=100, sticky='ns')



    def button_add_task(self):
        self.button_add = tk.Button(self, text="Add Task", width=12, height=3, command=self.open_add_task_window)
        self.button_add.place(x=680, y=80)

    def create_task_list(self):
        self.number_label = tk.Label(self, text="#")
        self.number_label.grid(row=0, column=0, padx=20, pady=20)
        self.task_name_label = tk.Label(self, text="Task Name")
        self.task_name_label.grid(row=0, column=1, padx=50, pady=20)
        self.status_label = tk.Label(self, text="Status")
        self.status_label.grid(row=0, column=2, padx=50, pady=20)
        self.edit_label = tk.Label(self, text="Edit")
        self.edit_label.grid(row=0, column=3, padx=50, pady=20)
        self.remove_label = tk.Label(self, text="Remove")
        self.remove_label.grid(row=0, column=4, padx=50, pady=20)

        self.task_frame = tk.Frame(self)
        self.task_frame.grid(row=1, column=0, columnspan=5, sticky='nsew')
        self.task_frame.grid_rowconfigure(0, weight=1)
        self.task_frame.grid_columnconfigure(0, weight=1)

        self.scrollbar = tk.Scrollbar(self.task_frame, orient=tk.VERTICAL)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        self.task_canvas = tk.Canvas(self.task_frame, bg='white', bd=0, highlightthickness=0,
                                     yscrollcommand=self.scrollbar.set)
        self.task_canvas.grid(row=0, column=0, sticky='nsew')
#
        self.scrollbar.config(command=self.task_canvas.yview)

        self.task_list_frame = tk.Frame(self.task_canvas, bg='white')
        self.task_list_frame.grid(row=0, column=0, sticky='nsew')

        self.task_canvas.create_window((0, 0), window=self.task_list_frame, anchor='nw')
        self.task_list_frame.bind("<Configure>",
            lambda e: self.task_canvas.configure(scrollregion=self.task_canvas.bbox("all")))

    def update_task_list(self):
        for widget in self.task_list_frame.grid_slaves():
            widget.grid_forget()

        for index, task in enumerate(self.controller.tasks):
            number_label = tk.Label(self.task_list_frame, text=str(index + 1))
            number_label.grid(row=index, column=0, padx=20, pady=1)
            task_name_label = tk.Label(self.task_list_frame, text=task["name"].strip())
            task_name_label.grid(row=index, column=1, padx=50, pady=1)
            status_label = tk.Label(self.task_list_frame, text=task["status"])
            status_label.grid(row=index, column=2, padx=50, pady=1)
            edit_button = tk.Button(self.task_list_frame, text="Edit", command=lambda idx=index: self.open_edit_task_window(idx))
            edit_button.grid(row=index, column=3, padx=50, pady=1)
            remove_button = tk.Button(self.task_list_frame, text="Delete", command=lambda idx=index: self.open_delete_task_window(idx))
            remove_button.grid(row=index, column=4, padx=50, pady=1)

    def open_add_task_window(self):
        AddTaskWindow(self.controller, self)

    def open_edit_task_window(self, index):
        EditTaskWindow(self, index, self.controller)

    def open_delete_task_window(self, index):
        DeleteTaskWindow(self, index, self.controller)

