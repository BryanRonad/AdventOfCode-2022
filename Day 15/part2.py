import re

pattern = re.compile(r"-?\d+")

lines = [list(map(int, pattern.findall(line))) for line in open("input.txt")]

ROW = 4000000

for Y in range(ROW + 1):
    if(Y % 10000 == 0):
        print(Y)
    intervals = list()
    row = Y
    for line in lines:
        sx, sy, bx, by = line
        d = abs(sx - bx) + abs(sy - by)
        offset = d - abs(sy - row)

        # Checking if ROW is too far from diamond center
        if offset < 0:
            continue

        # Appending interval to intervals
        intervals.append((sx - offset, sx + offset))

    # Merging intervals
    q = list()
    # Sorting intervals
    intervals.sort()
    for interval in intervals:
        l, h = interval
        if not q:
            q.append([l, h])
            continue
        pl, ph = q[-1]
        if l > ph + 1:
            q.append([l, h])
            continue
        q[-1][1] = max(h, ph)

    if len(q) > 1:
        print((q[0][1]+1)*4000000+row)
        break
