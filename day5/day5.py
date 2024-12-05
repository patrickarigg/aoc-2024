def read_input():
    with open('day5/data/input.txt') as f:
        input = f.read().split("\n\n")
    raw_rules, raw_updates = input
    rules = [tuple(map(int,raw_rule.split('|'))) for raw_rule in raw_rules.strip().split("\n")]
    updates = [list(map(int,update_row.split(','))) for update_row in raw_updates.strip().split("\n")]
    return rules, updates

def get_relevant_rules(rules,update):
    relevant_rules = []
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            relevant_rules.append(rule)
    return relevant_rules

def is_update_valid(relevant_rules,update):
    for i in range(len(update)):
        page_number = update[i]
        page_number_rules = [rule for rule in relevant_rules if page_number in rule]
        prior_page_numbers = update[:i]
        next_page_numbers = update[i+1:]
        for rule in page_number_rules:
            if rule[0]==page_number and rule[1] in prior_page_numbers:
                    return False
            if rule[1]==page_number and rule[0] in next_page_numbers:
                    return False
    return True

def order_update(relevant_rules,initial_update):
    update = initial_update.copy()
    n = len(update)
    is_changed = False
    for i in range(n):
        for j in range(n-i-1):
            page_number1 = update[j]
            page_number2 = update[j+1]
            rules = [rule for rule in relevant_rules if page_number1 in rule and page_number2 in rule]

            for rule in rules:
                # print(page_number,rule)
                if rule[0]==page_number2 and rule[1]==page_number1:
                        update[j], update[j+1] = update[j+1], update[j]
                        is_changed = True
    return update, is_changed

def part1():
    rules, updates = read_input()
    total = 0
    for update in updates:
        relevant_rules = get_relevant_rules(rules,update)
        is_valid = is_update_valid(relevant_rules,update)
        if is_valid:
            middle_page = update[len(update)//2]
            total += middle_page
    return total

def part2():
    rules, updates = read_input()
    total = 0
    for update in updates:
        relevant_rules = get_relevant_rules(rules,update)
        ordered_update, is_changed = order_update(relevant_rules,update)
        if is_changed:
            middle_page = ordered_update[len(ordered_update)//2]
            total += middle_page
    return total

if __name__ == "__main__":
    res1 = part1()
    print(f"Part 1: {res1}")
    res2 = part2()
    print(f"Part 2: {res2}")
