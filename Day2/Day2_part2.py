from functools import reduce

colors = ["red", "green", "blue"]


def get_power_of_set(pulls):
    min_color_values = {key: 0 for key in colors}

    for pull in pulls:
        for individual_cubs in pull.split(","):
            value_color = individual_cubs.split()

            min_color_values[value_color[1]] = max(min_color_values[value_color[1]], int(value_color[0]))

    return reduce(lambda x, y: x * y, min_color_values.values())


def get_sum_of_game_ids(path):
    with open(path, "r") as file:
        return sum(get_power_of_set(line.strip().split(":")[1].split(";")) for line in file.readlines())


if __name__ == '__main__':
    print(get_sum_of_game_ids("Day2_input.txt"))
