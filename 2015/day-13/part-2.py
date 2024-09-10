import os
from math import inf

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()
    arrangements = {"You": {}}

    for line in lines:
        line = line.split(" ")
        person = line[0]
        change = line[2]
        happiness = int(line[3])
        next_person = line[-1][:-1]
        arrangements.setdefault(person, {})[
            next_person] = happiness if change == "gain" else -happiness

    for person in dict.keys(arrangements):
        arrangements[person]["You"] = 0
        arrangements["You"][person] = 0

    people = list(dict.keys(arrangements))

    def dfs(start, path, res, visited):
        if start == len(people):
            res.append(path[:])
            return

        for i in range(len(people)):
            if visited[i]:
                continue

            path.append(people[i])
            visited[i] = True
            dfs(start + 1, path, res, visited)
            path.pop()
            visited[i] = False

    paths = []
    visited = [False] * len(people)
    dfs(0, [], paths, visited)

    max_happiness = -inf

    for path in paths:
        path_happiness = 0

        for i in range(len(path)):
            path_happiness += arrangements[path[i - 1]
                                           ][path[i]] + arrangements[path[i]][path[i - 1]]

        max_happiness = max(max_happiness, path_happiness)

    print(max_happiness)
