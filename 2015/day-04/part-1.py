from hashlib import md5

secret = "bgvyzdsv"
counter = 0

while True:
    hash = md5(f"{secret}{counter}".encode()).hexdigest()

    if hash.startswith("00000"):
        print(counter)
        break

    counter += 1
