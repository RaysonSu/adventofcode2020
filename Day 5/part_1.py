F = open("python/Advent of Code/2020/Day 5/input.txt", "r")
F = list(map(str.strip, F.readlines()))

def parse_inp(F):
    return list(map(lambda x: x.replace("R", "1").replace("L", "0").replace("F", "0").replace("B", "1"), F))

def main(inp):
    return max(map(lambda x: int(x, base=2), inp))

print(main(parse_inp(F)))
