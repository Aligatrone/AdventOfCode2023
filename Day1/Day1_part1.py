digits = [str(value) for value in range(1, 10)]


def get_first_digit(line, ascending=True):
    list_of_tuples = [(value, line.find(value) if ascending else line.rfind(value)) for value in digits]

    return min(filter(lambda x: x[1] >= 0, list_of_tuples), key=lambda x: x[1])[0] if ascending else max(list_of_tuples, key=lambda x: x[1])[0]


def get_sum_of_coordinates(path):
    with open(path, 'r') as file:
        return sum([int(get_first_digit(line) + get_first_digit(line, False)) for line in file.readlines()])


if __name__ == '__main__':
    print(get_sum_of_coordinates("Day1_input.txt"))
