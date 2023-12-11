import re


def get_sum_of_content(content):
    numbers_positions = []
    parts_positions = []

    for index_i, line in enumerate(content):
        numbers_positions.extend([(value.group(), (index_i, value.start())) for value in re.finditer(r"\d+", line)])
        parts_positions.extend([(index_i, value.start()) for value in re.finditer(r"[^0-9.]", line)])

    sum_of_numbers = list(filter(lambda x: bool(set(parts_positions) & set([(i, j) for i in range(x[1][0] - 1, x[1][0] + 2) for j in range(x[1][1] - 1, x[1][1] + 1 + len(x[0]))])), numbers_positions))

    return sum(int(value[0]) for value in sum_of_numbers)


def get_sum_of_number_parts(path):
    content = []

    with open(path, "r") as file:
        for line in file.readlines():
            content.append(line.strip())

        return get_sum_of_content(content)


if __name__ == '__main__':
    print(get_sum_of_number_parts("Day3_input.txt"))
