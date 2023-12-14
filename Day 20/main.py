from math import log2
from collections import defaultdict
OUTPUT_TYPE = int


def parse_inp(inp: list[str], reverse: bool = True) -> tuple[dict[int, tuple[int, int, int, int]], dict[int, list[str]]]:
    ret: dict[int, tuple[int, int, int, int]] = {}
    tiles: dict[int, list[str]] = {}
    for i in range(len(inp) // 12 + 1):
        key: int
        value: tuple[int, int, int, int]
        key, value = (parse_tile([row.strip()
                                  for row in inp[12 * i: 12 * i + 11]], reverse))
        ret[key] = value

        tiles[key] = [row.strip() for row in inp[12 * i + 1: 12 * i + 11]]

    return ret, tiles


def hash_str(string: str, reverse: bool) -> int:
    replaced: str = string.replace(".", "0").replace("#", "1")
    if reverse:
        return int(1000 * log2(1 + int(replaced, 2)) * log2(1 + int(replaced[::-1], 2)))
    else:
        return int(replaced, 2)


def parse_tile(tile: list[str], reverse: bool) -> tuple[int, tuple[int, int, int, int]]:
    id_num: int = int(tile[0][5:-1])
    tile = tile[1:]
    top: int = hash_str(tile[0].strip()[::-1], reverse)
    bottom: int = hash_str(tile[9].strip(), reverse)
    left: int = hash_str("".join([tile[i][0] for i in range(10)]), reverse)
    right: int = hash_str("".join([tile[i][9]
                          for i in range(10)])[::-1], reverse)

    return id_num, (top, left, bottom, right)


def main_part_1(inp: list[str]) -> OUTPUT_TYPE:
    data: dict[int, tuple[int, int, int, int]]
    data, _ = parse_inp(inp)

    seen: defaultdict = defaultdict(lambda: 0)
    for digits in data.values():
        for digit in digits:
            seen[digit] += 1

    ret: int = 1
    for index, digits in data.items():

        one_count: int = 0
        for digit in digits:
            if seen[digit] == 1:
                one_count += 1
        if one_count == 2:
            ret *= index
    return ret


def transpose(grid: list[str]) -> list[str]:
    return ["".join([grid[j][i] for j in range(len(grid))]) for i in range(len(grid[0]))]


def transpose_2d_list(grid: list[list[str]]) -> list[list[str]]:
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]


def rotate90(grid: list[str]) -> list[str]:
    return transpose(grid)[::-1]


def reflect_vertical(grid: list[str]) -> list[str]:
    return transpose(transpose(grid)[::-1])


def generate_rotations(grid: list[str]) -> list[list[str]]:
    ret: list[list[str]] = []
    for reflect in [False, True]:
        for rotations in range(4):
            tmp_image = grid.copy()
            for _ in range(rotations):
                tmp_image = rotate90(tmp_image)

            if reflect:
                tmp_image = reflect_vertical(tmp_image)
            ret.append(tmp_image)
    return ret


def main_part_2(inp: list[str]) -> OUTPUT_TYPE:
    data: dict[int, tuple[int, int, int, int]]
    data, tiles = parse_inp(inp)
    side_length: int = int(len(data) ** 0.5)

    seen: defaultdict = defaultdict(lambda: 0)
    for digits in data.values():
        for digit in digits:
            seen[digit] += 1

    del digit, digits

    initial_corners: int = -1
    corner_state: int = -1
    required: list[int] = []

    for tile_id, digits in data.items():
        one_count: int = 0
        state: int = 0
        for index, digit in enumerate(digits):
            if seen[digit] == 1:
                one_count += 1
                state += index ** 2

        if one_count == 2 and initial_corners == -1:
            corner_state = {1: 0, 5: 3, 13: 2, 9: 1}[state]
            initial_corners = tile_id
            continue

        required.append(tile_id)

    del tile_id, digits, one_count, state, index, digit

    top_tile = tiles[initial_corners]
    for i in range(corner_state):
        top_tile = rotate90(top_tile)

    grid_map: list[list[list[str]]] = [
        [[""] for _ in range(side_length)]
        for _ in range(side_length)
    ]
    grid_map[0][0] = top_tile

    for total in range(2 * side_length):
        for diff in range(total + 1):
            row: int = total - diff
            col: int = diff

            if row >= side_length or col >= side_length:
                continue

            # down
            if row + 1 < side_length:
                for state in required:
                    complete: bool = False
                    state_grid: list[str] = tiles[state]
                    for grid in generate_rotations(state_grid):
                        if grid_map[row][col][-1] == grid[0]:
                            complete = True
                            grid_map[row + 1][col] = grid

                    if complete:
                        required.remove(state)
                        break

            # left
            if col + 1 < side_length:
                for state in required:
                    complete = False
                    state_grid = tiles[state]
                    for grid in generate_rotations(state_grid):
                        if transpose(grid_map[row][col])[-1] == transpose(grid)[0]:
                            complete = True
                            grid_map[row][col + 1] = grid

                    if complete:
                        required.remove(state)
                        break

    for row_index, row in enumerate(grid_map):
        for col_index, col in enumerate(row):
            grid_map[row_index][col_index] = grid_map[row_index][col_index][1:-1]
            for inner_row_index in range(len(grid_map[row_index][col_index])):
                grid_map[row_index][col_index][inner_row_index] = grid_map[row_index][col_index][inner_row_index][1:-1]

    real_image: list[str] = []
    for row in grid_map:
        row_transpose: list[list[str]] = transpose_2d_list(row)
        for i in range(len(row_transpose)):
            row_image: str = ""
            for real_row in row_transpose[i]:
                row_image += real_row
            real_image.append(row_image)

    real_copies: list[set[tuple[int, int]]] = []
    for reflect in [False, True]:
        for rotations in range(4):
            tmp_image = real_image.copy()
            for _ in range(rotations):
                tmp_image = rotate90(tmp_image)

            if reflect:
                tmp_image = reflect_vertical(tmp_image)

            points: set[tuple[int, int]] = set()
            for y, row in enumerate(tmp_image):
                for x, char in enumerate(row):
                    if char == "#":
                        points.add((x, y))

            real_copies.append(points)

    monsters: int = 0
    for copy in real_copies:
        for x, y in copy:
            if (x, y) == (2, 3):
                pass
            points: set(tuple[int, int]) = {
                (x, y),
                (x + 1, y + 1),
                (x + 4, y + 1),
                (x + 5, y),
                (x + 6, y),
                (x + 7, y + 1),
                (x + 10, y + 1),
                (x + 11, y),
                (x + 12, y),
                (x + 13, y + 1),
                (x + 16, y + 1),
                (x + 17, y),
                (x + 18, y - 1),
                (x + 18, y),
                (x + 19, y)
            }
            p = points.intersection(copy)
            if points.intersection(copy) == points:
                monsters += 1
    return len(real_copies[0]) - 15 * monsters


def main() -> None:
    test_input: str = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""
    test_input_parsed: list[str] = test_input.splitlines(True)
    test_output_part_1_expected: OUTPUT_TYPE = 20899048083289
    test_output_part_2_expected: OUTPUT_TYPE = 273

    file_location: str = "python/Advent of Code/2020/Day 20/input.txt"
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
