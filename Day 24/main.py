from collections import defaultdict

OUTPUT_TYPE = int


class CellularAutomata:
    def __init__(self) -> None:
        self.points: set[tuple[int, int]] = set()

    def add_point(self, points: tuple[int, int] | list[tuple[int, int]]) -> None:
        if isinstance(points, list):
            for point in points:
                self.points.add(point)
        else:
            self.points.add(points)

    def generate_neighbours(self, point: tuple[int, int]) -> list[tuple[int, int]]:
        neighbours: list[tuple[int, int]] = []
        for x_diff, y_diff in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1)]:
            neighbours.append((point[0] + x_diff, point[1] + y_diff))

        return neighbours

    def count_neighbours(self, point: tuple[int, int]) -> int:
        lookup: int = 0
        for point in self.generate_neighbours(point):
            if point in self.points:
                lookup += 1

        return lookup

    def tick(self) -> None:
        new_points: set[tuple[int, int]] = set()
        for point in self.points:
            if self.count_neighbours(point) in [1, 2]:
                new_points.add(point)

            for neighbour in self.generate_neighbours(point):
                count: int = self.count_neighbours(neighbour)
                if neighbour not in self.points and count == 2:
                    new_points.add(neighbour)

        self.points = new_points


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    counts: defaultdict[tuple[int, int], int] = defaultdict(lambda: 0)

    for line in inp:
        line = line.replace("se", "r")
        line = line.replace("ne", "R")
        line = line.replace("sw", "l")
        line = line.replace("nw", "L")

        count = {char: line.count(char) for char in "ewrRlL"}
        counts[(
            count["e"] - count["w"] + count["R"] - count["l"],
            count["L"] - count["r"] + count["R"] - count["l"]
        )] += 1

    ret: int = 0
    for i in counts.values():
        ret += i % 2
    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    counts: defaultdict[tuple[int, int], int] = defaultdict(lambda: 0)

    for line in inp:
        line = line.replace("se", "r")
        line = line.replace("ne", "R")
        line = line.replace("sw", "l")
        line = line.replace("nw", "L")

        count = {char: line.count(char) for char in "ewrRlL"}
        counts[(
            count["e"] - count["w"] + count["R"] - count["l"],
            count["L"] - count["r"] + count["R"] - count["l"]
        )] += 1

    cell: CellularAutomata = CellularAutomata()
    for point, point_count in counts.items():
        if point_count % 2:
            cell.add_point(point)

    for _ in range(100):
        cell.tick()

    return len(cell.points)


def main() -> None:
    test_input: str = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 10
    test_output_part_2_expected: OUTPUT_TYPE = 2208

    file_location: str = "python/Advent of Code/2020/Day 24/input.txt"
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
