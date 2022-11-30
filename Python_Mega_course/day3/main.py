todos = []

while True:
    user_action = input("type add, show, or exit : ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        # _ is a dev convention
        case _:
            print("Error this doesn't exists")

print("Byes!")