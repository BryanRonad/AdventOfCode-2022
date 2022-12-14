import ast


def compare_lists(item1, item2):
    if(isinstance(item1, int) and isinstance(item2, int)):
        if(item1 < item2):
            return -1
        if(item1 > item2):
            return 1
        return 0
    if(isinstance(item1, int) and isinstance(item2, list)):
        item1 = [item1]
    if(isinstance(item1, list) and isinstance(item2, int)):
        item2 = [item2]
    if(isinstance(item1, list) and isinstance(item2, list)):
        i = 0
        while(i < len(item1) and i < len(item2)):
            comparison = compare_lists(item1[i], item2[i])
            if(comparison == -1):
                return -1
            if(comparison == 1):
                return 1
            i += 1
        if(len(item1) < len(item2)):
            return -1
        if(len(item1) > len(item2)):
            return 1
        return 0


with open("input.txt") as file:
    packets = [pair.split("\n") for pair in file.read().split("\n\n")]
    validity = []
    for packet_index, packet in enumerate(packets):
        lp, rp = map(ast.literal_eval, packet)
        if(compare_lists(lp, rp) == -1):
            validity.append(packet_index + 1)
    print("Part 1:", sum(validity))
