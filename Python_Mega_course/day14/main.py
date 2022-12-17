from Python_Mega_course.day14.modules.functions import get_todos,set_todos

while True:
    # Get user input ansd strip space chars from it
    user_action = input("type add, show, edit, complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo + '\n')

        set_todos(todos)

    elif user_action.startswith('show'):

        todo = user_action[4:]
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            # print vs f-string
            print(f"{index + 1}-{item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            set_todos(todos)

        except ValueError:
            print("There is an error, your command is not valid !")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            set_todos(todos)

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
