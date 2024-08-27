import os

with open(os.path.join(os.getcwd(), 'input.txt')) as f:
    chars = f.readline().strip()
    floor = 0

    for i, char in enumerate(chars, 1):
        floor += 1 if char == '(' else -1

        if floor == -1:
            print(i)
            break
