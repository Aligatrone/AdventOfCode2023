def get_scratchcard_value(scratchcard):
    return int(pow(2, len(list(filter(lambda x: x in scratchcard.split("|")[0].split(), scratchcard.split("|")[1].split()))) - 1))


def get_sum_of_scratchcards(path):
    with open(path, "r") as file:
        return sum(get_scratchcard_value(line.strip().split(":")[1]) for line in file.readlines())


if __name__ == '__main__':
    print(get_sum_of_scratchcards("Day4_input.txt"))
