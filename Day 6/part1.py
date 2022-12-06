with open("input.txt") as file:
    input = list(file.read())
    for i in range(len(input)):
        if i < 5:
            continue
        if len(set(input[i-4:i])) == len(input[i-4:i]):
            print(i)
            break
