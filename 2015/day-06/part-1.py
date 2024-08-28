import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.read().splitlines()
    gridSize = 1000
    grid = [[False for _ in range(gridSize)] for _ in range(gridSize)]

    for line in lines:
        instruction = ""
        line = line.split(" ")
        coords1, coords2 = "", ""

        if len(line) == 4:
            instruction, coords1, _, coords2 = line
        else:
            _, instruction, coords1, _, coords2 = line

        x1, y1 = coords1.split(",")
        x2, y2 = coords2.split(",")

        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] = True if instruction == "on" else False if instruction == "off" else not grid[x][y]

    print(sum(1 for row in grid for cell in row if cell))
