res = list()
with open("input.txt") as file:
    input = [[x for x in y.split(",")]
             for y in file.read().split("\n")]
    for line in input:
        first = set(range(int(line[0].split('-')[0]),
                    int(line[0].split("-")[1])+1))
        second = set(
            range(int(line[1].split('-')[0]), int(line[1].split("-")[1])+1))
        res.append(first.issubset(second) or second.issubset(first))
    print(sum(res))
