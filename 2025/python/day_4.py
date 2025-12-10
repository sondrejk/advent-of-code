from pathlib import Path


def main():
    part_2()


def part_1():
    input_file = Path("./inputs/day_4.txt")
    with open(input_file) as file:
        data = [line.strip() for line in file.readlines()]

    count = 0

    for line, string in enumerate(data):
        for index, char in enumerate(string):
            if char == "@":
                rolls = 0
                adjacents = []

                if line > 0:
                    if index > 0:
                        adjacents.append(data[line - 1][index - 1])
                    adjacents.append(data[line - 1][index])
                    if index < len(string) - 1:
                        adjacents.append(data[line - 1][index + 1])

                if index > 0:
                    adjacents.append(data[line][index - 1])
                if index < len(string) - 1:
                    adjacents.append(data[line][index + 1])

                if line < len(data) - 1:
                    if index > 0:
                        adjacents.append(data[line + 1][index - 1])
                    adjacents.append(data[line + 1][index])
                    if index < len(string) - 1:
                        adjacents.append(data[line + 1][index + 1])

                for adjacent in adjacents:
                    if adjacent == "@":
                        rolls += 1
                if rolls < 4:
                    count += 1
                print(adjacents, count)
    print(count)


def part_2():
    input_file = Path("./inputs/day_4.txt")
    with open(input_file) as file:
        data = [line.strip() for line in file.readlines()]
    run_count = 1
    total_count = 0

    while run_count != 0:
        new_data = []
        run_count = 0
        for line, string in enumerate(data):
            new_string = []
            for index, char in enumerate(string):
                if char == ".":
                    new_string.append(".")
                else:
                    rolls = 0
                    adjacents = []

                    if line > 0:
                        if index > 0:
                            adjacents.append(data[line - 1][index - 1])
                        adjacents.append(data[line - 1][index])
                        if index < len(string) - 1:
                            adjacents.append(data[line - 1][index + 1])

                    if index > 0:
                        adjacents.append(data[line][index - 1])
                    if index < len(string) - 1:
                        adjacents.append(data[line][index + 1])

                    if line < len(data) - 1:
                        if index > 0:
                            adjacents.append(data[line + 1][index - 1])
                        adjacents.append(data[line + 1][index])
                        if index < len(string) - 1:
                            adjacents.append(data[line + 1][index + 1])

                    for adjacent in adjacents:
                        if adjacent == "@":
                            rolls += 1
                    if rolls < 4:
                        run_count += 1
                        new_string.append(".")
                    else:
                        new_string.append("@")
            new_data.append(new_string)
        total_count += run_count
        data = new_data
    print(total_count)


if __name__ == "__main__":
    main()
