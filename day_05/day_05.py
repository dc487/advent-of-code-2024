import pathlib
from functools import partial, cmp_to_key

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n")

def update_meets_rules(rules, update):
    for x in range(len(update)):
        for y in range(x + 1, len(update)):
            if update[x] + "|" + update[y] not in rules:
                return False
    
    return True

def compare_items(rules, left, right):
    if left + "|" + right in rules:
        return 1
    elif right + "|" + left in rules:
        return -1
    else:
        return 0

if __name__ == "__main__":
    input = load_input()
    input_parts = input.split("\n\n")
    rules = set(input_parts[0].splitlines())
    updates = [x.split(",") for x in input_parts[1].splitlines()]

    valid_updates = [x for x in updates if update_meets_rules(rules, x)]

    page_number_sum = 0
    for update in valid_updates:
        middle = int((len(update) - 1) / 2)
        page_number_sum += int(update[middle])

    print(page_number_sum)

    invalid_updates = [x for x in updates if not update_meets_rules(rules, x)]

    page_number_sum = 0
    for update in invalid_updates:
        update.sort(key=cmp_to_key(partial(compare_items, rules)), reverse=True)
        middle = int((len(update) - 1) / 2)
        page_number_sum += int(update[middle])

    print(page_number_sum)