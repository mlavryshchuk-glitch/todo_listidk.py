to_do_list = []

def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# add_task("Buy toilet paper")

def view_tasks():
    print("\nYour To-Do List:")
    if not to_do_list:
        print("Your to-do list is empty. Add something!")
    else:
        for i, task in enumerate(to_do_list):
            print(f"{i + 1}. {task}")

# view_tasks()

def delete_task(task_number):
    try:

        index = int(task_number) - 1

        if 0 <= index < len(to_do_list):
            
            removed_task = to_do_list.pop(index)
            print(f"task '{removed_task}' deleted.")
        else:
            print("Error: A task with that number does not exist.")
    except ValueError:
        print("Error: Please enter a number.")

# delete_task(1)

def edit_task(task_number, new_task):
    try:
        index = int(task_number) - 1

        if 0 <= index < len(to_do_list):
            old_task = to_do_list[index]
            to_do_list[index] = new_task
            print(f"Task '{old_task}' updated to '{new_task}'.")
        else:
            print("Error: A task with that number does not exist.")
    except ValueError:
        print("Error: Please enter a number.")

# edit_task(1, "Buy milk")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Edit Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '3':
            task_number = input("Enter the task number to delete: ")
            delete_task(task_number)
        elif choice == '4':
            task_number = input("Enter the task number to edit: ")
            new_task = input("Enter the new task: ")
            edit_task(task_number, new_task)
        elif choice == '5':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()