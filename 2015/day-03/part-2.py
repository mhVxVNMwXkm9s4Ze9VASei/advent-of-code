import os

with open(os.path.join(os.getcwd(), 'input.txt')) as f:
    lines = f.readlines()[0].strip()
    directions = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}
    robotX, robotY = 0, 0
    santaX, santaY = 0, 0
    visited = {}
    santa = True

    for char in lines:
        deltaX, deltaY = directions[char]
        stringCoord = ""

        if santa:
            santaX += deltaX
            santaY += deltaY
            stringCoord = f"{santaX},{santaY}"
        else:
            robotX += deltaX
            robotY += deltaY
            stringCoord = f"{robotX},{robotY}"

        if stringCoord in visited:
            visited[stringCoord] += 1
        else:
            visited[stringCoord] = 1

        santa = not santa

    print(len(visited))
