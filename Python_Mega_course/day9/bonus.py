password = input("Enter password: ")

result = {}

if len(password) >= 8:
    result["Lenght"] = True
else:
    result["Lenght"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["uppercase"] = uppercase

lowercase = False
for i in password:
    if i.islower():
        lowercase = True

result["lowercase"] = lowercase

print(result)
if all(result):
    print("Strong Password")
else:
    print("Weak Password")
