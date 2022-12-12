from string import ascii_lowercase
from heapq import heappush, heappop

with open("input.txt") as file:
    lines = file.read().strip().split()
    grid = [list(line) for line in lines]
    a = len(grid)
    b = len(grid[0])

    for i in range(a):
        for j in range(b):
            char = grid[i][j]
            if char == "S":
                start = i, j
            elif char == "E":
                end = i, j

    def elevation(s):
        if s in ascii_lowercase:
            return ascii_lowercase.index(s)
        if s == "E":
            return 25
        if s == "S":
            return 0

    def neighbours(i, j):
        for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            new_i = i+x
            new_j = j+y
            if not (0 <= new_i < a and 0 <= new_j < b):
                continue
            if elevation(grid[new_i][new_j]) >= elevation(grid[i][j])-1:
                yield new_i, new_j

    visited = [[False] * b for _ in range(a)]
    heap = [(0, end[0], end[1])]
    while True:
        steps, i, j = heappop(heap)
        if visited[i][j]:
            continue
        visited[i][j] = True
        if elevation(grid[i][j]) == 0:
            break
        for neighbour_i, neighbour_j in neighbours(i, j):
            heappush(heap, (steps+1, neighbour_i, neighbour_j))
    print(heap)
