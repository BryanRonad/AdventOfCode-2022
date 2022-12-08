with open("input.txt") as file:
    visible = []
    file_input = [[int(y) for y in list(x)] for x in file.read().split("\n")]
    for row_index, row in enumerate(file_input):
        if(row_index in [0, len(file_input)-1]):
            continue
        for col_index, height in enumerate(row):
            if(col_index in [0, len(row)-1]):
                visible.append(tuple([row_index, col_index]))
                continue
            if(any([all(ele < height for ele in row[:col_index]),
                    all(ele < height for ele in row[col_index+1:]),
                    all(ele < height for ele in [x[col_index]
                        for x in file_input][:row_index]),
                    all(ele < height for ele in [x[col_index]
                        for x in file_input][row_index+1:])])):
                visible.append(tuple([row_index, col_index]))
    print("Part 1:", sum(
        [len(file_input[0]), len(file_input[-1]), len(visible)]))
