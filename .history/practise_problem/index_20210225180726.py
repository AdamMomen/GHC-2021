from os import path
dirname = path.dirname(__file__)
filename = path.join(dirname, 'input_file.txt')

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        chunks = line.splitlines()[0].split(' ')

        print(chunks)

# caluclate the number of teams
# Tahmid
# nap sack problem


# Objective
# - maximum number of ingredients in miniumum number of pizza

# Constraints
# - number of pizza  = number of
# - all the team have of pizza or non!
# -
"""
5 1 2 1
3 onion pepper olive
3 mushroom tomato basil
3 chicken mushroom pepper
3 tomato mushroom basil
2 chicken basil
"""
