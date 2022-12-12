import re
import operator
from collections import defaultdict
import math

ops = {"+": operator.add, "-": operator.sub,
       "*": operator.mul, "/": operator.truediv, "divisible": operator.mod}
M_items = defaultdict(list)
M_operations = defaultdict(list)
M_test = defaultdict(list)
M_true = defaultdict(list)
M_false = defaultdict(list)
M_inspections = defaultdict(int)
big_mod = 1

with open("input.txt") as file:
    input = [x.split('\n') for x in file.read().split("\n\n")]
    for sub_round in input:
        monkey = int(sub_round[0].split(" ")[1][0])
        items = list(
            map(int, re.search(r"\: (.*)", sub_round[1]).group(1).split(", ")))
        operation = re.search(r"\= (.*)", sub_round[2]).group(1).split(" ")
        operation = [int(x) if x.isnumeric() else ops[x]
                     if x in ops.keys() else x for x in operation]
        test = re.search(r"\: (.*)", sub_round[3]).group(1).split(" ")
        M_items[monkey] = items.copy()
        M_operations[monkey] = operation.copy()
        M_test[monkey] = test.copy()
        M_true[monkey] = sub_round[4].split(" ")[-1]
        M_false[monkey] = sub_round[5].split(" ")[-1]
        big_mod *= int(test[-1])

    for i in range(10000):
        for monkey_index in range(len(M_items)):
            for item in M_items[monkey_index].copy():
                M_inspections[monkey_index] += 1
                item_operation = [
                    int(item) if x == "old" else x for x in M_operations[monkey_index]]
                result = item_operation[1](
                    item_operation[0], item_operation[2])
                result %= big_mod
                if(ops[M_test[monkey_index][0]](result, int(M_test[monkey_index][-1])) == 0):
                    thrown_monkey = int(M_true[monkey_index].split(" ")[-1])
                    M_items[thrown_monkey].append(result)
                else:
                    thrown_monkey = int(M_false[monkey_index].split(" ")[-1])
                    M_items[thrown_monkey].append(result)
                M_items[monkey_index].remove(item)
    print(math.prod(sorted(M_inspections.values())[-2:]))
