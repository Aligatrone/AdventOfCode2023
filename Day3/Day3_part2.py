import re
from functools import reduce


def get_sum_of_content(content):
    numbers_positions = []
    gears_positions = []

    for index_i, line in enumerate(content):
        numbers_positions.extend([(value.group(), (index_i, value.start())) for value in re.finditer(r"\d+", line)])
        gears_positions.extend([(index_i, value.start()) for value in re.finditer(r"\*", line)])

    dict_gears = {key: [] for key in gears_positions}

    for number in numbers_positions:
        number_perimeter = [(i, j) for i in range(number[1][0] - 1, number[1][0] + 2) for j in range(number[1][1] - 1, number[1][1] + 1 + len(number[0]))]

        for number_adjacent in number_perimeter:
            if number_adjacent in gears_positions:
                dict_gears[number_adjacent].append(int(number[0]))

    return sum(reduce(lambda x, y: x * y, item) for item in filter(lambda x: len(x) == 2, dict_gears.values()))


def get_sum_of_number_parts(path):
    content = []

    with open(path, "r") as file:
        for line in file.readlines():
            content.append(line.strip())

        return get_sum_of_content(content)


if __name__ == '__main__':
    print(get_sum_of_number_parts("Day3_input.txt"))
