while True:
    # Get user input ansd strip space chars from it
    user_action = input("type add, show, edit, complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('todos.txt', 'a') as file:
            todos = file.writelines(todo)

    elif user_action.startswith('show'):

        todo = user_action[4:]
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            # print vs f-string
            print(f"{index + 1}-{item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number -1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        except ValueError:
            print("There is an error, your command is not valid !")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print('Out of index !')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command doens't exists !")

print("Byes!")

