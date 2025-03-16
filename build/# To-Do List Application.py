# To-Do List Application

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        """View all tasks"""
        if not self.tasks:
            print("No tasks in your to-do list.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def remove_task(self, task_number):
        """Remove a task from the list by its number"""
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")

    def update_task(self, task_number, new_task):
        """Update a task with a new description"""
        if 0 < task_number <= len(self.tasks):
            old_task = self.tasks[task_number - 1]
            self.tasks[task_number - 1] = new_task
            print(f"Task '{old_task}' updated to '{new_task}' successfully!")
        else:
            print("Invalid task number.")


def show_menu():
    """Display the menu"""
    print("\nTo-Do List Application")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Update a task")
    print("4. Remove a task")
    print("5. Exit")


def main():
    todo_list = ToDoList()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input("Enter the task description: ")
            todo_list.add_task(task)
        elif choice == '3':
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to update: "))
                new_task = input("Enter the new description for the task: ")
                todo_list.update_task(task_number, new_task)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == '4':
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                todo_list.remove_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice, please select a valid option (1-5).")


if __name__ == "__main__":
    main()