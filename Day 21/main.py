def parse_inp(inp: list[str]) -> tuple[list[tuple[set[str], set[str]]], set[str], set[str]]:
    ret: list[tuple[set[str], set[str]]] = []
    cont: set[str] = set()
    ing: set[str] = set()
    for line in inp:
        line = line.strip()

        contaminants: set[str] = {x for x in line.split(
            " (contains ")[1][:-1].split(", ")}
        ingredients: set[str] = {x for x in line.split(
            " (contains ")[0].split(" ")}
        ret.append((ingredients, contaminants))
        cont = cont.union(contaminants)
        ing = ing.union(ingredients)
    return ret, cont, ing


def main_part_1(inp: list[str]) -> int:
    recipes: list[tuple[set[str], set[str]]]
    contaminants: set[str]
    ingredients: set[str]
    recipes, contaminants, ingredients = parse_inp(inp)

    possible_comtaminants: dict[str, set[str]] = {
        contaminant: ingredients.copy() for contaminant in contaminants}

    for ing, cont in recipes:
        for single_contaminant in cont:
            possible_comtaminants[single_contaminant] = \
                possible_comtaminants[single_contaminant].intersection(ing)

    ing_contamin: set[str] = set()
    for contamin in possible_comtaminants.values():
        ing_contamin = ing_contamin.union(contamin)

    ing_safe: set[str] = ingredients.difference(ing_contamin)

    ret: int = 0
    for ing, _ in recipes:
        ret += len(ing_safe.intersection(ing))

    return ret


def main_part_2(inp: list[str]) -> str:
    recipes: list[tuple[set[str], set[str]]]
    contaminants: set[str]
    ingredients: set[str]
    recipes, contaminants, ingredients = parse_inp(inp)

    possible_comtaminants: dict[str, set[str]] = {
        contaminant: ingredients.copy() for contaminant in contaminants}

    for ing, cont in recipes:
        for single_contaminant in cont:
            possible_comtaminants[single_contaminant] = \
                possible_comtaminants[single_contaminant].intersection(ing)

    while max([len(x) for x in possible_comtaminants.values()]) > 1:
        for i in possible_comtaminants.values():
            if len(i) != 1:
                continue

            ingredient: str = i.copy().pop()
            for key in possible_comtaminants.keys():
                if len(possible_comtaminants[key]) == 1:
                    continue

                if ingredient not in possible_comtaminants[key]:
                    continue

                possible_comtaminants[key].remove(ingredient)

    ret: str = ""
    for cont_type in sorted(list(possible_comtaminants.keys())):
        ret += possible_comtaminants[cont_type].pop() + ","
    ret = ret[:-1]
    return ret


def main() -> None:
    test_input: str = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
    test_input_parsed: list[str] = test_input.split("\n")
    test_output_part_1_expected: int = 5
    test_output_part_2_expected: str = "mxmxvkd,sqjhc,fvjkl"

    file_location: str = "python/Advent of Code/2020/Day 21/input.txt"
    input_file: list[str] = open(file_location, "r").readlines()

    test_output_part_1: int = main_part_1(test_input_parsed)
    test_output_part_2: str = main_part_2(test_input_parsed)

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
