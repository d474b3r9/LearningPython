while True:
    # Get user input ansd strip space chars from it
    user_action = input("type add, show, edit, complete or exit : ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'w')
            todos = file.writelines(todo)
            file.close()

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                # print vs f-string
                print(f"{index + 1}-{item}")

        case 'edit':
            number = int(input("Number to edit:"))
            number = number -1
            todos[number] = input("New item:")
        case 'complete':
            removed_item = int(input("Item number to remove:"))
            todos.pop(removed_item -1)
        case 'exit':
            break
        # _ is a dev convention
        case _:
            print("Error this doesn't exists")

print("Byes!")
