sum = 0
with open("input.txt") as file:
    input = file.read().split("\n")
    for i in range(0, len(input)-2, 3):
        common = list(
            set(input[i]).intersection(input[i+1]).intersection(input[i+2]))[0]
        priority = ord(common)-96 if common.islower() else ord(common)-38
        sum += priority
print(sum)
