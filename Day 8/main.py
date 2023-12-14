OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    index: int = 0
    acc: int = 0
    seen: list[int] = []
    while index not in seen:
        instruction: list[str] = inp[index].strip().split(" ")
        seen.append(index)
        if instruction[0] == "nop":
            index += 1
            continue
        elif instruction[0] == "acc":
            index += 1
            acc += int(instruction[1])
        elif instruction[0] == "jmp":
            index += int(instruction[1])
    return acc


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    for row in range(len(inp)):
        program: list[str] = inp.copy()
        if inp[row].startswith("acc"):
            continue
        elif inp[row].startswith("jmp"):
            program[row] = "nop" + program[row][3:]
        else:
            program[row] = "jmp" + program[row][3:]

        try:
            index: int = 0
            acc: int = 0
            seen: list[int] = []
            while index not in seen:
                instruction: list[str] = program[index].strip().split(" ")
                seen.append(index)
                if instruction[0] == "nop":
                    index += 1
                    continue
                elif instruction[0] == "acc":
                    index += 1
                    acc += int(instruction[1])
                elif instruction[0] == "jmp":
                    index += int(instruction[1])
        except:
            return acc


def main() -> None:
    test_input: str = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 5
    test_output_part_2_expected: OUTPUT_TYPE = 8

    file_location: str = "python/Advent of Code/2020/Day 8/input.txt"
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
