import tkinter as tk
from add_task_window import AddTaskWindow
from delete_task_window import DeleteTaskWindow
from edit_task_window import EditTaskWindow
from controller import Controller
import datetime
from notify import Notify


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x490")
        self.title("Task List")
        self.controller = Controller()
        self.resizable(False, False)
        self.create_task_list()
        self.button_add_task()
        self.status_labels = []
        self.refresh_time()
        self.controller.read_task_file()
        self.update_task_list()
        self.notification = Notify()
        self.notification.show_notification(self.controller)
        self.protocol("WM_DELETE_WINDOW", self.on_destroy)

    def create_task_list(self):
        disc = tk.Label(self, text="My ToDo List", font=50)
        disc.place(x=150, y=350)
        self.time = tk.Label(self, text="Current time: " + str(datetime.datetime.now()), font=50)
        self.time.place(x=150, y=400)
        number_label = tk.Label(self, text="#", anchor="center")
        number_label.grid(row=0, column=0, padx=20, pady=20)
        task_name_label = tk.Label(self, text="Task Name", anchor="center")
        task_name_label.grid(row=0, column=1, padx=50, pady=20)
        status_label = tk.Label(self, text="Status", anchor="center")
        status_label.grid(row=0, column=2, padx=50, pady=20)
        edit_label = tk.Label(self, text="Edit Task", anchor="center")
        edit_label.grid(row=0, column=3, padx=50, pady=20)
        remove_label = tk.Label(self, text="Remove Task", anchor="center")
        remove_label.grid(row=0, column=4, padx=50, pady=20)

        #scrollbar canvas
        task_frame = tk.Frame(self)
        task_frame.grid(row=1, column=0, columnspan=5, sticky='nsew')
        task_frame.grid_columnconfigure(0, weight=1)

        scrollbar = tk.Scrollbar(task_frame, orient=tk.VERTICAL)
        scrollbar.grid(row=0, column=1, sticky='ns')

        self.task_canvas = tk.Canvas(task_frame, bg='#E0E0E0', bd=0, width=650, highlightthickness=0,
                        yscrollcommand=scrollbar.set)
        self.task_canvas.grid(row=0, column=0, sticky='nsew')
        self.task_list_frame = tk.Frame(self.task_canvas, bg='#E0E0E0')
        self.task_list_frame.grid(row=0, column=0, sticky='nsew')
        self.task_canvas.create_window((0, 0), window=self.task_list_frame, anchor='nw')
        self.task_list_frame.bind("<Configure>",
            lambda e: self.task_canvas.configure(scrollregion=self.task_canvas.bbox("all")))
        self.task_canvas.bind_all("<MouseWheel>", self.on_mousewheel) # mousewheel

        scrollbar.config(command=self.task_canvas.yview)

        self.icon_del = tk.PhotoImage(file="icon/del.png")
        self.icon_add = tk.PhotoImage(file="icon/add.png")
        self.icon_edit = tk.PhotoImage(file="icon/edit.png")

    def button_add_task(self):
        button_add = tk.Button(self, text="Add Task", image=self.icon_add, command=self.open_add_task_window)
        button_add.place(x=680, y=80)

    def refresh_time(self):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.time.config(text="Current time: " + current_time, font=50)
        self.time.after(1000, self.refresh_time)

    def on_mousewheel(self, event):
        if event.delta < 0:
            self.task_canvas.yview_scroll(1, "units")
        else:
            self.task_canvas.yview_scroll(-1, "units")

    def update_task_list(self):
        for widget in self.task_list_frame.grid_slaves():
            widget.grid_forget()

        self.status_labels.clear()

        for index, task in enumerate(self.controller.tasks):
            number_label = tk.Label(self.task_list_frame, text=str(index + 1), bg='#E0E0E0', anchor="center")
            number_label.grid(row=index, column=0, padx=20, pady=1)
            task_name_label = tk.Label(self.task_list_frame, text=task["name"].strip(), wraplength=90, bg='#E0E0E0', anchor="center")
            task_name_label.grid(row=index, column=1, padx=50, pady=1)
            status_label = tk.Label(self.task_list_frame, text=task["status"], bg = "#BBC092", anchor="center", borderwidth=2, relief="solid")
            status_label.grid(row=index, column=2, padx=50, pady=1)
            edit_button = tk.Button(self.task_list_frame, text="Edit",bg='#E0E0E0', anchor="center",  image=self.icon_edit, command=lambda idx=index: self.open_edit_task_window(idx))
            edit_button.grid(row=index, column=3, padx=50, pady=1)
            remove_button = tk.Button(self.task_list_frame, text="Delete",bg='#E0E0E0', anchor="center", image=self.icon_del, command=lambda idx=index: self.open_delete_task_window(idx))
            remove_button.grid(row=index, column=4, padx=50, pady=1)

            self.status_labels.append(status_label)

    def change_status_label_color(self, index, color):
        self.status_labels[index].config(bg=color)

    def open_add_task_window(self):
        AddTaskWindow(self.controller, self)

    def open_edit_task_window(self, index):
        EditTaskWindow(self, index, self.controller)

    def open_delete_task_window(self, index):
        DeleteTaskWindow(self, index, self.controller)

    def on_destroy(self):
        self.controller.save_task_file()
        self.destroy()
