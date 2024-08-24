import os


def get_areas(sides: list[int]) -> list[int]:
    return [sides[0] * sides[1], sides[0] * sides[2], sides[1] * sides[2]]


with open(os.path.join(os.getcwd(), 'input.txt')) as f:
    lines = f.readlines()
    total_area: int = 0

    for line in lines:
        line = line.strip()
        sides = line.split('x')
        sides = [int(side) for side in sides]
        areas: list[int] = get_areas(sides)
        total_area += 2 * sum(areas) + min(areas)

    print(total_area)
