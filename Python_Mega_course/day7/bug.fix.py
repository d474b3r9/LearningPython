temperatures = [10, 12, 14]
file = open("file.txt", 'w')
file.writelines(str(i) for i in temperatures)

numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for number in numbers]
print(numbers)
