from functools import cmp_to_key
OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> dict[str, list[tuple[str, int]]]:
    ret: dict[str, list[tuple[str, int]]] = {}
    for row in inp:
        row = row.replace("bags", "bag")

        bag_type: str
        bag_type, row = tuple(row.split(" bag contain "))
        if row == "no other bag.":
            ret[bag_type] = []
            continue

        items: list[tuple[str, int]] = []
        for contains in row[:-1].split(", "):
            # 1 dark olive bag
            amount: int
            contains_type: str
            amount, contains_type = tuple(contains.split(" ", 1))
            items.append((contains_type[:-4], int(amount)))

        ret[bag_type] = items
    return ret


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    seen: set[str] = {"shiny gold"}
    prev_seen: set[str] = set()
    while prev_seen != seen:
        prev_seen = seen.copy()
        for row in inp:
            for bag in seen.copy():
                if bag in row:
                    seen.add(row.split(" bags")[0])
    return len(seen) - 1


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    bag_containment: dict[str, list[tuple[str, int]]] = parse_inp(inp)
    counted: dict[str, int] = {}

    def compute(color: str) -> int:
        if color in counted.keys():
            return counted[color]

        ret: int = 1
        for subcolor, amount in bag_containment[color]:
            ret += compute(subcolor) * amount
        counted[color] = ret

        return ret

    return compute("shiny gold") - 1


def main() -> None:
    test_input: str = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 4
    test_output_part_2_expected: OUTPUT_TYPE = 32

    file_location: str = "python/Advent of Code/2020/Day 7/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()
    input_file = [x.replace("\n", "") for x in input_file]

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
