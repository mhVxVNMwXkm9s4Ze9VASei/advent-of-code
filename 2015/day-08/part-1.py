import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    lines = f.read().splitlines()
    total_chars = 0
    total_processed_chars = 0

    for line in lines:
        line = line.strip()
        line_len = len(line)
        char_count = 0
        i = 0

        while i < line_len:
            skip = 0

            if line[i] == "\\":
                if line[i + 1] == "\"" or line[i + 1] == "\\":
                    skip += 1
                else:
                    skip += 3

            char_count += 1
            i += 1 + skip

        total_chars += line_len
        total_processed_chars += char_count - 2

    print(total_chars - total_processed_chars)
