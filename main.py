print('''Welcome to your to-do list app
These are your current to-dos''')
def todolist():
    todolist = [{"todo description": "Learn Python", "done": False},  
                {"todo description": "Walk the dog", "done": False}]
    print(todolist)
    return todolist

def add_todos(todos):
    confirmation = input("Do you want to add a new todo? y/n ")
    
    if confirmation == "y":
        addition = todos.append({"todo description": input("What's your new todo"), "done": False})
        print(todos)
        return addition
    else:
        print("thank you for using this program")

todos = todolist()
addition = add_todos(todos)
