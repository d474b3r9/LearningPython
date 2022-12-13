user_password = input("Enter new password: ")

def pwd_checker(pwd):
    result = {}

    if len(pwd) >= 8:
        result["Lenght"] = True
    else:
        result["Lenght"] = False

    uppercase = False
    for i in pwd:
        if i.isupper():
            uppercase = True

    result["uppercase"] = uppercase

    digit = False
    for i in pwd:
        if i.isdigit():
            digit = True

    result["digits"] = digit

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"

print(pwd_checker(user_password))


