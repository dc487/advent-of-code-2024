import pathlib

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

def check_increasing(levels, current_index):
    if current_index >= len(levels):
        return False
    
    current_level = levels[current_index]
    next_level = levels[current_index + 1]
    is_safe_increase = next_level > current_level and next_level < current_level + 4

    if current_index + 2 >= len(levels):
        return is_safe_increase
    else:
        return is_safe_increase and check_increasing(levels, current_index + 1)

def check_decreasing(levels, current_index):
    if current_index >= len(levels):
        return False
    
    current_level = levels[current_index]
    next_level = levels[current_index + 1]
    is_safe_decrease = next_level < current_level and next_level > current_level - 4

    if current_index + 2 >= len(levels):
        return is_safe_decrease
    else:
        return is_safe_decrease and check_decreasing(levels, current_index + 1)

if __name__ == "__main__":
    input = load_input()

    safe_reports_part_1 = []
    for report in input:
        levels = [int(x) for x in report.split(" ")]
        if check_increasing(levels, 0) or check_decreasing(levels, 0):
            safe_reports_part_1.append(report)

    print(len(safe_reports_part_1))

    safe_reports_part_2 = []
    for report in input:
        levels = [int(x) for x in report.split(" ")]
        if check_increasing(levels, 0) or check_decreasing(levels, 0):
            safe_reports_part_2.append(report)
        else:
            for i in range(len(levels)):
                skipped_levels = levels[:i] + levels[i + 1:]
                if check_increasing(skipped_levels, 0) or check_decreasing(skipped_levels, 0):
                    safe_reports_part_2.append(report)
                    break

    print(len(safe_reports_part_2))

