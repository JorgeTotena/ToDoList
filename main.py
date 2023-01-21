print('''Welcome to your to-do list app
These are your current to-dos''')
todolist = [{"todo description": "Learn Python", "due date": "01/14/2023"},  
            {"todo description": "Walk the dog", "due date": "01/14/2023"}
            ]
print(todolist)

def add_todos(todolist):    
    todolist.append({"todo description": input("What's your new todo "), "due data": input('When is it due -> mm/dd/aaaa ')})
    return todolist
    
def delete_todos(todolist):    
    description = input("Input the description you want to delete -> ")
    todolist = [item for item in todolist if item["todo description"] != description]
    return todolist
    
def update_todos(todolist):
    description = input("Input the description you want to update -> ")   
    todolist = [item for item in todolist if item["todo description"] != description]
    todolist.append({"todo description": input("Input your new todo"), "due data": input('When is it due -> mm/dd/aaaa ')})
    print(todolist)
    return todolist
change = input("Would you like to change something in your list y/n -> ")
if change == "y":
    option = input(''' Select your option (in numbers)
    1. Add todos
    2. Delete todos
    3. Update todos
    4. Consult todos                   
''')
    if option == "1":
        add_todolist = add_todos(todolist)
        print(add_todolist)
    elif option == "2":
        delete_todo = delete_todos(todolist)
        print(delete_todo)
    elif option == "3":
        update_todolist = update_todos(todolist)
        #updating = update_todos(update_todolist)
        print(update_todolist)
    else:
        print("you did not input a correct option")
        
else:
    print("Choose a correct option")    


'''index = list(todolist[0].keys()).pop("todo description")
print(index) '''

# GETS THE index within the dictionary stored in the list
''' index = list(todolist[0].keys()).index("todo description")
print(index) '''

#REMOVING A VALUE FROM THE TODOLIST WITH A STANDARD LIST
"""for item in todolist:
    if item["todo description"] == "Learn Python":
        todolist.remove(item) """
        
''' todolist = [item["todo description"] = new_todo for item in todolist if item["todo description"] == description]'''