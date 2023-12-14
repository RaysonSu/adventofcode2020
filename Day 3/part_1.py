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
    return check(1, 3)

print(main())
