
waiting_list = ["john", "marry"]
name = input("Enter name: ")

try:
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print("Value doesn't exists.")