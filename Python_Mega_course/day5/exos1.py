waiting_list = ["sen","ben","jonh"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f"{index+1}.{item.capitalize()}"
    print(row)

filenames = ['document', 'report', 'presentation']
for index, item in enumerate(filenames):
    row = f"{index}.{item.capitalize()}.txt"
    print(row)

ips = ['100.122.133.105', '100.122.133.111']
huhu= int(input(" enter 0 or 1 :"))
print(ips[huhu])

menu = ["pasta", "pizza", "salad"]

user_choice = int(input("Enter the index of the item: "))
message = f"You chose {menu[user_choice]}."
print(message)