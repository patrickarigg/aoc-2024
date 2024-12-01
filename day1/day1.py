def read_input():
    with open('day1/data/input.txt', 'r') as f:
        lines = f.readlines()
    nums_list = [line.strip().split('   ') for line in lines]
    list_1 = [int(nums[0]) for nums in nums_list]
    list_2 = [int(nums[1]) for nums in nums_list]

    return list_1, list_2

def part1():
    list_1, list_2 = read_input()
    list_1.sort()
    list_2.sort()
    sum_of_diffs = sum([abs(a - b) for a, b in zip(list_1, list_2)])
    return sum_of_diffs

def part2():
    list_1, list_2 = read_input()
    list_1.sort()
    list_2.sort()

    frequencies = {}
    total = 0

    for i in list_1:
        if i in frequencies:
            total += frequencies[i]*i
            continue
        frequencies[i] = 0
        for j in list_2:
            if j==i:
                frequencies[i] += 1
        total += frequencies[i]*i

    return total



if __name__ == '__main__':
    res1 = part1()
    print("part 1:",res1)
    res2 = part2()
    print("part 2:",res2)
