import time

def display_menu():
    print("\nTo-Do List Menu:")
    print("1: View To-Do List")
    print("2: Add Task")
    print("3: Remove Task")
    print("4: Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour To-Do list is empty.")
    else:
        print("\nYour To-Do list:")
        for i, task in enumerate(tasks, 1):
            print(f"Task {i}: {task}")

def add_task(tasks):
    while True:
        task = input("\nEnter the task you want to add (0 to go back): ")
        if task == '0':
            break
        elif task.strip() == "":
            print("Empty task entered. Please enter a valid task.")
        else:
            tasks.append(task)
            print(f"{task} added to To-Do list.")
            break

def remove_task(tasks):
    while True:
        view_tasks(tasks)
        if not tasks:
            break
        try:
            task_num = int(input("\nEnter the number of the task you want to remove (0 to go back): "))
            if task_num == 0:
                break
            elif 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"{removed_task} removed from To-Do list.")
                break
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

def goodbye():
    message = "Exiting To-Do-List app. Goodbye!"
    for char in message:
        print(char, end = '', flush = True)
        time.sleep(0.05)
    print()
    exit()

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            goodbye()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()