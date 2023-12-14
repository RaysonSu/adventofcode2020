F = open("python/Advent of Code/2020/Day 1/input.txt", "r")
F = list(map(int, F.readlines()))

for i in F:
    if 2020 - i in F:
        print(i, i * (2020 - i))
