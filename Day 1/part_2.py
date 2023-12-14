F = open("python/Advent of Code/2020/Day 1/input.txt", "r")
F = list(map(int, F.readlines()))

for i in F:
    for j in F:
        if 2020 - i - j in F and i != j:
            print(i, i * j * (2020 - i - j))
