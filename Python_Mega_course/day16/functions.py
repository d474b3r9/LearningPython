FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Return the text file and return the list of
    to-do items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def set_todos(value_todo, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(value_todo)


print(__name__)

if __name__ == "__main__":
    print("Hello from functions")
