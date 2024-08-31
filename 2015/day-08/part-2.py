import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()
    original_chars = 0
    processed_chars = 0

    for line in lines:
        line = line.strip()
        original_chars += len(line)
        processed_chars += 2 + \
            sum(2 if char == "\\" or char == "\"" else 1 for char in line)

    print(processed_chars - original_chars)
