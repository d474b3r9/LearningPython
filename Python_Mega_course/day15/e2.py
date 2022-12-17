import csv

with open("inc/weather.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

# we put [1:] to skip list labels
for row in data[1:]:
    if row[0] == city:
        print(row[1])
