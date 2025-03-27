class TodoList:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not any(t['task'] == task for t in self.tasks):
            self.tasks.append({"task": task, "done": False})
            return f"Task '{task}' added"
        return f"Task '{task}' already exists"

    def remove_task(self,task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                return f"Task '{task}' removed"
        return f"Task '{task}' not found"

    def get_tasks(self):
        return self.tasks

    def mark_complete(self, task):
        for t in self.tasks:
            if t['task'] == task:
                t['task'] = True
                return f"Task '{task}' marked as complete"
        return f"Task '{task}' not found"