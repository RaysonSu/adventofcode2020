OUTPUT_TYPE = int


class CellularAutomata:
    def __init__(self, grid: list[str], part: int) -> None:
        self.grid: list[str] = grid
        self.determine_bounds()
        self.part: int = part

    def determine_bounds(self) -> None:
        self.bounds = (0, 0, len(self.grid[0]), len(self.grid))

    def in_bound(self, x: int, y: int) -> bool:
        return self.bounds[0] <= x and x < self.bounds[2] and self.bounds[1] <= y and y < self.bounds[3]

    def determine_future_point(self, x: int, y: int) -> str:
        if self.grid[y][x] == ".":
            return "."

        box: str = ""
        for y_diff in range(-1, 2):
            for x_diff in range(-1, 2):
                if x_diff == 0 and y_diff == 0:
                    continue

                if self.part == 1:
                    if self.in_bound(x + x_diff, y + y_diff):
                        box += self.grid[y + y_diff][x + x_diff]
                    else:
                        box += "."
                elif self.part == 2:
                    multiplier: int = 1
                    while self.in_bound(x + x_diff * multiplier, y + y_diff * multiplier):
                        if self.grid[y + y_diff * multiplier][x + x_diff * multiplier] in "#L":
                            box += self.grid[y + y_diff *
                                             multiplier][x + x_diff * multiplier]
                            break
                        multiplier += 1
                    else:
                        box += "."

        if self.grid[y][x] == "L":
            if "#" not in box:
                return "#"
            return "L"

        if self.grid[y][x] == "#":
            if box.count("#") >= 4 and self.part == 1:
                return "L"
            if box.count("#") >= 5 and self.part == 2:
                return "L"
            return "#"

        return ""

    def tick(self) -> bool:
        new_grid: list = []
        for y in range(self.bounds[1], self.bounds[3]):
            new_row: str = ""
            for x in range(self.bounds[0], self.bounds[2]):
                new_row += self.determine_future_point(x, y)
            new_grid.append(new_row)

        diffrent: bool = new_grid != self.grid
        self.grid = new_grid
        self.determine_bounds()

        return diffrent


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    grid: list[str] = [row.strip() for row in inp]
    cell: CellularAutomata = CellularAutomata(grid, 1)

    while cell.tick():
        pass

    return "".join(cell.grid).count("#")


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    grid: list[str] = [row.strip() for row in inp]
    cell: CellularAutomata = CellularAutomata(grid, 2)

    while cell.tick():
        pass

    return "".join(cell.grid).count("#")


def main() -> None:
    test_input: str = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: OUTPUT_TYPE = 37
    test_output_part_2_expected: OUTPUT_TYPE = 26

    file_location: str = "python/Advent of Code/2020/Day 11/input.txt"
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
