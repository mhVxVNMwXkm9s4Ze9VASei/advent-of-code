import os

with open(os.path.join(os.getcwd(), 'input.txt')) as f:
    chars = f.readlines()
    open: int = 0
    closed: int = 0
    chars = chars[0]

    for char in chars:
        if char == '(':
            open += 1
        else:
            closed += 1

        if closed > open:
            print(closed + open)
            break
