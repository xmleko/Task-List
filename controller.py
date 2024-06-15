class Controller:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, status):
        self.tasks.append({"name": task, "status": status})

    def edit_task(self, index, task, status):
        self.tasks[index] = {"name": task, "status": status}

    def delete_task(self, index):
        del self.tasks[index]
