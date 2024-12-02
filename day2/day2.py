def read_input():
    with open('day2/data/input.txt', 'r') as f:
        lines = f.readlines()
    reports = [list(map(int,line.strip().split(' '))) for line in lines]
    # print(reports)
    return reports

def is_valid_increasing_order(report):
    for i in range(len(report)-1):
        if report[i+1] <= report[i]:
            return False
        if report[i+1]-report[i]>3:
            return False
    return True

def is_valid_decreasing_order(report):
    for i in range(len(report)-1):
        if report[i+1] >= report[i]:
            return False
        if report[i]-report[i+1]>3:
            return False
    return True

def part1():
    reports = read_input()
    report_results = [is_valid_decreasing_order(report) or is_valid_increasing_order(report) for report in reports]
    print(report_results)
    return sum(report_results)

def is_valid_increasing_order_2(report):
    for i in range(len(report)-1):
        if report[i+1] <= report[i]:
            return is_valid_increasing_order(report[:i]+report[i+1:]) or is_valid_increasing_order(report[:i+1]+report[i+2:])
        if report[i+1]-report[i]>3:
            return is_valid_increasing_order(report[:i]+report[i+1:]) or is_valid_increasing_order(report[:i+1]+report[i+2:])
    return True

def is_valid_decreasing_order_2(report):
    for i in range(len(report)-1):
        if report[i+1] >= report[i]:
            return is_valid_decreasing_order(report[:i]+report[i+1:]) or is_valid_decreasing_order(report[:i+1]+report[i+2:])
        if report[i]-report[i+1]>3:
            return is_valid_decreasing_order(report[:i]+report[i+1:]) or is_valid_decreasing_order(report[:i+1]+report[i+2:])
    return True

def part2():
    reports = read_input()
    report_results = [is_valid_decreasing_order_2(report) or is_valid_increasing_order_2(report) for report in reports]
    return sum(report_results)

if __name__ == '__main__':
    res1 = part1()
    print(f"Part 1: {res1}")
    res2 = part2()
    print(f"Part 2: {res2}")
