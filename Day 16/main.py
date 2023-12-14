OUTPUT_TYPE = int


def parse_inp(inp: str) -> tuple[list[set[int]], list[int], list[list[int]]]:
    text: list[str] = inp.split("\n\n")
    ranges: list[set[int]] = []
    for i in text[0].split("\n"):
        i = i.split(": ")[1]
        numbers: list[str] = i.split(" or ")
        range_set: set[int] = set()
        for number_range in numbers:
            range_set = range_set.union(
                range(int(number_range.split("-")[0]),
                      int(number_range.split("-")[1]) + 1)
            )
        ranges.append(range_set)

    self_ticket: list[int] = list(
        map(int, eval(f"[{text[1].splitlines()[1]}]")))

    other_tickets: list[list[int]] = []
    for ticket in text[2].split("\n")[1:]:
        other_tickets.append(list(map(int, eval(f"[{ticket.strip()}]"))))

    return ranges, self_ticket, other_tickets


def main_part_1(inp: str) -> OUTPUT_TYPE:
    ranges: list[set[int]]
    other_tickets: list[list[int]]
    ranges, _, other_tickets = parse_inp(inp)

    all_range: set[int] = set()
    for single_range in ranges:
        all_range = all_range.union(single_range)

    ret: int = 0
    for ticket in other_tickets:
        for number in ticket:
            if number not in all_range:
                ret += number
                break

    return ret


def main_part_2(inp: str) -> OUTPUT_TYPE:
    ranges: list[set[int]]
    self_ticket: list[int]
    other_tickets: list[list[int]]
    ranges, self_ticket, other_tickets = parse_inp(inp)

    all_range: set[int] = set()
    for single_range in ranges:
        all_range = all_range.union(single_range)

    valid_tickets: list[list[int]] = []
    for ticket in other_tickets:
        for number in ticket:
            if number not in all_range:
                break
        else:
            valid_tickets.append(ticket)

    ticket_data: list[set[int]] = [
        {valid_tickets[j][i] for j in range(len(valid_tickets))}
        for i in range(len(ranges))
    ]

    possibilities: list[list[int]] = []
    for i in ranges:
        this_possibilities: list[int] = []
        for index, j in enumerate(ticket_data):
            if len(j.difference(i)) == 0:
                this_possibilities.append(index)
        possibilities.append(this_possibilities)

    options: list[int] = [-1 for _ in range(len(ticket_data))]
    while -1 in options:
        lengths: list[int] = [len(option) for option in possibilities]
        index = lengths.index(1)
        real: int = possibilities[index][0]
        for option in range(len(possibilities)):
            if real in possibilities[option]:
                possibilities[option].remove(real)
        options[index] = real

    ret: int = 1
    for index in options[:6]:
        ret *= self_ticket[index]

    return ret


def main() -> None:
    test_input: str = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""
    test_output_part_1_expected: OUTPUT_TYPE = 0
    test_output_part_2_expected: OUTPUT_TYPE = 1716

    file_location: str = "python/Advent of Code/2020/Day 16/input.txt"
    input_file: str = open(file_location, "r").read()

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
