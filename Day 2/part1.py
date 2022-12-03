score_dict = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

equality_dict = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

fight_dict = {
    "X": "Y",
    "Y": "Z",
    "Z": "X"
}

with open("input.txt") as file:
    input = file.read().split("\n")
    score = 0
    for line in input:
        them, me = line.split(" ")
        them = equality_dict[them]
        if(them == me):
            score += (3+score_dict[me])
            continue
        if(me == fight_dict[them]):
            score += (6+score_dict[me])
            continue
        score += score_dict[me]
    print(score)
