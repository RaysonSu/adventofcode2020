OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> tuple[int, int]:
    numbers: list[int] = [int(num.strip()) for num in inp]
    return numbers[0], numbers[1]


def powerlog(base: int, value: int, mod: int = 20201227) -> int:
    guess: int = 1
    log: int = 0

    while guess != value:
        guess *= base
        guess %= mod
        log += 1

    return log


def modpow(value: int, power: int, mod: int = 20201227) -> int:
    ret: int = 1

    for _ in range(power):
        ret *= value
        ret %= mod

    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    card, door = parse_inp(inp)
    return modpow(card, powerlog(7, door))


def main() -> None:
    test_input: str = """5764801
17807724"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 14897079

    file_location: str = "python/Advent of Code/2020/Day 25/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: OUTPUT_TYPE = main_part_1(test_input_parsed)

    if test_output_part_1_expected == test_output_part_1:
        print(f"Part 1: {main_part_1(input_file)}")
    else:
        print(f"Part 1 testing error: ")
        print(f"Test input: {test_input}")
        print(f"Expected output: {test_output_part_1_expected}")
        print(f"Got: {test_output_part_1}")
        print()


if __name__ == "__main__":
    main()
