from math import prod


def main():
    part_2()


def part_1():
    with open("./inputs/day_6.txt") as file:
        data = [
            [int(s.strip()) for s in line.split(" ") if s.strip()]
            for line in file.readlines()[:-1]
        ]
        file.seek(0)

        operators = [s.strip() for s in file.readlines()[-1].split(" ") if s.strip()]
    transposed_data_tuples = zip(*data)
    columns = [list(row) for row in transposed_data_tuples]

    total = 0

    for operator, column in zip(operators, columns):
        match operator:
            case "+":
                total += sum(column)
            case "*":
                total += prod(column)
    print(total)


def part_2():
    with open("./inputs/day_6_test.txt") as file:
        data = [
            [s.strip() for s in line.split(" ") if s.strip()]
            for line in file.readlines()[:-1]
        ]
        file.seek(0)

        operators = [s.strip() for s in file.readlines()[-1].split(" ") if s.strip()]
    transposed_data_tuples = zip(*data)
    columns = [list(row) for row in transposed_data_tuples]

    zeroed_columns = []
    for column in columns:
        # Find max len of string
        max_len = 0
        for string in column:
            if len(string) > max_len:
                max_len = len(string)
        zeroed_column = []
        for string in column:
            num_of_zeros = max_len - len(string)
            zeroed_column.append("0" * num_of_zeros + string)
        zeroed_columns.append(zeroed_column)

    print(zeroed_columns)

    horizontal_column_list = []
    for column in zeroed_columns:
        horizontal_column = []
        for i in range(len(column[0])):
            number = 0
            for index, string in enumerate(column):
                number += int(string[i]) * 10 ** (index)
            horizontal_column.append(number)
        horizontal_column_list.append(horizontal_column)

    print(horizontal_column_list)


if __name__ == "__main__":
    main()
