OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> None:
    return


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    values: dict[int, int] = {}
    zero_mask: int = 0
    one_mask: int = 0

    for line in inp:
        if line.startswith("mask = "):
            line = line[7:].strip()
            zero_mask = int(line.replace("X", "1"), 2)
            one_mask = int(line.replace("X", "0"), 2)
        else:
            index: int = int(line[line.index("[")+1:line.index("]")])
            value: int = int(line[line.index("=")+2:].strip())
            values[index] = value
            values[index] &= zero_mask
            values[index] |= one_mask
    return sum(values.values())


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    values: dict[int, int] = {}
    zero_mask: int = 0
    one_mask: int = 0
    extra_masks: list[int] = []

    for line in inp:
        if line.startswith("mask = "):
            line = line[7:].strip()
            zero_mask = int(line.replace("0", "1").replace("X", "0"), 2)
            one_mask = int(line.replace("X", "0"), 2)
            extra_mask: str = line.replace("1", "0")

            extra_masks = []
            for i in range(2 ** extra_mask.count("X")):
                tmp_mask: str = extra_mask
                for _ in range(extra_mask.count("X")):
                    digit: int
                    i, digit = divmod(i, 2)
                    tmp_mask = tmp_mask.replace("X", str(digit), 1)
                extra_masks.append(int(tmp_mask, 2))
        else:
            index: int = int(line[line.index("[")+1:line.index("]")])
            value: int = int(line[line.index("=")+2:].strip())
            index &= zero_mask
            index |= one_mask
            for mask in extra_masks:
                values[index + mask] = value

    return sum(values.values())


def main() -> None:
    test_input: str = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 51
    test_output_part_2_expected: OUTPUT_TYPE = 208

    file_location: str = "python/Advent of Code/2020/Day 14/input.txt"
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
