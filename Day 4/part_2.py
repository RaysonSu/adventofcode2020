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
    def is_n_digits(string, n):
        return len(string) == n and string.isnumeric()
    
    def in_between(string, lower, upper):
        try:
            return int(string) <= upper and int(string) >= lower
        except:
            return False
    
    def valid_hgt(string):
        # check ending"
        if not (string.endswith("in") or string.endswith("cm")):
            return False

        try:
            suffix = string[-2:]
            prefix = int(string[:-2])
            multipliers = {"in": 1, "cm": 1 / 2.54}
            return in_between(prefix * multipliers[suffix], 59, 76)
        except:
            return False
    
    def valid_hcl(string):
        if not string.startswith("#"):
            return False
        
        string = string[1:]

        if len(string) != 6:
            return False
        
        try:
            string = int(string, base=16)
            return True
        except:
            return False
    
    total = 0
    for dictionary in inp:
        required = {"byr": lambda x: is_n_digits(x, 4) and in_between(x, 1920, 2002), 
                    "iyr": lambda x: is_n_digits(x, 4) and in_between(x, 2010, 2020), 
                    "eyr": lambda x: is_n_digits(x, 4) and in_between(x, 2020, 2030),
                    "hgt": valid_hgt, 
                    "hcl": valid_hcl, 
                    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                    "pid": lambda x: x.isnumeric() and len(x) == 9}
        
        if False in list(map(lambda x: x in dictionary.keys() and required[x](dictionary[x]), required.keys())):
            continue
        total += 1
    return total

print(main(parse_inp(F)))
