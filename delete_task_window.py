import tkinter as tk
class DeleteTaskWindow(tk.Toplevel):
    def __init__(self, parent, index, controller):
        super().__init__()
        self.title("Delete Task")
        self.geometry("400x270")
        self.parent = parent
        self.index = index
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, width=40, height=5, text="Are you sure you want to delete this task?")
        label.pack()
        button_accept = tk.Button(self, width= 25, height=2, text="Yes", command = self.confirm_delete)
        button_accept.pack()
        button_cancel = tk.Button(self, width= 25, height=2, text="No", command = self.cancel_delete)
        button_cancel.pack()

    def confirm_delete(self):
        self.controller.delete_task(self.index)
        self.parent.update_task_list()
        self.destroy()

    def cancel_delete(self):
        self.destroy()

