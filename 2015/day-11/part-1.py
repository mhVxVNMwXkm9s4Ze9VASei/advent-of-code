current_password = input("Enter password: ")
password_len = len(current_password)
converted_password = [ord(char) - 96 for char in current_password]
forbidden_chars = set(ord(char) - 96 for char in "ilo")


def check_password(password):
    has_increasing_sequence = False
    increasing_sequence_count = 1
    repeating_chars = 0
    repeating_pairs = 0

    for i in range(password_len):
        if password[i] in forbidden_chars:
            return False

        if i > 0 and password[i] - password[i - 1] == 1:
            increasing_sequence_count += 1

            if increasing_sequence_count == 3:
                has_increasing_sequence = True
        else:
            increasing_sequence_count = 1

        if i > 0 and password[i] == password[i - 1]:
            repeating_chars += 1 if password[i] == password[i -
                                                            2] and i > 1 else 2

    repeating_pairs = repeating_chars // 2

    return has_increasing_sequence and repeating_pairs >= 2


def update_password(password):
    i = password_len - 1
    password[i] += 1

    while i > 0:
        if password[i] == 27:
            password[i] = 1

            if i > 0:
                password[i - 1] += 1

        if password[i] in forbidden_chars:
            return password[0:i] + [password[i] + 1] + [1] * (password_len - i - 1)

        i -= 1

    return password


is_valid_password = check_password(converted_password)

while not is_valid_password:
    converted_password = update_password(converted_password)
    is_valid_password = check_password(converted_password)

print("".join(chr(char + 96) for char in converted_password))
