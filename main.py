print('''Welcome to your to-do list app
These are your current to-dos''')
todolist = [{"todo description": "Learn Python", "due date": "01/14/2023"},  
            {"todo description": "Walk the dog", "due date": "01/14/2023"}
            ]
print(todolist)

def add_todos(todolist):
    confirmation = input("Do you want to add a new todo? y/n ")
    if confirmation == "y":
        addition = todolist.append({"todo description": input("What's your new todo "), "due data": input('When is it due -> mm/dd/aaaa ')})
        return addition
    else:
        print("thank you for using this program")

def delete_todos(todolist):
    confirmation = input("Do you want to delete a todo y/n ")
    if confirmation == "y":
        pass
    
# addition = add_todos(todolist)

# escription = input("Input the description you want to delete -> ")
#todolist = [item for item in todolist if item["todo description"] != description]

print(todolist)
change = input("Would you like to change something in your list y/n -> ")
if change == "y":
    option = input(''' Select your option (in numbers)
    1. Add todos
    2. Delete todos
    3. Update todos
    4. Consult todos                   
''')
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