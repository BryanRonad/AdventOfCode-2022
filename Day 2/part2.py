score_dict = {
    "A": 1,
    "B": 2,
    "C": 3
}

fight_dict = {
    "A": "B",
    "B": "C",
    "C": "A"
}

with open("input.txt") as file:
    input = file.read().split("\n")
    score = 0
    for line in input:
        them, result = line.split(" ")
        if(result == "Y"):
            me = them
            score += (3+score_dict[me])
            continue
        if(result == "X"):
            me = {v: k for k, v in fight_dict.items()}[them]
            score += score_dict[me]
            continue
        me = fight_dict[them]
        score += (6+score_dict[me])

    print(score)
