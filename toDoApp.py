# toDoApp.py
# Applied Black formatter 

tasks = []


def addtask(task):
    tasks.append(task)
    print("task added!")


def showTasks():
    if len(tasks) == 0:
        print("no tasks yet")
    else:
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])


def removetask(tasknumber):
    tasks.pop(tasknumber - 1)
    print("task removed!!")


def main():
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        ch = input("enter choice : ")
        if ch == "1":
            t = input("enter task : ")
            addtask(t)
        elif ch == "2":
            showTasks()
        elif ch == "3":
            showTasks()  
            if tasks:  
                try:
                    n = int(input("enter task no to remove: "))
                    if 1 <= n <= len(tasks):
                        removetask(n)
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number!")
            else:
                print("No tasks to remove!")
        elif ch == "4":
            break
        else:
            print("wrong choice!!")
        print() 


main()