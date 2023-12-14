OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> None:
    return


def solve_quadratic(b: int | float, c: int | float) -> float:
    return (-b - (b ** 2 - 4 * c) ** 0.5) / 2


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    inp = "".join([row.replace("\n", "") + "\n" for row in inp]).split("\n\n")
    ret: int = 0
    for row in inp:
        ret += len(set(row.replace("\n", "")))
    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    inp = "".join([row.replace("\n", "") + "\n" for row in inp]).split("\n\n")
    ret: int = 0
    for row in inp:
        row = row.strip()
        data: list[str] = row.split("\n")
        valid: set[str] = set(data[0])
        for person in data:
            valid = valid.intersection(set(person))
        ret += len(valid)
    return ret


def main() -> None:
    test_input: str = """abc

a
b
c

ab
ac

a
a
a
a

b"""
    test_input_parsed: list[str] = test_input.splitlines()
    test_output_part_1_expected: OUTPUT_TYPE = 11
    test_output_part_2_expected: OUTPUT_TYPE = 6

    file_location: str = "python/Advent of Code/2020/Day 6/input.txt"
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
