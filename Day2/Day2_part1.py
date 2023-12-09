max_values = {"red": 12, "green": 13, "blue": 14}


def check_valid_game(pulls):
    for pull in pulls:
        for individual_cubs in pull.split(","):
            value_color = individual_cubs.split()

            if max_values[value_color[1]] < int(value_color[0]):
                return False

    return True


def get_sum_of_game_ids(path):
    list_of_invalid_games = set()

    with open(path, "r") as file:
        for index, line in enumerate(file.readlines()):
            if not check_valid_game(line.strip().split(":")[1].split(";")):
                list_of_invalid_games.add(index + 1)

    return sum(filter(lambda x: x not in list_of_invalid_games, [value for value in range(1, 101)]))


if __name__ == '__main__':
    print(get_sum_of_game_ids("Day2_input.txt"))
