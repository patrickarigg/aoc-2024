def read_input():
    with open('day7/data/input.txt') as f:
        data = [line.strip() for line in f.readlines()]
        equations = []
        for line in data:
            test_value = int(line.split(':')[0])
            numbers = list(map(int,line.split(':')[1].strip().split(' ')))
            equations.append((test_value, numbers))
    return equations

def generate_permutations(operators, n, current_sequence=[]):
    # Base case: if the current sequence is of length n, return it as a single result
    if len(current_sequence) == n:
        return [current_sequence]

    # Recursive case: collect results from all branches
    all_sequences = []
    for symbol in operators:
        all_sequences += generate_permutations(operators, n, current_sequence + [symbol])
    return all_sequences

def part1():
    equations = read_input()
    operators = ['+', '*']
    result = 0
    for equation in equations:
        test_value, numbers = equation
        n = len(numbers) - 1
        permutations = generate_permutations(operators, n)
        for operator_combo in permutations:
            total = numbers[0]
            for i in range(n):
                if operator_combo[i] == '+':
                    total += numbers[i+1]
                elif operator_combo[i] == '*':
                    total *= numbers[i+1]
            if total == test_value:
                result += test_value
                break
    return result

def part2():
    equations = read_input()
    operators = ['+', '*','||']
    result = 0
    for equation in equations:
        test_value, numbers = equation
        n = len(numbers) - 1
        permutations = generate_permutations(operators, n)
        for operator_combo in permutations:
            total = numbers[0]
            for i in range(n):
                if operator_combo[i] == '+':
                    total += numbers[i+1]
                elif operator_combo[i] == '*':
                    total *= numbers[i+1]
                elif operator_combo[i] == '||':
                    total = int(str(total) + str(numbers[i+1]))
            if total == test_value:
                result += test_value
                break
    return result

if __name__ == '__main__':
    res1 = part1()
    print(f"Part 1: {res1}")
    res2 = part2()
    print(f"Part 2: {res2}")
