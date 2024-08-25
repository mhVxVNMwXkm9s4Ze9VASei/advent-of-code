import os

with open(os.path.join(os.getcwd(), 'input.txt')) as f:
    lines = f.readlines()[0].strip()
    directions = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}
    x, y = 0, 0
    visited = {}

    for char in lines:
        deltaX, deltaY = directions[char]
        x += deltaX
        y += deltaY
        stringCoord = f"{x},{y}"

        if stringCoord in visited:
            visited[stringCoord] += 1
        else:
            visited[stringCoord] = 1

    print(len(visited))
