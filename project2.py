def show_menu():
    print("****/Todo List/****")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark task as completed")
    print("4. Quit")
    
def add_task(todo_list, task):
    '''
    Add task function takes a todo list which is used to store all it todo inside it
    Task is a new todo which will be added to the todo_list
    Append function of the list is used to add a new element of the end of list
    '''
    todo_list,append(task)
    print(f"Task{task} added to the to do list")

def view_tasks(todo_list):
    '''
    view_task function takes a todo_list and shows all the todos present inside it
    First, we are checking if the todo_list doesn't contain anything and if it doesn't contain antyhing, then it prints the error message
    if it contains anything, then using a for loop to iterate in the todo_list and getting the index and the task and printing it using  Fstring
    enumerate function is used to put some condition like here, we are putting that the index should start with 1
    '''
    if not todo_list:
        print("Todo list to empty")
    else:
        print("\n Current Tasks")

        for index, task in emunerate(todo_list, start=1):
            print(f"{index}, {task}")

def mark_completed(todo_list, task_index):
    '''
    mark_completed function takes todo list and the index of the task which you want to delete from the list
    Checking if task index is present in todo_list or not, it it's present the removing the task from the list using pop function and pop function 
    take the index of the list element which we need to delete
    '''
    if 1<= task_index <= len(todo_list):
        Completed_task todo_list. pop(task_index -1)
        print(f"Task {completed_task} marked as completed")
    else:
        print("Invalid task index")