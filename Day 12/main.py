OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    coords: list[int] = [0, 0]
    mapping: dict[int, list[int]] = {
        0: [1, 0], 90: [0, 1], 180: [-1, 0], 270: [0, -1]}
    angle: int = 0
    for line in inp:
        action: str = line[0]
        amount: int = int(line[1:].strip())
        if action == "N":
            coords[1] += amount
        elif action == "S":
            coords[1] -= amount
        elif action == "E":
            coords[0] += amount
        elif action == "W":
            coords[0] -= amount
        elif action == "L":
            angle += amount
            angle %= 360
        elif action == "R":
            angle -= amount
            angle %= 360
        elif action == "F":
            coords[0] += mapping[angle][0] * amount
            coords[1] += mapping[angle][1] * amount

    return sum(map(abs, coords))


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    coords: list[int] = [0, 0]
    waypoint: list[int] = [10, 1]
    for line in inp:
        action: str = line[0]
        amount: int = int(line[1:].strip())
        if action == "N":
            waypoint[1] += amount
        elif action == "S":
            waypoint[1] -= amount
        elif action == "E":
            waypoint[0] += amount
        elif action == "W":
            waypoint[0] -= amount
        elif action in "LR":
            if action == "R":
                amount *= -1
            amount %= 360
            for _ in range(amount // 90):
                waypoint = [-waypoint[1], waypoint[0]]
        elif action == "F":
            coords[0] += waypoint[0] * amount
            coords[1] += waypoint[1] * amount

    return sum(map(abs, coords))


def main() -> None:
    test_input: str = """F10
N3
F7
R90
F11"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 25
    test_output_part_2_expected: OUTPUT_TYPE = 286

    file_location: str = "python/Advent of Code/2020/Day 12/input.txt"
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
