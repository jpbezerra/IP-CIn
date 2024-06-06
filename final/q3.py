word = input()

for index in range(1, len(word) + 1):
    print(f"{word[-index]}", end='')