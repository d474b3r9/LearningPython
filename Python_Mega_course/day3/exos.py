meals = ['pasta','pizza','salad']

for meal in meals:
    print(meal.capitalize())

print("Bye")

ingredients = ["john smith", "sen plakay", "dora ngacely"]

for i in ingredients:
    print(i.title())

user_action = input("Where do you come from ?")

match user_action:
    case 'USA':
        print('Hello')
    case 'India':
        print('Namaste')
    case 'Germany':
        print('Hallo')