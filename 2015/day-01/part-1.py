import os

with open(os.path.join(os.getcwd(), 'input.txt')) as f:
    chars = f.readlines()
    chars = chars[0]
    count: int = 0

    for char in chars:
        if char == '(':
            count += 1
        else:
            count -= 1

    print(count)
