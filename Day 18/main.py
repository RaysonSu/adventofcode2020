OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> None:
    return


def compute(line: str) -> int:
    line = line[1:-1]
    if "+" not in line and "*" not in line:
        return int(line)

    paren_depth: int = 0
    for index, char in enumerate(line):
        if char == "(":
            paren_depth += 1
        elif char == ")":
            paren_depth -= 1
        elif paren_depth == 0:
            first: str = line[:index]
            second: str = line[index+1:]

            first = f"({first})"
            second = f"({second})"

            if char == "+":
                return compute(first) + compute(second)
            if char == "*":
                return compute(first) * compute(second)
    return compute(line)


def compute_2(line: str) -> int:
    line = line[1:-1]
    if "+" not in line and "*" not in line:
        return int(line)

    paren_depth: int = 0
    for index, char in enumerate(line):
        if char == "(":
            paren_depth -= 1
        elif char == ")":
            paren_depth += 1
        elif paren_depth == 0 and char == "*":
            first: str = line[:index]
            second: str = line[index+1:]

            first = f"){first}("
            second = f"){second}("

            return compute_2(first) * compute_2(second)

    for index, char in enumerate(line):
        if char == "(":
            paren_depth -= 1
        elif char == ")":
            paren_depth += 1
        elif paren_depth == 0 and char == "+":
            first = line[:index]
            second = line[index+1:]

            first = f"){first}("
            second = f"){second}("

            return compute_2(first) + compute_2(second)

    return compute_2(line)


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    ret: int = 0
    for line in inp:
        line = "(" + \
            line.replace(" ", "") \
            .replace("(", "v") \
            .replace(")", "(") \
            .replace("v", ")") \
            .strip()[::-1] + ")"
        ret += compute(line)
    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    ret: int = 0
    for line in inp:
        line = "(" + line.replace(" ", "").strip() + ")"
        ret += compute_2(line[::-1])
    return ret


def main() -> None:
    test_input: str = """1 + 2 * 3 + 4 * 5 + 6"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 71
    test_output_part_2_expected: OUTPUT_TYPE = 231

    file_location: str = "python/Advent of Code/2020/Day 18/input.txt"
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
