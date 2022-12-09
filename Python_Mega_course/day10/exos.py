try:
    total_value = float(input("Enter total_value: "))
    value = float(input("Enter value: "))
    result = value / total_value * 100
    print(result)
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("You can't divide by zero.")

