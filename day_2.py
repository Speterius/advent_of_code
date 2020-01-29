from common import read_input_lines


def int_program(code, i=0):
    opcode = code[i]

    if opcode == 1:
        code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]]
        int_program(code, i=i+4)
    elif opcode == 2:
        code[code[i + 3]] = code[code[i + 1]] * code[code[i + 2]]
        int_program(code, i=i+4)
    elif opcode == 99:
        return code


def main():
    # Read the data:
    intcode = []
    for line, _ in read_input_lines(file_name='day_2.txt'):
        intcode = line.split(",")
    intcode = [int(i) for i in intcode]
    intcode_original = tuple(intcode)

    # Part 1: what is the result of 12, 2
    intcode[1] = 12
    intcode[2] = 2
    int_program(intcode)
    print('Part 1:', intcode[0])

    # Part 2: what input gives 19690720?
    solution = 0
    for noun in range(99):
        for verb in range(99):
            intcode = list(intcode_original)
            intcode[1] = noun
            intcode[2] = verb

            int_program(intcode)
            result = intcode[0]

            if result == 19690720:
                solution = (noun*100+verb)

    print('Part 2: ', solution)


if __name__ == '__main__':
    main()
