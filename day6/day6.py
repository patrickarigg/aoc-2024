import time

def read_input():
    with open("day6/data/input.txt") as f:
        return [line.strip() for line in f.readlines()]

def find_starting_position(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "^":
                return (i, j)


def find_points_visited(data, starting_point):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    pos = starting_point
    points_visited = [pos]
    turn_count = 0
    stuck = False

    turn_points = []

    while True:
        current_direction = directions[turn_count % 4]
        next_pos = (pos[0] + current_direction[0], pos[1] + current_direction[1])
        row, col = next_pos
        if row < 0 or row >= len(data) or col < 0 or col >= len(data[0]):
            break
        if data[row][col] == "#":
            turn_count += 1
            turn_point = (next_pos, current_direction)
            if turn_point in turn_points:
                stuck = True
                break
            turn_points.append(turn_point)

        else:
            pos = next_pos
            points_visited.append(pos)

    return points_visited, stuck

def part1():
    data = read_input()
    starting_point = find_starting_position(data)
    points_visited, _ = find_points_visited(data, starting_point)
    return len(list(set(points_visited)))

def part2():
    data = read_input()
    starting_point = find_starting_position(data)

    stuck_in_loop_count = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            data_copy = data.copy()
            if data_copy[i][j] != "^" and data[i][j] != "#":
                data_copy[i] = data_copy[i][:j] + "#" + data_copy[i][j+1:]
            _, is_stuck_in_loop = find_points_visited(data_copy, starting_point)
            if is_stuck_in_loop:
                stuck_in_loop_count+=1

    return stuck_in_loop_count


if __name__ == "__main__":
    start1 = time.time()
    res1 = part1()
    print(f"Part 1: {res1}, {time.time() - start1}")
    start2 = time.time()
    res2 = part2()
    print(f"Part 2: {res2}, {time.time() - start2}")
