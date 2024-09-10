import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()
    contestants = []
    elapsed_time = 2503

    for line in lines:
        line = line.split(" ")
        contestants.append({
            "speed": int(line[3]),
            "flying_time": int(line[6]),
            "rest_time": int(line[-2]),
            "remaining_time": int(line[6]),
            "is_flying": True,
            "distance": 0,
            "points": 0
        })

    for _ in range(elapsed_time):
        for contestant in contestants:
            contestant["remaining_time"] -= 1

            if contestant["is_flying"]:
                contestant["distance"] += contestant["speed"]

            if contestant["remaining_time"] == 0:
                contestant["is_flying"] = not contestant["is_flying"]
                contestant["remaining_time"] = contestant["flying_time"] if contestant["is_flying"] else contestant["rest_time"]

        max_distance = max(contestant["distance"]
                           for contestant in contestants)

        for contestant in contestants:
            if contestant["distance"] == max_distance:
                contestant["points"] += 1

    print(max(contestant["points"] for contestant in contestants))
