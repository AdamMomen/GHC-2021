from os import path
dirname = path.dirname(__file__)
filename = path.join(dirname, 'input_file.txt')

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        chunks = line.split(' ')
        print(chunks)
        # print(line)
