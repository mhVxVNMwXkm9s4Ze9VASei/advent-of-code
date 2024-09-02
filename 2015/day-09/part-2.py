import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()
    distances = {}

    for line in lines:
        origin, _, destination, _, distance = line.strip().split(" ")
        distance = int(distance)

        if origin not in distances:
            distances[origin] = {}

        if destination not in distances:
            distances[destination] = {}

        if origin not in distances[destination]:
            distances[destination][origin] = distance

        if destination not in distances[origin]:
            distances[origin][destination] = distance

    cities = list(dict.keys(distances))

    def dfs(start, path, res, visited):
        if start == len(cities):
            res.append(path[:])
            return

        for i in range(len(cities)):
            if visited[i]:
                continue

            path.append(cities[i])
            visited[i] = True
            dfs(start + 1, path, res, visited)
            path.pop()
            visited[i] = False

    paths = []
    visited = [False] * len(cities)
    dfs(0, [], paths, visited)

    paths_distances = []

    for path in paths:
        path_distance = 0

        for i in range(1, len(path)):
            path_distance += distances[path[i - 1]][path[i]]

        paths_distances.append(path_distance)

    print(max(paths_distances))
