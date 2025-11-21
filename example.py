todo_list = ["homework", "classwork", "project work"]
while True:
    print("To-Do List:", todo_list)
    print("1. Add task")
    print("2. Remove task") 
    print("3. Clear all")
    print("4. Exit")
    
    choice = input("Choose 1-4: ")
    
    if choice == "1":
        task = input("Add task: ")
        todo_list.append(task)
        
    elif choice == "2":
        print("Tasks:", todo_list)
        index = int(input("Remove position: "))
        todo_list.pop(index)
        
    elif choice == "3":
        todo_list.clear()
        print("All cleared!")
        
    elif choice == "4":
        break
        
    else:
        print("Wrong choice!")