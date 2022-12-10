with open("input.txt") as file:
    file_input = [x.split(' ') for x in file.read().split("\n")]
    start = 0
    hashmap = dict()
    check = 20
    cycle = 0
    x = 1
    offset = 1
    for line in file_input:
        if(line[0] == "noop"):
            cycle += 1
            hashmap[cycle] = x
        if(line[0] == "addx"):
            cycle += 2
            for i in range(start+1, cycle+1):
                hashmap[i] = x
            x += int(line[1])
        start = cycle
    for k, v in hashmap.items():
        hashmap[k] = "#" if k-offset in [v-1, v, v+1] else "."
        if(k in range(40, 240, 40)):
            offset += 40
    print('\n'.join([''.join(x) for x in
          [list(hashmap.values())[i:i + 40]
           for i in range(0, len(hashmap.values()), 40)]]))
