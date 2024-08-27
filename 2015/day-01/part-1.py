import os

with open(os.path.join(os.getcwd(), 'input.txt')) as f:
    chars = f.readline().strip()
    print(sum(1 if char == "(" else -1 for char in chars))
