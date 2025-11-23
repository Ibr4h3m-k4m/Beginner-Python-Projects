print("Hello User welcome to the Command Line To-Do List Application")

tasks = []

while True:
    option = input("Please chose an option from the following options by writing a number:\n1. Add a Task\n2. List Tasks\n3. Mark a task as done\n4. Delete a task\n5. Quit \n")

    if option == '1':
        task = input("Please enter the task you want to add: ")
        tasks.append({"text": task, "done": False})
        print(f'Task "{task}" added successfully!')

    elif option == '2':
        if not tasks:
            print("No tasks yet.")
        else:
            for idx, t in enumerate(tasks, start=1):
                status = "[x]" if t["done"] else "[ ]"
                print(f"{idx}. {status} {t['text']}")

    elif option == '3':
        i = int(input("Please enter the number of the task you want to mark as done: "))
        tasks[i-1]["done"] = True
        print(f'Task "{tasks[i-1]["text"]}" marked as done!')

    elif option == '4':
        i = int(input("Please enter the number of the task you want to delete: "))
        del tasks[i-1]
        print(f'Task number {i} deleted successfully!')

    elif option == '5':
        break

    else:
        print("Invalid option selected. Please try again.")
        continue

print("Thank you for using the To-Do List Application. Goodbye!")
