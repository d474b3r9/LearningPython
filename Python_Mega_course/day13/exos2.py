
def get_names(names):
    names = names.split(',')
    return len(names)

name_list = input("Enter names separated by commas (no spaces):")
print(get_names(name_list))