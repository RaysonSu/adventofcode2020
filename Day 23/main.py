def main_part_1(inp: str) -> str:
    numbers: dict[int, int] = {
        int(x) - 1: int(prev) - 1
        for prev, x in zip(inp[1:], inp)
    }
    numbers[int(inp[-1]) - 1] = int(inp[0]) - 1

    cup: int = int(inp[0]) - 1  # init
    for _ in range(100):
        pick_up_0: int = numbers[cup]  # p1
        pick_up_1: int = numbers[pick_up_0]  # p2
        pick_up_2: int = numbers[pick_up_1]  # p3
        after: int = numbers[pick_up_2]  # next

        dest: int = (cup - 1) % 9
        while dest == pick_up_0 or dest == pick_up_1 or dest == pick_up_2:
            dest -= 1
            dest %= 9

        dest_after: int = numbers[dest]  # b3

        numbers[cup] = after
        numbers[dest] = pick_up_0
        numbers[pick_up_2] = dest_after
        cup = after

    ret: str = ""
    prev: int = numbers[0]
    while prev:
        ret += str(prev + 1)
        prev = numbers[prev]

    return ret


def main_part_2(inp: str) -> int:
    numbers: dict[int, int] = {
        int(x) - 1: int(prev) - 1
        for prev, x in zip(inp[1:], inp)
    }
    numbers = numbers | {x: (x + 1) % 1000000 for x in range(9, 999999)}
    numbers[999999] = int(inp[0]) - 1
    numbers[int(inp[-1]) - 1] = 9

    cup: int = int(inp[0]) - 1  # init
    for _ in range(10000000):
        pick_up_0: int = numbers[cup]  # p1
        pick_up_1: int = numbers[pick_up_0]  # p2
        pick_up_2: int = numbers[pick_up_1]  # p3
        after: int = numbers[pick_up_2]  # next

        dest: int = (cup - 1) % 1000000
        while dest == pick_up_0 or dest == pick_up_1 or dest == pick_up_2:
            dest -= 1
            dest %= 1000000

        dest_after: int = numbers[dest]  # b3

        numbers[cup] = after
        numbers[dest] = pick_up_0
        numbers[pick_up_2] = dest_after

        ret: list[int] = []
        prev: int = numbers[0]
        while prev and len(ret) < 9:
            ret.append(prev)
            prev = numbers[prev]
        cup = after

    return (numbers[0] + 1) * (numbers[numbers[0]] + 1)


def main() -> None:
    test_input: str = "389125467"
    test_output_part_1_expected: str = "67384529"
    test_output_part_2_expected: int = 149245887792

    input_data: str = "643719258"

    test_output_part_1: str = main_part_1(test_input)
    test_output_part_2: int = main_part_2(test_input)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_data)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()

    if test_output_part_2_expected == test_output_part_2:
        print(f"Part 2: {main_part_2(input_data)}")
    else:
        print(f"Part 2 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_2_expected}")
        print(f"Got: {test_output_part_2}")


if __name__ == "__main__":
    main()
