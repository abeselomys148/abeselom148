todo_list = ["maths homework", "english essay", "laundry", "codm tournament"]
completed = []

while True:
    print(f"To-Do List: {todo_list}")
    print(f"Completed: {completed}")
    print("1. Add task")
    print("2. Remove task")
    print("3. Clear all")
    print("4. Exit")
    print("5. Mark as completed")
    
    choice = input("Choose 1-5: ")
    
    if choice == "1":
        task = input("Add task: ")
        todo_list.append(task)
        print("Task added!")

    elif choice == "2":
        print("Tasks:", todo_list)
        index = int(input("Remove position (0,1,2...): "))
        
        if 0 <= index < len(todo_list):
            todo_list.pop(index)
            print("Task removed!")
        else:
            print("Invalid position!")

    elif choice == "3":
        todo_list.clear()
        completed.clear()
        print("All cleared!")

    elif choice == "4":
        print("Goodbye!")
        break

    elif choice == "5":
        print("Tasks:", todo_list)
        index = int(input("Position to complete (0,1,2...): "))
        
        if 0 <= index < len(todo_list):
            completed.append(todo_list[index])
            print("Marked as completed!")
        else:
            print("Invalid position!")

    else:
        print("Wrong choice!")
