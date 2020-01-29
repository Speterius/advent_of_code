from common import timer, read_input_lines
import numpy as np
import math
import warnings
warnings.filterwarnings("ignore")


@timer
def best_location(asteroid_field: np.ndarray) -> (np.ndarray, int):

    # Make a square matrix the repeated asteroid_field vector:
    repeated_field = np.repeat(asteroid_field[:, :, np.newaxis], asteroid_field.shape[0], axis=2)

    # Shift the coordinates of each row by the asteroid:
    relative_field = repeated_field - repeated_field.T

    # Calculate the reduced (divided by GCD) relative vector for each position:
    reduced_field = np.zeros(relative_field.shape)
    for i, row in enumerate(relative_field):
        for j, coord in enumerate((row[:, i:]).T):
            c = coord // math.gcd(*coord)           # Let numpy take care of div 0 exceptions. We don't have time.
            reduced_field[i, :, i + j] = c
            reduced_field[i + j, :, i] = -c         # The matrix is symmetric, but one half is negative.
    reduced_field = reduced_field.astype(int)

    # Count the unique vectors in each row:
    unique_count = np.zeros(shape=asteroid_field.shape[0], dtype=int)
    for i in range(reduced_field.shape[0]):
        row = [tuple(c) for c in reduced_field[i, :, :].T]
        unique_count[i] = len(list(set(row))) - 1               # -1 because of (0, 0)

    # Best asteroid:
    best_idx = np.argmax(unique_count)
    max_count = unique_count[best_idx]

    return asteroid_field[best_idx], max_count


def main():
    # Part 1:
    input_file = 'day_10_part_1.txt'
    asteroid_coordinates = []
    for line, y in read_input_lines(input_file):
        asteroid_coordinates += [[x, y] for x, char in enumerate(line) if char == "#"]
    asteroid_coordinates = np.array(asteroid_coordinates)

    station_coordinates, n_detectable_asteroids = best_location(asteroid_coordinates)
    print('='*10+'  PART 1  '+'='*10)
    print(f'Best station is at: {station_coordinates} and can see {n_detectable_asteroids} asteroids.')

    # Part 2:
    # (...)


if __name__ == '__main__':
    main()
