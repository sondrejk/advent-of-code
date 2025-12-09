from pathlib import Path
from tabulate import tabulate


def main():
    part_2()


def part_1():
    headers = ["bank", "joltage"]
    table = []
    input_file = Path("./inputs/day_3.txt")
    with open(input_file, "r") as file:
        banks = file.readlines()

    joltages = []
    for bank in banks:
        max_ten, index = find_max(bank.strip()[0:-1], 0, len(bank))
        max_one, _ = find_max(bank.strip()[index + 1 :], 0, len(bank))
        joltage = int(str(max_ten) + str(max_one))
        joltages.append(joltage)
        table.append([bank, joltage])
    print(tabulate(table, headers=headers))
    print(sum(joltages))


def part_2():
    headers = ["bank", "joltage"]
    table = []
    input_file = Path("./inputs/day_3.txt")
    with open(input_file, "r") as file:
        banks = file.readlines()

    joltages = []
    for bank in banks:
        bank = bank.strip()
        joltage_str = ""
        last_index = 0
        for i in range(12):
            digit, index = find_max(bank, last_index, len(bank) - 11 + i)
            last_index = index + 1
            joltage_str += str(digit)
        joltages.append(int(joltage_str))
        table.append([bank, int(joltage_str)])
    print(tabulate(table, headers=headers))
    print(sum(joltages))


def find_max(number: str, p, r) -> int:
    max_val = int(number[p])
    index = p
    for i, n in enumerate(number[p:r]):
        if int(n) > max_val:
            max_val = int(n)
            index = int(i) + p
    return max_val, index


if __name__ == "__main__":
    main()
