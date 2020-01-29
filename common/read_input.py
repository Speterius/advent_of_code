def read_input_lines(file_name):
    input_path = 'inputs/'+file_name

    with open(input_path) as f:
        for y, line in enumerate(f):
            yield line, y
