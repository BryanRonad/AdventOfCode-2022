with open("input.txt") as file:
    file_input = [x.split(' ') for x in file.read().split("\n")]
    score_arr = list()
    check = 20
    cycle = 0
    x = 1
    for line in file_input:
        if(line[0] == "noop"):
            cycle += 1
        if(line[0] == "addx"):
            cycle += 2
        if(cycle >= check):
            score_arr.append(check * x)
            check += 40
        if(line[0] == "addx"):
            x += int(line[1])
    print(sum(score_arr))
