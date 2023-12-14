OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    decks: tuple[list[int], list[int]] = ([], [])
    player: int = 0
    for line in inp:
        line = line.strip()

        if line == "":
            player += 1
            continue

        if not line.isnumeric():
            continue

        decks[player].append(int(line))
    return tuple(decks[0]), tuple(decks[1])


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    player_1: tuple[int, ...]
    player_2: tuple[int, ...]

    player_1, player_2 = parse_inp(inp)
    while player_1 and player_2:
        p1: int = player_1[0]
        p2: int = player_2[0]

        player_1 = player_1[1:]
        player_2 = player_2[1:]

        if p1 > p2:
            player_1 += (p1, p2)
        else:
            player_2 += (p2, p1)

    ret: int = 0
    ret += sum([index * value for index, value in enumerate(player_1[::-1], 1)])
    ret += sum([index * value for index, value in enumerate(player_2[::-1], 1)])

    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    player_1: tuple[int, ...]
    player_2: tuple[int, ...]

    player_1, player_2 = parse_inp(inp)

    def combat(player_1: tuple[int, ...], player_2: tuple[int, ...], extra: bool = False) -> bool | tuple[bool, tuple[int, ...]]:
        turns: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
        while player_1 and player_2:
            if (player_1, player_2) in turns:
                if extra:
                    return True, player_1
                return True

            turns.add((player_1, player_2))

            p1: int = player_1[0]
            p2: int = player_2[0]

            player_1 = player_1[1:]
            player_2 = player_2[1:]
            if len(player_1) >= p1 and len(player_2) >= p2:
                if combat(player_1[:p1], player_2[:p2]):
                    player_1 += (p1, p2)
                else:
                    player_2 += (p2, p1)
            elif p1 > p2:
                player_1 += (p1, p2)
            else:
                player_2 += (p2, p1)

        if player_1:
            if extra:
                return True, player_1
            return True

        if extra:
            return False, player_2
        return False

    return sum([index * value for index, value in enumerate(combat(player_1, player_2, True)[1][::-1], 1)])


def main() -> None:
    test_input: str = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 306
    test_output_part_2_expected: OUTPUT_TYPE = 291

    file_location: str = "python/Advent of Code/2020/Day 22/input.txt"
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
