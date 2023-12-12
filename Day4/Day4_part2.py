scratchcards_dict = {}


def get_scratchcard_value(scratchcard):
    return 0 if int(scratchcard[1]) == 0 else sum(1 + get_scratchcard_value((str(index), scratchcards_dict[str(index)])) for index in range(1 + int(scratchcard[0]), scratchcard[1] + 1 + int(scratchcard[0])))


def get_sum_of_scratchcards(path):
    global scratchcards_dict

    with open(path, "r") as file:
        scratchcards_dict = {line.split(":")[0].split()[1]: len(list(filter(lambda x: x in line.split(":")[1].split("|")[0].split(), line.split(":")[1].split("|")[1].split()))) for line in file.readlines()}

    return sum(1 + get_scratchcard_value(scratchcard) for scratchcard in scratchcards_dict.items())


if __name__ == '__main__':
    print(get_sum_of_scratchcards("Day4_input.txt"))
