from pathlib import Path


def main():
    part_2()


def part_1():
    input_file = Path("./inputs/day_1.txt")
    with open(input_file, "r") as file:
        data = file.readline().split(",")

    invalid_ids = []

    for number_range in data:
        bounds = number_range.split("-")
        low_bount = int(bounds[0])
        high_bound = int(bounds[1])

        for i in range(low_bount, high_bound + 1):
            number_of_digits = len(str(i))
            # Only numbers with an even number of digits can consist of two repeating numbers
            if number_of_digits % 2 == 0:
                half_mark = int(number_of_digits / 2)
                left_half = str(i)[0:half_mark]
                right_half = str(i)[half_mark:]

                if left_half == right_half:
                    invalid_ids.append(i)

    print(sum(invalid_ids))


def part_2():
    input_file = Path("./inputs/day_2.txt")
    with open(input_file, "r") as file:
        data = file.readline().split(",")

    invalid_ids = []

    for number_range in data:
        bounds = number_range.split("-")
        low_bount = int(bounds[0])
        high_bound = int(bounds[1])

        for i in range(low_bount, high_bound + 1):
            number_of_digits = len(str(i))
            half_mark = int(number_of_digits / 2 + 1)
            for j in range(half_mark):
                # Checks if the length of a substring multiplied by its count is equal to the number of digits (Its a repeating sequence)
                if str(i).count(str(i)[0:j]) * j == number_of_digits:
                    invalid_ids.append(i)
                    break

    print(invalid_ids)
    print(sum(invalid_ids))


if __name__ == "__main__":
    main()
