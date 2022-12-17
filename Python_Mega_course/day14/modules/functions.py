def get_todos(filepath='todos.txt'):
    """ Return the text file and return the list of
    to-do items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def set_todos(value_todo,filepath='todos.txt'):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(value_todo)
