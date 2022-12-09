import math


def slope(x1, y1, x2, y2):
    if(x2-x1 != 0):
        return (y2-y1)/(x2-x1)
    else:
        return 0


with open("input.txt") as file:
    file_input = [x.split(' ') for x in file.read().split("\n")]
    res = []
    O = list([0, 0])
    H = O.copy()
    rope_dict = {k: O.copy() for k in range(1, 10)}
    for direction, steps in file_input:
        for step in range(1, int(steps)+1):
            # Move H according to direction, stepwise
            if(direction == "R"):
                H[0] += 1
            elif(direction == "L"):
                H[0] -= 1
            elif(direction == "U"):
                H[1] += 1
            elif(direction == "D"):
                H[1] -= 1
            # Move rope_dict[k] according to the relative positions
            for k in rope_dict.keys():
                if(k == 1):
                    h = H
                else:
                    h = rope_dict[k-1]
                dist = math.dist(h, rope_dict[k])
                m = slope(*rope_dict[k], *h)
                if(dist > 1.5):
                    if(m == 0):
                        if rope_dict[k][0] < h[0]:
                            rope_dict[k][0] += 1
                        elif rope_dict[k][0] > h[0]:
                            rope_dict[k][0] -= 1
                        elif rope_dict[k][1] < h[1]:
                            rope_dict[k][1] += 1
                        elif rope_dict[k][1] > h[1]:
                            rope_dict[k][1] -= 1
                    elif(m > 0):
                        if rope_dict[k][1] < h[1]:
                            rope_dict[k] = [x+1 for x in rope_dict[k]]
                        elif rope_dict[k][1] > h[1]:
                            if rope_dict[k][0] > h[0]:
                                rope_dict[k][0] -= 1
                            elif rope_dict[k][0] < h[0]:
                                rope_dict[k][0] += 1
                            rope_dict[k][1] -= 1
                    elif(m < 0):
                        if rope_dict[k][1] < h[1]:
                            rope_dict[k][0] -= 1
                            rope_dict[k][1] += 1
                        elif rope_dict[k][1] > h[1]:
                            if rope_dict[k][0] > h[0]:
                                rope_dict[k][0] -= 1
                            elif rope_dict[k][0] < h[0]:
                                rope_dict[k][0] += 1
                            rope_dict[k][1] -= 1
            res.append(tuple(rope_dict[9]))
    print(len(set(res)))
