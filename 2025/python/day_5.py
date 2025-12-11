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

    fresh_ids: set = set()

    for rangee in ranges:
        print(rangee)
        fresh_ids.update(range(rangee[0], rangee[1] + 1))
    print(len(fresh_ids))


if __name__ == "__main__":
    main()
