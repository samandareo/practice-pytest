from projects.basics.todo_list import TodoList

class TestTodoList:

    def setup_method(self):
        self.tasks = TodoList()

    def test_add_task(self):
        res = self.tasks.add_task("Write test for add task")
        expected = "Task 'Write test for add task' added"
        assert res == expected

    def test_add_task_for_duplicate_tasks(self):
        self.tasks.add_task("Number task one")
        duplicated_task1 = self.tasks.add_task("Number task one")
        expected = "Task 'Number task one' already exists"
        assert duplicated_task1 == expected

    def test_remove_task(self):
        self.tasks.add_task("Task to remove")
        remove_task = self.tasks.remove_task("Task to remove")
        expected = "Task 'Task to remove' removed"
        assert remove_task == expected

    def test_remove_not_exist_task(self):
        remove_task = self.tasks.remove_task("Task to remove")
        expected = "Task 'Task to remove' not found"
        assert remove_task == expected

    def test_get_tasks(self):
        self.tasks.add_task("Task 1")
        self.tasks.add_task("Task 2")
        self.tasks.add_task("Task 3")
        tasks_list = self.tasks.get_tasks()
        expected = [{"task": "Task 1", "done": False}, {"task": "Task 2", "done": False}, {"task": "Task 3", "done": False}]
        assert tasks_list == expected

    def test_mark_complete(self):
        self.tasks.add_task("Task 1")
        result = self.tasks.mark_complete("Task 1")
        expected_msg = "Task 'Task 1' marked as complete"
        assert result == expected_msg
        tasks = self.tasks.get_tasks()
        assert tasks[0]["done"] is False

    def test_mark_complete_not_exist_task(self):
        marked_task = self.tasks.mark_complete("Task 1")
        expected = "Task 'Task 1' not found"
        assert marked_task == expected

