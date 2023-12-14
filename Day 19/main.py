OUTPUT_TYPE = int


def parse_inp(inp: list[str], part: int = 1) -> tuple[dict[str, set[str]], list[str]]:
    split: int = inp.index("\n")
    tests: list[str] = inp[:split]
    strings: list[str] = inp[split+1:]

    valid_strings: dict[str, set[str]] = {}
    while tests:
        confused: list[str] = []
        for line in tests:
            line = line.strip()
            index: str = line.split(":")[0]
            conditions: str = line.split(": ")[1]

            if "\"" in conditions:
                valid_strings[index] = {conditions[1]}
                continue

            if part == 2:
                if index in [0, 8, 11]:
                    continue

            options: list[str] = conditions.split(" | ")
            valid: set[str] = set()
            for row in options:
                data = row.split(" ")
                try:
                    if len(data) == 1:
                        valid = valid.union(valid_strings[data[0]])
                    elif len(data) == 2:
                        valid = valid.union(
                            {x + y for x in valid_strings[data[0]] for y in valid_strings[data[1]]})
                    elif len(data) == 3:
                        print("well crap")
                except:
                    break
            else:
                valid_strings[index] = valid
                continue

            confused.append(line)
        tests = confused

    return valid_strings, list(map(str.strip, strings))


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    valid_strings: dict[str, set[str]]
    strings: list[str]

    valid_strings, strings = parse_inp(inp)

    ret: int = 0
    for string in strings:
        if string in valid_strings["0"]:
            ret += 1
    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    valid_strings: dict[str, set[str]]
    strings: list[str]

    valid_strings, strings = parse_inp(inp, 2)

    ret: int = 0
    length_31: int = max([len(i) for i in valid_strings["31"]])
    length_42: int = max([len(i) for i in valid_strings["42"]])
    for string in strings:
        matched_31: int = 0
        matched_42: int = 0
        while string[-length_31:] in valid_strings["31"]:
            string = string[:-length_31]
            matched_31 += 1

        while string[:length_42] in valid_strings["42"]:
            string = string[length_42:]
            matched_42 += 1

        if matched_31 > 0 and matched_42 > matched_31 and string == "":
            ret += 1
    return ret


def main() -> None:
    test_input: str = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""
    test_input_parsed: list[str] = test_input.splitlines(True)
    test_output_part_1_expected: OUTPUT_TYPE = 3
    test_output_part_2_expected: OUTPUT_TYPE = 12

    file_location: str = "python/Advent of Code/2020/Day 19/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed)
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input_parsed)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    if test_output_part_2_expected == test_output_part_2:
        print(f"Part 2: {main_part_2(input_file)}")
    else:
        print(f"Part 2 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_2_expected}")
        print(f"Got: {test_output_part_2}")


if __name__ == "__main__":
    main()
