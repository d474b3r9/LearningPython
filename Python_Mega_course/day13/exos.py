
def birth(y_o_birth,current_year=2022):
    age =  current_year - y_o_birth
    return age,current_year

age = birth(int(input(" What is your year of birth ?")))
current_age = age[0]
if current_age > 120:
    print("wow you so old !")
else:
    print(age)
# print(birth(1984))