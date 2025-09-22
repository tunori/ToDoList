# toDoApp.py

tasks = []

def addTask(task):
    '''
    This Function appends the input/task to the stack
    '''
    tasks.append(task)
    print("task added!\n")

def showTasks():
    '''
    This Function shows current tasks.
    '''
    if len(tasks) == 0:
        print("\nNo tasks yet.")
    else:
        print("\nCurrent Tasks: ")
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])
        print("\n")

def removeTask(tasknumber):
    '''
    This Function removes/pops a task depending on the user.
    '''
    tasks.pop(tasknumber - 1)
    print("task removed!\n")

def main():
    '''
    A function called main for readability and modularity
    '''
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        ch = input("\nEnter choice: ")
        if ch == "1":
            t = input("Enter task : ")
            addTask(t)
        elif ch == "2":
            showTasks()
        elif ch == "3":
            showTasks()  
            if tasks:  
                try:
                    n = int(input("Enter task number to remove: "))
                    if 1 <= n <= len(tasks):
                        removeTask(n)
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number!")
            else:
                print("No tasks to remove!")
        elif ch == "4":
            print("Bye!\n")
            break
        else:
            print("Wrong choice !")
            print() 

if __name__ == "__main__":
    main()