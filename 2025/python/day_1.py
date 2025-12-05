from pathlib import Path
from tabulate import tabulate



def main():
    input_file = Path("./inputs/day_1.txt")
    headers = ["current rotation", "rotation", "quotient", "remainder", "number of zeros"]
    table = []
    with open(input_file, "r") as file:
        data = file.readlines()
    
    lock_number = 50
    num_of_zeros = 0
    for line in data:
        direction = -1 if line[0] == "L" else 1
        amount = int(line[1:])

        q, r = divmod(lock_number + direction * amount, 100)
        if r == 0:
            num_of_zeros += 1
            if lock_number == 0:
                if direction == -1:
                    num_of_zeros += max(0, abs(q) - 2)
                else:
                    num_of_zeros += max(0, abs(q) - 1)
            else:
                if direction == -1:
                    num_of_zeros += abs(q)
                else:
                    num_of_zeros += max(0, abs(q) - 1)
        else:
            if lock_number == 0:
                if direction == -1:
                    num_of_zeros += max(0, abs(q) - 1)
                else:
                    num_of_zeros += abs(q)
            else:
                if direction == -1:
                    num_of_zeros += abs(q)
                else:
                    num_of_zeros += abs(q)
        table.append([lock_number, line, q, r, num_of_zeros])
        lock_number = r
    print(tabulate(table, headers=headers))
    print(num_of_zeros)

# Situasjon 1:
#   a0 != 0
#   rotasjon = <100
#   Løsning: Legger ikke til en null

# Situasjon 2:
#   a0 != 0
#   rotasjon = venstre til man når 0
#   Løsning: legge til 1 null fordi tallet er 0. Kvotienten er også 0

# Situasjon 3:
#   a0 != 0
#   rotasjon = høyre til man når 0
#   Løsning: legge til 1 null fordi man når 0. Kvotient blir 1

# Situasjon 4:
#   a0 = 0
#   rotasjon = mot venstre <100
#   Løsning: Ikke legge til 0, men kvotient er 1
if __name__ == "__main__":
    print(divmod(-100, 100))
    main()
