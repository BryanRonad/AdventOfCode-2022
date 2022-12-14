from functools import cmp_to_key
import math


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
    packets = file.read().replace("\n\n", "\n").split("\n")
    packets = list(map(eval, packets))
    packets.append([[6]])
    packets.append([[2]])
    validity = []
    sorted_with_key = sorted(packets, key=cmp_to_key(compare_lists))
    print("Part 2:",
          math.prod([index+1 for index, divider in enumerate(sorted_with_key) if divider in [[[6]], [[2]]]]))
