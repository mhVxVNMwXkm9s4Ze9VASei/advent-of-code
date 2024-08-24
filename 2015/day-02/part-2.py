import os


def get_ribbon(sides: list[int]) -> int:
    perimeters = [sides[0] + sides[1],
                  sides[0] + sides[2], sides[1] + sides[2]]
    perimeters = [perimeter * 2 for perimeter in perimeters]
    bow = 1

    for side in sides:
        bow *= side

    return min(perimeters) + bow


with open(os.path.join(os.getcwd(), 'input.txt')) as f:
    lines = f.readlines()
    total_ribbon: int = 0

    for line in lines:
        line = line.strip()
        sides = line.split('x')
        sides = [int(side) for side in sides]
        total_ribbon += get_ribbon(sides)

    print(total_ribbon)
