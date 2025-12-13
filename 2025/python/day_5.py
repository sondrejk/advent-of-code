def main():
    part_2()


def part_1():
    ranges = []
    with open("./inputs/day_5.txt") as file:
        line = file.readline().strip()
        while line != "":
            ranges.append(line)
            line = file.readline().strip()
        ids = [int(line.strip()) for line in file.readlines()]

    ranges = [[int(line.split("-")[0]), int(line.split("-")[1])] for line in ranges]

    fresh_count = 0

    for id in ids:
        for range in ranges:
            if id >= range[0] and id <= range[1]:
                fresh_count += 1
                break

    print(fresh_count)


def part_2():
    ranges = []
    with open("./inputs/day_5.txt") as file:
        line = file.readline().strip()
        while line != "":
            ranges.append(line)
            line = file.readline().strip()

    ranges = [[int(line.split("-")[0]), int(line.split("-")[1])] for line in ranges]
    ranges.sort(key=lambda x: x[0])

    sum = 0
    highest = 0
    for range in ranges:
        sum += max(range[1] - max(range[0], highest + 1) + 1, 0)
        highest = max(highest, range[1])
    print(sum)


if __name__ == "__main__":
    main()
