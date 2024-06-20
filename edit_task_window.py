import tkinter
import tkinter as tk
from tkinter import messagebox

class EditTaskWindow(tk.Toplevel):
    def __init__(self, parent, index, controller):
        super().__init__()
        self.title('Edit Task')
        self.geometry("450x330")
        self.parent = parent
        self.index = index
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.icon = tk.PhotoImage(file="icon/ok.png")
        label = tk.Label(self, width=40, height=4, text="Editing a task", font=("Helvetica", 14, "bold"), fg="white", bg='#413F3F')
        label.pack(pady=5)
        self.task_text = tk.Text(self, width=30, height=5, bg='#E0E0E0')
        self.task_text.insert(tk.INSERT, self.controller.tasks[self.index]["name"])
        self.task_text.pack(pady = 10)
      #  self.status_text = tk.Text(self,  width=30, height=5)
      #  self.status_text.insert(tk.INSERT, self.controller.tasks[self.index]["status"])
      #  self.status_text.pack()
        self.status_text = tk.Listbox(self, width=40, height=3, justify="center", bg='#E0E0E0')
        self.status_text.insert(1, "Awaiting")
        self.status_text.insert(2, "In Progress")
        self.status_text.insert(3, "Finished")
        self.status_text.pack(pady = 5)
        confirm = tk.Button(self, image=self.icon, command=self.confirm_change)
        confirm.pack()

    def confirm_change(self):
        try:
            task = self.task_text.get("1.0", tk.END).strip()
            status_index = self.status_text.curselection()[0]
            status = self.status_text.get(status_index)
            self.controller.edit_task(self.index, task, status)
            self.parent.update_task_list()
            self.destroy()
        except:
            tkinter.messagebox.showinfo("Error", "Please select status task")