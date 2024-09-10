import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()
    max_distance = 0
    elapsed_time = 2503

    for line in lines:
        line = line.split(" ")
        speed = int(line[3])
        flying_time = int(line[6])
        rest_time = int(line[-2])
        total_time = flying_time + rest_time
        total_distance = speed * \
            ((flying_time * (elapsed_time // total_time)) +
             min(flying_time, elapsed_time % total_time))
        max_distance = max(max_distance, total_distance)

    print(max_distance)
