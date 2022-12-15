def generate_grid(sand_locations, rock_locations):
    # Get the minimum and maximum x and y coordinates
    min_x = min(sand_locations + rock_locations, key=lambda x: x[0])[0]
    max_x = max(sand_locations + rock_locations, key=lambda x: x[0])[0]
    min_y = min(sand_locations + rock_locations, key=lambda x: x[1])[1]
    max_y = max(sand_locations + rock_locations, key=lambda x: x[1])[1]

    # Initialize the grid with dots
    grid = [["." for _ in range(min_x, max_x + 1)]
            for _ in range(min_y, max_y + 2)]

    # Replace the dots with #s in the locations where there are rocks
    for x, y in rock_locations:
        grid[y - min_y][x - min_x] = "#"

    # Replace the dots with #s in the locations where there is a floor
    for x in range(min_x, max_x + 1):
        grid[max_y - min_y + 1][x - min_x] = "#"

    # Replace the dots with o's in the locations where there is sand
    for x, y in sand_locations:
        grid[y - min_y][x - min_x] = "o"

    # Return the grid as a list of strings
    return ["".join(row) for row in grid]


with open("input.txt") as file:
    lines = [[list(map(int, x.split(','))) for x in point.split(' -> ')]
             for point in file.read().split("\n")]
    rocks = []
    sand = []

    def sand_coord(X, Y):
        if(Y <= -1):  # If sand blocks [500,0]
            return None
        if([X, Y+1] not in rocks+sand and Y+1 != floor_y):
            return sand_coord(X, Y+1)   # Nothing below, falling down
        if(([X-1, Y+1] in rocks+sand) or Y+1 == floor_y):
            # Left and right both occupied, sand settling
            if(([X+1, Y+1] in rocks+sand) or Y+1 == floor_y):
                return [X, Y]
            else:
                return sand_coord(X+1, Y+1)   # Right is empty
        else:
            return sand_coord(X-1, Y+1)   # Left is empty

    # Adding rocks to a list
    for line in lines:
        for i in range(len(line)-1):
            if(line[i][0] == line[i+1][0]):
                for j in range(min([line[i][1], line[i+1][1]]), max([line[i][1], line[i+1][1]])+1):
                    rocks.append([line[i][0], j])
            else:
                for j in range(min([line[i][0], line[i+1][0]]), max([line[i][0], line[i+1][0]])+1):
                    rocks.append([j, line[i][1]])

    # Looping over sand till abyss
    floor_y = max(rocks+sand, key=lambda x: x[1])[1]+2
    while True:
        min_y = min([x[1] for x in rocks+sand if x[0] == 500])
        sand_position = sand_coord(500, min_y-1)
        if sand_position:
            sand.append(sand_position)
        else:
            break

    # Draw
    print('\n'.join(generate_grid(sand, rocks)))

    # Count sand
    print("Sand count:", len(sand))
