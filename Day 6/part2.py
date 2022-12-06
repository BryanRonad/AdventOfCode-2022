with open("input.txt") as file:
    input = list(file.read())
    for i in range(14, len(input)):
        if len(set(input[i-14:i])) == len(input[i-14:i]):
            print(i)
            break
