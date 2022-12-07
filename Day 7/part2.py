from collections import defaultdict

with open("input.txt") as file:
    file_input = file.read().split("\n")
    current_dir = ["/"]
    dir_size = defaultdict(int)
    for index, line in enumerate(file_input):
        if line[0] == "$":
            command = line[2:]
            if(command[:2] == "cd"):
                change_to = command[3:]
                if(change_to == ".."):
                    current_dir.pop()
                    continue
                if(change_to == "/"):
                    current_dir = ["/"]
                    continue
                current_dir.append(f"{change_to}")
        else:
            prefix, name = line.split(" ")
            if(prefix == "dir"):
                continue
            for i in range(1, len(current_dir)+1):
                dir_size['/'.join(current_dir[:i])] += int(prefix)
    print(min([v for v in dir_size.values()
          if v >= dir_size['/']-(70000000 - 30000000)]))
