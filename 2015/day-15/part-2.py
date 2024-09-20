import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()
    ingredients = []

    for line in lines:
        line = line.split(": ")[1]
        traits = line.split(", ")
        ingredient = {}

        for item in traits:
            trait, score = item.split(" ")
            ingredient[trait] = int(score)

        ingredients.append(ingredient)

    def digitCombos(target, path, res):
        comboLength = len(path)
        total = sum(path)

        if comboLength == 4:
            if total == target:
                res.add(tuple(path))

            return

        remaining = target - total

        for i in range(0, remaining + 1):
            path.append(i)
            digitCombos(target, path, res)
            path.pop()

    combos = set()
    digitCombos(100, [], combos)
    score = 0
    traits = ingredients[0].keys()

    for combo in combos:
        comboTotal = 1
        calories = sum(combo[i] * ingredients[i]["calories"]
                       for i in range(len(ingredients)))

        if calories != 500:
            continue

        for trait in traits:
            if trait == "calories":
                continue

            traitTotal = sum(combo[i] * ingredients[i][trait]
                             for i in range(len(ingredients)))

            traitTotal = max(0, traitTotal)
            comboTotal *= traitTotal

            if traitTotal == 0:
                break

        score = max(score, comboTotal)

    print(score)
