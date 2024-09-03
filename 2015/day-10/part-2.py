def generate_sequence(input_str):
    count = 0
    last_char = input_str[0]
    new_sequence = ""

    for i in range(len(input_str)):
        char = input_str[i]

        if char != last_char:
            new_sequence += f"{count}{last_char}"
            count = 1
            last_char = char
        else:
            count += 1

    new_sequence += f"{count}{last_char}"

    return new_sequence


input_str = "1113222113"

for _ in range(50):
    input_str = generate_sequence(input_str)

print(len(input_str))
