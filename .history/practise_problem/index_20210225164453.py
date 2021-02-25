from os import path
dirname = path.dirname(__file__)
filename = path.join(dirname, 'input_file.txt')
with open('input_file.txt') as file_object:
    data = file_object.read()

    print(data)
