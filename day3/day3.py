import re

def read_input():
    with open('day3/data/input.txt') as f:
        input = f.read().replace("\n","").replace(" ","")
    return input

def part1():
    input = read_input()
    matches = re.findall(r"mul\((\d+),(\d+)\)",input)
    result = sum([int(x) * int(y) for x,y in matches])
    return result

def part2():
    input = read_input()

    start_section = re.findall(r"^.*?don't\(\)",input)
    middle_sections = re.findall(r"do\(\).*?don't\(\)",input)

    valid_sections = "".join(start_section + middle_sections)

    end_string = re.findall(r".*(do\(\).*?$)",input)[0]
    if "don't()" in end_string:
        pass
    else:
        valid_sections += end_string

    matches = re.findall(r"mul\((\d+),(\d+)\)",valid_sections)
    result = sum([int(x) * int(y) for x,y in matches])
    return result


if __name__ == "__main__":
    res1 = part1()
    print(f"Part 1: {res1}")
    res2 = part2()
    print(f"Part 2: {res2}")
