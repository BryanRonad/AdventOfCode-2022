with open("input.txt") as file:
    stacks, steps = file.read().split("\n\n")
    stacks = [x for x in stacks.split("\n")]
    stacks = [[stack[i:i+3] for i in range(0, len(stack), 4)]
              for stack in stacks]
    steps = steps.split("\n")
    stack_dict = {str(x+1): list() for x in range(9)}
    for level in stacks[:-1]:
        for stack_index in range(len(level)):
            if(level[stack_index] != "   "):
                stack_dict[str(stack_index+1)].append(level[stack_index])
    for step in steps:
        crates, source, dest = [step.split(" ")[i] for i in [1, 3, 5]]
        stack_dict[dest] = list(reversed(stack_dict[source][:int(
            crates)]))+stack_dict[dest]
        stack_dict[source] = stack_dict[source][int(crates):]
    print([x[0] if len(x) > 0 else "" for x in list(stack_dict.values())])
