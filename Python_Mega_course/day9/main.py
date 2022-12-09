while True:
    # Get user input ansd strip space chars from it
    user_action = input("type add, show, edit, complete or exit : ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'a') as file:
            todos = file.writelines(todo)

    elif 'show' in user_action:

        todo = user_action[4:]
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            # print vs f-string
            print(f"{index + 1}-{item}")

    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number -1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)

        message = f"Todo {number} was removed from the list"
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print("Command doens't exists !")

print("Byes!")

