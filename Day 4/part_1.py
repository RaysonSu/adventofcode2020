F = open("python/Advent of Code/2020/Day 4/input.txt", "r")
F = list(map(str.strip, F.readlines()))

def parse_inp(F):
    ret = []
    current = {}

    for i in F:
        if len(i) == 0:
            ret.append(current.copy())
            current = {}
            continue
            
        i = i.strip().split(" ")
        for pair in i:
            if pair == "":
                continue
            pair = pair.split(":")
            current[pair[0]] = pair[1]

    return ret

def main(inp):
    total = 0
    for dictionary in inp:
        required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        if False in list(map(lambda x: x in dictionary.keys(), required.copy())):
            continue
        total += 1
    return total

print(main(parse_inp(F)))
