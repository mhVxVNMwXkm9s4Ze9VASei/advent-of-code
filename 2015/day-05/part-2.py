import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.read().splitlines()
    count = 0

    for line in lines:
        has_repeating_pair = False
        has_separated_chars = False
        has_overlapping_pairs = False
        matching_pairs = 0
        pairs = set([line[0:2]])

        for i in range(len(line) - 1):
            next_char = line[i + 1]
            prev_char = line[i - 1]

            current_pair = f"{line[i]}{next_char}"
            prev_pair = f"{prev_char}{line[i]}"
            pairs_overlap = current_pair == prev_pair

            if i > 0 and i < len(line) - 1:
                if next_char == prev_char and not has_separated_chars:
                    has_separated_chars = True

                if current_pair not in pairs:
                    pairs.add(current_pair)
                else:
                    has_repeating_pair = True
                    matching_pairs += 1

                if pairs_overlap and not has_overlapping_pairs:
                    has_overlapping_pairs = True

        if has_repeating_pair and has_separated_chars and (not has_overlapping_pairs or (has_overlapping_pairs and matching_pairs > 1)):
            count += 1

    print(count)
