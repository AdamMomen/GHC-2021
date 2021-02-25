from os import path
dirname = path.dirname(__file__)
filename = path.join(dirname, 'input_file.txt')

with open(filename) as file_object:
    data = file_object.read()
    for line, idx in enumerate(data):
        print(idx, line)
