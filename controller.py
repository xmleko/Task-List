from pathlib import Path
from tkinter import messagebox
class Controller:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, status):
        self.tasks.append({"name": task, "status": status})

    def edit_task(self, index, task, status):
        self.tasks[index] = {"name": task, "status": status}

    def delete_task(self, index):
        del self.tasks[index]

    def save_task_file(self):
        desktop_path = Path.home() / "Desktop"
        file_path = desktop_path / "task.txt"
        with open(file_path, 'w', encoding='utf-8') as f:
            for task in self.tasks:
                task_name = task["name"].strip()
                task_status = task["status"].strip()
                f.write(f"{task_name},{task_status}\n")

    def read_task_file(self):
        try:
            desktop_path = Path.home() / "Desktop"
            file_path = desktop_path / "task.txt"
            with open(file_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        task_name = parts[0]
                        task_status = parts[1]
                        self.tasks.append({"name": task_name, "status": task_status})
                    else:
                        print(f"Błąd: Nieprawidłowy format linii w pliku: {line}")
        except Exception as e:
            print(f"Wystąpił błąd podczas odczytu pliku: {e}")


