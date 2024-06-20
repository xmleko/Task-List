import tkinter as tk

class EditTaskWindow(tk.Toplevel):
    def __init__(self, parent, index, controller):
        super().__init__()
        self.title('Edit Task')
        self.geometry("450x320")
        self.parent = parent
        self.index = index
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, width=40, height=5, text="Editing a task")
        label.pack()
        self.task_text = tk.Text(self, width=30, height=5)
        self.task_text.insert(tk.INSERT, self.controller.tasks[self.index]["name"])
        self.task_text.pack()
        self.status_text = tk.Text(self, width=30, height=5)
        self.status_text.insert(tk.INSERT, self.controller.tasks[self.index]["status"])
        self.status_text.pack()
        confirm_change = tk.Button(self, width = 20, height = 5, text="Confirm Change", command=self.confirm_change)
        confirm_change.pack()

    def confirm_change(self):
        task = self.task_text.get("1.0", tk.END).strip()
        status = self.status_text.get("1.0", tk.END).strip()
        self.controller.edit_task(self.index, task, status)
        self.parent.update_task_list()