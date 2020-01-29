from common import read_input_lines
import numpy as np


class Wire:
    unit_vectors = {'R': [1, 0], 'U': [0, 1], 'L': [-1, 0], 'D': [0, -1]}

    def __init__(self, instructions):
        position = np.array([0, 0])
        self.points = [position]

        for instruction in instructions:
            letter = instruction[0]
            steps = int(instruction[1:])
            direction = np.array(self.unit_vectors[letter])

            for i in range(steps):
                position = position + direction
                self.points.append(position)

        self.points = np.array(self.points)
        self.unique_points = set([tuple(P) for P in self.points])
        self.unique_points.remove((0, 0))

    def intersections(self, B):
        return self.unique_points.intersection(B.unique_points)


def main():

    wire_data = []
    for line, y in read_input_lines('day_3.txt'):
        wire_data.append(line.split(','))

    wire_1 = Wire(instructions=wire_data[0])
    wire_2 = Wire(instructions=wire_data[1])

    intersections = wire_1.intersections(wire_2)
    distances = [abs(t[0]) + abs(t[1]) for t in intersections]

    print('Part 1:', min(distances))


if __name__ == "__main__":
    main()

