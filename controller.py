class Controller:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

        print(self.tasks)
