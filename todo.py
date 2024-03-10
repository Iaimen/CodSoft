class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found in the list.")

    def view_tasks(self):
        if self.tasks:
            print("Your to-do list:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Your to-do list is empty.")

# Example usage:
todo_list = TodoList()

todo_list.add_task("Buy groceries")
todo_list.add_task("Finish homework")
todo_list.add_task("Call mom")

todo_list.view_tasks()

todo_list.remove_task("Finish homework")

todo_list.view_tasks()
