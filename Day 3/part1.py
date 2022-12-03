sum = 0
with open("input.txt") as file:
    for line in file.read().split("\n"):
        common = list(
            set(line[:len(line)//2]).intersection(line[len(line)//2:]))[0]
        priority = ord(common)-96 if common.islower() else ord(common)-38
        sum += priority
print(sum)
