OUTPUT_TYPE = int


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    time: int = int(inp[0].strip())
    busses: list[int] = [int(i)
                         for i in eval(f"[{inp[1].strip().replace(',x', '')}]") if i != "x"]
    remainders: list[int] = [-time % bus for bus in busses]
    lowest: int = min(remainders)
    return lowest * busses[remainders.index(lowest)]


def chinese_remainder(divisors: list[int], remainders: list[int]) -> int:
    if len(remainders) == 1:
        return remainders[0] % divisors[0]

    divisors = divisors.copy()
    remainders = remainders.copy()

    a_1: int = remainders.pop()
    a_2: int = remainders.pop()

    n_1: int = divisors.pop()
    n_2: int = divisors.pop()

    m_1: int
    m_2: int
    m_1, m_2 = euclidian(n_1, n_2)

    divisors.append(n_1 * n_2)
    remainders.append((a_1 * m_2 * n_2 + a_2 * m_1 * n_1) % (n_1 * n_2))

    return chinese_remainder(divisors, remainders)


def euclidian(x: int, y: int) -> tuple[int, int]:
    r_0: int = x
    r_1: int = y

    s_0: int = 1
    s_1: int = 0

    t_0: int = 0
    t_1: int = 1

    while r_1:
        quotient: int = r_0 // r_1
        r_0, r_1 = r_1, r_0 % r_1
        s_0, s_1 = s_1, s_0 - quotient * s_1
        t_0, t_1 = t_1, t_0 - quotient * t_1

    return s_0, t_0


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    time: int = int(inp[0].strip())
    busses: list[int] = [int(i)
                         for i in eval(f"[{inp[1].strip().replace(',x', ',1')}]") if i != "x"]
    remainders: list[int] = list(range(len(busses)))
    i: int = 0
    while i < len(busses):
        if busses[i] == 1:
            del busses[i]
            del remainders[i]
        else:
            remainders[i] *= -1
            remainders[i] %= busses[i]
            i += 1

    return chinese_remainder(busses, remainders)


def main() -> None:
    test_input: str = """939
7,13,x,x,59,x,31,19"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 295
    test_output_part_2_expected: OUTPUT_TYPE = 1068781
    file_location: str = "python/Advent of Code/2020/Day 13/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()
    input_file = list(map(str.strip, input_file))

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
