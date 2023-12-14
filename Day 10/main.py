OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    data: list[int] = [int(num.strip()) for num in inp]
    data.sort()
    diffrences: dict[int, int] = {1: 1, 2: 0, 3: 1}
    for i in range(len(data) - 1):
        diff: int = data[i + 1] - data[i]
        diffrences[diff] += 1

    return diffrences[3] * diffrences[1]


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    data: list[int] = [int(num.strip()) for num in inp]
    data.append(0)

    running_total: list[int] = [0 for _ in range(max(data) + 1)]
    running_total[0] += 1

    for i in range(max(data) + 1):
        for j in range(1, 4):
            if i - j in data:
                running_total[i] += running_total[i - j]

    return running_total[-1]


def main() -> None:
    test_input: str = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 220
    test_output_part_2_expected: OUTPUT_TYPE = 19208

    file_location: str = "python/Advent of Code/2020/Day 10/input.txt"
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
