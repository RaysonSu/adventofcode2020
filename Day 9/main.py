OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    data: list[int] = [int(i.strip()) for i in inp]
    for i in range(25, len(data)):
        val: int = data[i]
        box: list[int] = data[i - 25: i]

        success: bool = False
        for value in box:
            success = success or (val - value) in box

        if not success:
            return val
    return 0


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    data: list[int] = [int(i.strip()) for i in inp]
    invalid: int = 0
    for i in range(25, len(data)):
        val: int = data[i]
        box: list[int] = data[i - 25:i]

        success: int = False
        for value in box:
            success = success or (val - value) in box

        if not success:
            invalid = val
            break

    low: int = 0
    high: int = 0
    while True:
        total: int = sum(data[low:high])
        if total < invalid:
            high += 1
        elif total == invalid:
            break
        else:
            low += 1

    return min(data[low:high]) + max(data[low:high])


def main() -> None:
    test_input: str = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 0
    test_output_part_2_expected: OUTPUT_TYPE = 0

    file_location: str = "python/Advent of Code/2020/Day 9/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed)
    test_output_part_2: OUTPUT_TYPE = 0

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
