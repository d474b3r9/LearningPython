mylist = ['a','b','c']
z = mylist[1]
print(mylist[1])
print(z)
print(mylist.index('b'))

# change item
mylist.__setitem__(1, 'e')
print(mylist)
# usually change item
mylist[1]='e'

# get item
print(mylist.__getitem__(2))
mylist[2]

filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]
i=0

for filename in filenames:
    # replace . with - only first occurence
    filename = filename.replace('.', '-',1)
    filenames[i]=filename
    i = i +1

print(filenames)