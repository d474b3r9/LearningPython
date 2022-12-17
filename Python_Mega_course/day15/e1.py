import glob

#read all files

myfiles = glob.glob("inc/*.txt")
print(myfiles)

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())