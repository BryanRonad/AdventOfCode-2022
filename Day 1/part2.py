with open("input.txt") as f:
    input = sorted(sum(int(y) for y in x.split("\n"))
                   for x in f.read().split("\n\n"))
print(sum(input[-3:]))
