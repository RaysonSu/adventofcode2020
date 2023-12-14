F = open("python/Advent of Code/2020/Day 2/input.txt", "r")
F = F.readlines()

total = 0

for i in F:
    p1 = i.split(":")
    string = p1[1][:-1]
    char = p1[0][-1]
    p5 = list(map(int, p1[0].split(" ")[0].split("-")))
    if p5[0] <= string.count(char) and p5[1] >= string.count(char):
        total += 1

print(total)
