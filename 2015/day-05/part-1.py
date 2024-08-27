import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.read().splitlines()
    count = 0
    forbidden_chars = set(["ab", "cd", "pq", "xy"])
    vowels = set("aeiou")

    for line in lines:
        has_forbidden_chars = False
        has_repeated_chars = False
        vowel_count = 1 if line[0] in vowels else 0

        for i in range(1, len(line)):
            if f"{line[i - 1]}{line[i]}" in forbidden_chars:
                has_forbidden_chars = True
                break

            if line[i - 1] == line[i]:
                has_repeated_chars = True

            if line[i] in vowels:
                vowel_count += 1

        if not has_forbidden_chars and has_repeated_chars and vowel_count >= 3:
            count += 1

    print(count)
