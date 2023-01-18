print('''Welcome to your to-do list app
These are your current to-dos''')
todolist = [{"todo description": "Learn Python", "due date": "01/14/2023"},  
            {"todo description": "Walk the dog", "due date": "01/14/2023"}
            ]
print(todolist)

def add_todos(todolist):    
    todolist = todolist.append({"todo description": input("What's your new todo "), "due data": input('When is it due -> mm/dd/aaaa ')})
    return todolist
    
def delete_todos(todolist):    
    description = input("Input the description you want to delete -> ")
    todolist = [item for item in todolist if item["todo description"] != description]
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
        addition = add_todos(todolist)
    elif option == "2":
        todolist = delete_todos(todolist)
    else:
        print("you did not input a correct option")
        
else:
    print("Choose a correct option")    

print(todolist)





'''index = list(todolist[0].keys()).pop("todo description")
print(index) '''

# GETS THE index within the dictionary stored in the list
''' index = list(todolist[0].keys()).index("todo description")
print(index) '''

#REMOVING A VALUE FROM THE TODOLIST WITH A STANDARD LIST
"""for item in todolist:
    if item["todo description"] == "Learn Python":
        todolist.remove(item) """