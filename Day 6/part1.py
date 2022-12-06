with open("input.txt") as file:
    input = list(file.read())
    for i in range(4, len(input)):
        if len(set(input[i-4:i])) == len(input[i-4:i]):
            print(i)
            break
