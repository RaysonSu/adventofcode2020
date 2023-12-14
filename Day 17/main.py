OUTPUT_TYPE = int


def parse_inp(inp: list[str]) -> None:
    return


class CellularAutomata1:
    def __init__(self) -> None:
        self.points: set[tuple[int, int, int]] = set()

    def add_point(self, points: tuple[int, int, int] | list[tuple[int, int, int]]) -> None:
        if isinstance(points, list):
            for point in points:
                self.points.add(point)
        else:
            self.points.add(points)

    def generate_neighbours(self, point: tuple[int, int, int]) -> list[tuple[int, int, int]]:
        neighbours: list[tuple[int, int, int]] = []
        for z_diff in range(-1, 2):
            for y_diff in range(-1, 2):
                for x_diff in range(-1, 2):
                    if x_diff == 0 and y_diff == 0 and z_diff == 0:
                        continue
                    neighbours.append(
                        (point[0] + x_diff, point[1] + y_diff, point[2] + z_diff))

        return neighbours

    def determine_future_point(self, point: tuple[int, int, int]) -> int:
        lookup: int = 0
        for point in self.generate_neighbours(point):
            if point in self.points:
                lookup += 1

        return lookup

    def tick(self) -> None:
        new_points: set[tuple[int, int, int]] = set()
        for point in self.points:
            if self.determine_future_point(point) in [2, 3]:
                new_points.add(point)

            for neighbour in self.generate_neighbours(point):
                count: int = self.determine_future_point(neighbour)
                if neighbour in self.points and count in [2, 3]:
                    new_points.add(neighbour)
                elif neighbour not in self.points and count == 3:
                    new_points.add(neighbour)

        self.points = new_points


class CellularAutomata2:
    def __init__(self) -> None:
        self.points: set[tuple[int, int, int, int]] = set()

    def add_point(self, points: tuple[int, int, int, int] | list[tuple[int, int, int, int]]) -> None:
        if isinstance(points, list):
            for point in points:
                self.points.add(point)
        else:
            self.points.add(points)

    def generate_neighbours(self, point: tuple[int, int, int, int]) -> list[tuple[int, int, int, int]]:
        neighbours: list[tuple[int, int, int, int]] = []
        for w_diff in range(-1, 2):
            for z_diff in range(-1, 2):
                for y_diff in range(-1, 2):
                    for x_diff in range(-1, 2):
                        if x_diff == 0 and y_diff == 0 and z_diff == 0 and w_diff == 0:
                            continue
                        neighbours.append(
                            (point[0] + x_diff, point[1] + y_diff, point[2] + z_diff, point[3] + w_diff))

        return neighbours

    def determine_future_point(self, point: tuple[int, int, int, int]) -> int:
        lookup: int = 0
        for point in self.generate_neighbours(point):
            if point in self.points:
                lookup += 1

        return lookup

    def tick(self) -> None:
        new_points: set[tuple[int, int, int, int]] = set()
        for point in self.points:
            if self.determine_future_point(point) in [2, 3]:
                new_points.add(point)

            for neighbour in self.generate_neighbours(point):
                count: int = self.determine_future_point(neighbour)
                if neighbour in self.points and count in [2, 3]:
                    new_points.add(neighbour)
                elif neighbour not in self.points and count == 3:
                    new_points.add(neighbour)

        self.points = new_points


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    cell: CellularAutomata1 = CellularAutomata1()
    grid: list[tuple[int, int, int]] = []

    for y, row in enumerate(inp):
        for x, char in enumerate(row.strip()):
            if char == "#":
                grid.append((x, y, 0))

    cell.add_point(grid)
    for _ in range(6):
        cell.tick()

    return len(cell.points)


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    cell: CellularAutomata2 = CellularAutomata2()
    grid: list[tuple[int, int, int, int]] = []

    for y, row in enumerate(inp):
        for x, char in enumerate(row.strip()):
            if char == "#":
                grid.append((x, y, 0, 0))

    cell.add_point(grid)
    for _ in range(6):
        cell.tick()

    return len(cell.points)


def main() -> None:
    test_input: str = """.#.
..#
###"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 112
    test_output_part_2_expected: OUTPUT_TYPE = 848

    file_location: str = "python/Advent of Code/2020/Day 17/input.txt"
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
