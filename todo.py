import os           #to performperation with operating system
import pickle        # to serialize the objects

#if file exists, then open file
class Todo:
    def __init__(self, filename="todo.pickle"):
        self.filename = filename
        if os.path.exists(filename):
            with open(filename, 'rb') as c:
                self.tasks = pickle.load(c)
        else:
            self.tasks = []

#function to add task in list
    def add(self, task):
        self.tasks.append(task)

#delete task from list
    def remove(self, task_index):
        del self.tasks[task_index]

#display tasks
    def display(self):
        if self.tasks:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")
        else:
            print("No task are there in list")

# save file
    def save_to_file(self):
        with open(self.filename, 'wb') as z:
            pickle.dump(self.tasks, z)


# main body
def main():
    todo_list = Todo()

# print list for user to enter choice
    while True:
        print("\n=--------TODO LIST----------=")
        print("1. Add Task to do")
        print("2. Remove Task from list")
        print("3. Display List of Tasks")
        print("4. Quit and exit program")

        choice = input("\n\nEnter your choice: ")

# 1 for added tasks
        if choice == '1':
            task = input("Enter task: ")
            todo_list.add(task)
            todo_list.save_to_file()
            print("Task added in list.")
# 2 for remove tasks
        elif choice == '2':
            todo_list.display()
            if todo_list.tasks:
                task_index = int(input("Enter task number to remove: ")) - 1
                if 0 <= task_index < len(todo_list.tasks):
                    todo_list.remove(task_index)
                    todo_list.save_to_file()
                    print("Task removed.")
                else:
                    print("Invalid task number.")
# 3 for display tasks
        elif choice == '3':
            print("Tasks:")
            todo_list.display()
# 4 for exit the terminal
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. choose number between 1-3.")

#call main function
if __name__ == "__main__":
    main()
