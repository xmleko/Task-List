import tkinter as tk
from tkinter import messagebox
from status import Status


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
        self.status_text = tk.Listbox(self, width=40, height=3, justify="center", bg='#E0E0E0')
        for status in Status:
            self.status_text.insert(tk.END, status.value)
        #self.status_text.insert(1, "Awaiting")
        #self.status_text.insert(2, "In Progress")
        #self.status_text.insert(3, "Finished")
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
        #   match status:
            #    case Status.AWAITING.value:
            #        self.parent.change_status_label_color(self.index, "#BBC092")
            #    case Status.IN_PROGRESS.value:
            #        self.parent.change_status_label_color(self.index, "#E0F64F")
            #    case Status.FINISHED.value:
            #        self.parent.change_status_label_color(self.index, "#519131")
            self.destroy()
        except:
            tk.messagebox.showinfo("Error", "Please select status task")
