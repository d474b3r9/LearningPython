def get_average():
    with open("../bonus/data.txt", 'r') as file:
        data = file.readlines()

    values = data[1:]
    values = [float(i) for i in values]
    average_local = sum(values) / len(values)

    return average_local


average = get_average()
print(average)


def get_max():
    grades = [9.6, 9.2, 9.7]
    grades_max = max(grades)
    grades_min = min(grades)
    message = f"Max: {grades_max}, Min: {grades_min}"
    return message


print(get_max())
