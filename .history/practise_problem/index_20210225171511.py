from os import path
dirname = path.dirname(__file__)
filename = path.join(dirname, 'input_file.txt')

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        chunks = line.split(' ')
        for chunk in chunks:
            print(chunk[-1])
            chunk[-1].replace('\n', '')
        print(chunks)