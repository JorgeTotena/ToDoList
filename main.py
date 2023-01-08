print('''Welcome to your to-do list app
These are your current to-dos''')
def todolist(position):
    todolist = [{"todo description": "Learn Python", "done": False}, 
                {"todo description": "Walk the dog", "done": False}]
    print(todolist[position])
    return todolist

todos = todolist(int(input("Input your task number -> ")))