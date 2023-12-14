F = open("python/Advent of Code/2020/Day 3/input.txt", "r")
F = list(map(str.strip, F.readlines()))

def check(down, right):
    total = 0
    row = len(F[0])

    for index, mapo in enumerate(F):
        if bool(index % down):
            continue
        if mapo[right * index // down % row] == "#":
            total += 1
    
    return total

def main():
    vals = [check(1, 1), check(1, 3), check(1, 5), check(1, 7), check(2, 1)]
    return vals[0] * vals[1] * vals[2] * vals[3] * vals[4]

print(main())
