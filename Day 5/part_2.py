F = open("python/Advent of Code/2020/Day 5/input.txt", "r")
F = list(map(str.strip, F.readlines()))

def parse_inp(F):
    return list(map(lambda x: int(x.replace("R", "1").replace("L", "0").replace("F", "0").replace("B", "1"), base=2), F))

def main(inp):
    missing = [i for i in range(1024) if i not in inp]
    for i in range(len(missing) - 1):
        if missing[i + 1] - missing[i] > 1:
            return missing[i + 1]

print(main(parse_inp(F)))
