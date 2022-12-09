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
    T = O.copy()
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
            # Move T according to the relative positions
            dist = math.dist(H, T)
            m = slope(*T, *H)
            if(dist > 1.5):
                if(m == 0):
                    if T[0] < H[0]:
                        T[0] += 1
                    elif T[0] > H[0]:
                        T[0] -= 1
                    elif T[1] < H[1]:
                        T[1] += 1
                    elif T[1] > H[1]:
                        T[1] -= 1
                elif(m > 0):
                    if T[1] < H[1]:
                        T = [x+1 for x in T]
                    elif T[1] > H[1]:
                        if T[0] > H[0]:
                            T[0] -= 1
                        elif T[0] < H[0]:
                            T[0] += 1
                        T[1] -= 1
                elif(m < 0):
                    if T[1] < H[1]:
                        T[0] -= 1
                        T[1] += 1
                    elif T[1] > H[1]:
                        if T[0] > H[0]:
                            T[0] -= 1
                        elif T[0] < H[0]:
                            T[0] += 1
                        T[1] -= 1
            res.append(tuple(T))
    print(len(set(res)))
