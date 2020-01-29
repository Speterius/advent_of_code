from common import read_input_lines
import numpy as np


def fuel_required(mass: int) -> int:
    return mass // 3 - 2


def total_fuel(mass: int) -> int:
    total = 0
    fuel_req = fuel_required(mass)
    while fuel_req > 0:
        total += fuel_req
        fuel_req = fuel_required(fuel_req)
    return total


def main():
    # Read the data:
    data = []
    for line, _ in read_input_lines(file_name='day_01_part_1.txt'):
        data.append(int(line))
    data = np.array(data)

    # Part 1:
    fuel_sum = sum([fuel_required(m) for m in data])
    print('Part 1:', fuel_sum)

    # Part 2:
    fuel_sum = sum([total_fuel(m) for m in data])
    print('Part 2:',fuel_sum)


if __name__ == '__main__':
    main()
