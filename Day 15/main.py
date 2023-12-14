OUTPUT_TYPE = int


def main_part_1(inp: str) -> OUTPUT_TYPE:
    sequence: list[int] = list(map(int, eval(f"[{inp}]")))
    prev_data: dict[int, int] = {}

    prev_value: int = sequence[-1]
    for value, key in enumerate(sequence[:-1]):
        prev_data[key] = value

    index: int = len(sequence)
    while index < 2020:
        next_value: int
        if prev_value in prev_data.keys():
            next_value = index - prev_data[prev_value] - 1
        else:
            next_value = 0
        prev_data[prev_value] = index - 1
        prev_value = next_value
        index += 1
    return prev_value


def main_part_2(inp: str) -> OUTPUT_TYPE:
    sequence: list[int] = list(map(int, eval(f"[{inp}]")))
    prev_data: dict[int, int] = {}

    prev_value: int = sequence[-1]
    for value, key in enumerate(sequence[:-1]):
        prev_data[key] = value

    index: int = len(sequence)
    while index < 30000000:
        next_value: int
        if prev_value in prev_data.keys():
            next_value = index - prev_data[prev_value] - 1
        else:
            next_value = 0
        prev_data[prev_value] = index - 1
        prev_value = next_value
        index += 1
    return prev_value


def main() -> None:
    test_input: str = """0,3,6"""
    test_output_part_1_expected: OUTPUT_TYPE = 436
    test_output_part_2_expected: OUTPUT_TYPE = 175594

    input_file: str = "6,3,15,13,1,0"

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input)
    test_output_part_2: OUTPUT_TYPE = main_part_2(test_input)

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
