def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


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
    for sensor in sensor_arr:
        # Get the beacon of the sensor
        beacon = sensor_dict[tuple(sensor)]
        # Get the distance between the sensor and beacon
        distance = manhattan_distance(sensor, beacon)
        # Get a list of coordinates that are within the distance
        coordinates = [(x, y) for x in range(sensor[0] - distance, sensor[0] + distance + 1)
                       for y in range(sensor[1] - distance, sensor[1] + distance + 1) if manhattan_distance(sensor, [x, y]) <= distance and [x, y] not in sensor_arr+beacon_arr and [x, y] not in covered_yet]
        sensor_coverage[tuple(sensor)] = coordinates
        # if(sensor == [8, 7]):
        #     print(sensor, beacon)
        #     print([x for x in coordinates if x[1] == 10])
        covered_yet = [position for positions in sensor_coverage.values()
                       for position in positions]
    print(len(set([x for x in covered_yet if x[1] == 2000000])))
