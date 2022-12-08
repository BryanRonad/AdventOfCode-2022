import math


def takewhile(predicate, iterable):
    for x in iterable:
        if predicate(x):
            yield x
        else:
            yield x
            break


with open("input.txt") as file:
    scores = []
    file_input = [[int(y) for y in list(x)] for x in file.read().split("\n")]
    for row_index, row in enumerate(file_input):
        if(row_index in [0, len(file_input)-1]):
            continue
        for col_index, height in enumerate(row):
            if(col_index in [0, len(row)-1]):
                continue
            scores.append(math.prod([len(list(takewhile(lambda ele: ele <
                                                        height, reversed(row[:col_index])))),
                                     len(list(takewhile(lambda ele: ele <
                                                        height, row[col_index+1:]))),
                                     len(list(takewhile(lambda ele: ele <
                                                        height, reversed([x[col_index]
                                                                          for x in file_input][:row_index])))),
                                     len(list(takewhile(lambda ele: ele <
                                                        height, [x[col_index]
                                                                 for x in file_input][row_index+1:])))]))
    print("Part 2:", max(scores))
