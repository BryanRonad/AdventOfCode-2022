row = 2000000


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


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


with open("input.txt") as file:
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
    for sensor in sensor_arr:
        # Get the beacon of the sensor
        beacon = sensor_dict[tuple(sensor)]
        # Get the distance between the sensor and beacon
        distance = manhattan_distance(sensor, beacon)
        diamond = ((sensor[0]-distance, sensor[1]), (sensor[0]+distance, sensor[1]),
                   (sensor[0], sensor[1]-distance), (sensor[0], sensor[1]+distance))
        diamonds.append(diamond)
    # Get min and max x coordinate of beacon or sensor
    # Extract all the x values into a separate list
    x_values = [x for t in diamonds for x, y in t]

    # Find the lowest and highest x values
    min_x = min(x_values)
    max_x = max(x_values)
    # Check the rowth row if exists in diamonds
    hashes = 0
    flag = False
    for i in range(min_x, max_x+1):
        for diamond_index, diamond in enumerate(diamonds):
            if is_point_in_diamond((i, row), diamond):
                flag = True
                break
        hashes += 1 if flag and [i, row] not in sensor_arr+beacon_arr else 0
        flag = False
    print(hashes)
