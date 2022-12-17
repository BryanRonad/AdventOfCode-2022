dimension = 4000000


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_diamond_points(left, right, up, down):
    points = []
    x_mid = (left[0] + right[0]) // 2
    y_mid = (up[1] + down[1]) // 2
    radius = abs(x_mid - left[0])
    for x in range(left[0], right[0] + 1):
        for y in range(up[1], down[1] + 1):
            if abs(x-x_mid) + abs(y-y_mid) <= radius:
                points.append([x, y])
    return points


def is_point_in_diamond(point, diamond):
    x, y = point
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = diamond
    # Calculate midpoints
    x_mid = (x1 + x2) / 2
    y_mid = (y3 + y4) / 2
    # Calculate the distance between the point and the midpoints
    x_dist = abs(x - x_mid)
    y_dist = abs(y - y_mid)
    size = [x_mid - x1, y_mid - y3]
    return x_dist / size[0] + y_dist / size[1] <= 1


with open("/Users/bryanronad/Documents/Practice/AdventOfCode-2022/Day 15/input.txt") as file:
    input = file.read().split("\n")
    sensor_arr = list()
    beacon_arr = list()
    sensor_dict = dict()
    sensor_coverage = dict()
    for index, line in enumerate(input):
        positions = [list(map(lambda x: int(x.split("=")[1]), y))
                     for y in [x.split(",") for x in line.split(":")]]
        sensor, beacon = positions
        # Create a sensor and beacon array
        sensor_arr.append(sensor)
        beacon_arr.append(beacon)
        sensor_dict[tuple(sensor)] = beacon

    # Check coverage of each sensor
    covered_yet = list()
    diamonds = list()
    diamond_points = list()
    for sensor in sensor_arr:
        # Get the beacon of the sensor
        beacon = sensor_dict[tuple(sensor)]
        # Get the distance between the sensor and beacon
        distance = manhattan_distance(sensor, beacon)
        diamond = ((sensor[0]-distance, sensor[1]), (sensor[0]+distance, sensor[1]),
                   (sensor[0], sensor[1]-distance), (sensor[0], sensor[1]+distance))
        # diamond_points += get_diamond_points(*diamond)
        diamonds.append(diamond)

    # Check for unknown beacon's location
    # unknown_beacon = tuple()
    # for i in range(row):
    #     for j in range(col):
    #         if [i, j] in diamond_points:
    #             continue
    #         unknown_beacon = (i, j)

    # print(4000000*unknown_beacon[0] + unknown_beacon[1])

    # Faster check for unknown beacon's location
        # Get min and max x coordinate of beacon or sensor
        # Extract all the x values into a separate list
    x_values = [x for t in diamonds for x, y in t]

    # Find the lowest and highest x values
    min_x = min(x_values)
    max_x = max(x_values)

    unknown_beacon = False
    flag = True
    for i in range(dimension+1):
        for j in range(dimension+1):
            for diamond in diamonds:
                if is_point_in_diamond((i, j), diamond):
                    flag = False
                    break
            if flag:
                unknown_beacon = (i, j)
                break
            flag = True
        if unknown_beacon:
            print(unknown_beacon)
            print(4000000*unknown_beacon[0] + unknown_beacon[1])
            break
