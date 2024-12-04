def read_input():
    with open('day4/data/input.txt') as f:
        data = f.readlines()
        input = [x.strip() for x in data]
    return input

def get_routes(i,j,grid):
    routes = [
        [(i,j-n) for n in range(4)],
        [(i-n,j-n) for n in range(4)],
        [(i-n,j) for n in range(4)],
        [(i-n,j+n) for n in range(4)],
        [(i,j+n) for n in range(4)],
        [(i+n,j+n) for n in range(4)],
        [(i+n,j) for n in range(4)],
        [(i+n,j-n) for n in range(4)],
    ]
    updated_routes = []
    for route in routes:
        is_valid = True
        for point in route:
            row,col = point
            if row < 0 or col < 0:
                is_valid=False
                break
            if row >= len(grid) or col >= len(grid[0]):
                is_valid=False
                break
        if is_valid:
            updated_routes.append(route)

    return updated_routes

def get_x_routes(i,j,grid):
    routes = [
        [(i+n,j+n) for n in range(-1,2)],
        [(i+n,j-n) for n in range(-1,2)],
    ]
    updated_routes = []
    for route in routes:
        is_valid = True
        for point in route:
            row,col = point
            if row < 0 or col < 0:
                is_valid=False
                break
            if row >= len(grid) or col >= len(grid[0]):
                is_valid=False
                break
        if is_valid:
            updated_routes.append(route)

    return updated_routes

def part1():
    input = read_input()

    count = 0

    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "X":
                routes = get_routes(i,j,input)
                for route in routes:
                    text = "".join([input[x][y] for x,y in route])
                    if text=="XMAS":
                        count += 1
    return count

def part2():
    input = read_input()
    count = 0

    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "A":
                routes = get_x_routes(i,j,input)
                mas_count = 0
                for route in routes:
                    text = "".join([input[x][y] for x,y in route])
                    text_reversed = text[::-1]
                    if text=="MAS" or text_reversed=="MAS":
                        mas_count += 1
                if mas_count == 2:
                    count += 1
    return count

if __name__ == "__main__":
    res1 = part1()
    print(f"Part 1: {res1}")
    res2 = part2()
    print(f"Part 2: {res2}")
