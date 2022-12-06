with open("input.txt") as file:
    input = list(file.read())
    for i in range(len(input)):
        if i < 15:
            continue
        if len(set(input[i-14:i])) == len(input[i-14:i]):
            print(i)
            break
