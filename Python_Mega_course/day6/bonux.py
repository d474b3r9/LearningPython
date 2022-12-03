contents = ["fdsfdsfdsfdfsdfds.", "fdsfdsfdsfd", "gfdgfdgfdgfd"]
filenames = ["fgfds.txt", "vcxvcxv.txt", "fsdfsdffsd.txt"]

for contents, filenames in zip(contents, filenames):
    file = open(f"files/{filenames}", 'w')
    file.write(contents)
