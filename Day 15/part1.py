import re

pattern = re.compile(r"-?\d+")

lines = [list(map(int, pattern.findall(line))) for line in open("input.txt")]

ROW = 10
intervals = list()
row_beacons = set()

for line in lines:
    sx, sy, bx, by = line
    d = abs(sx - bx) + abs(sy - by)
    offset = d - abs(sy - ROW)

    # Checking if ROW is too far from diamond center
    if offset < 0:
        continue

    # Appending interval to intervals
    intervals.append((sx - offset, sx + offset))

    # Appending beacons of ROW to known set
    if by == ROW:
        row_beacons.add(bx)

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

# Counting the number of impossible points
impossible = set()
for l, h in q:
    for i in range(l, h + 1):
        impossible.add(i)

print(len(impossible-row_beacons))
