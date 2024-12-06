import pathlib
import re

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n")

if __name__ == "__main__":
    input = load_input()

    instructions = re.findall("mul\(\d+,\d+\)", input)
    multiplications = [x.strip("mul(").strip(")") for x in instructions]
    
    results = [int(x.split(",")[0]) * int(x.split(",")[1]) for x in multiplications]
    print(sum(results))

    part_2_instructions = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", input)
    valid_instructions = []
    can_multiply = True
    for instruction in part_2_instructions:
        if instruction == "do()":
            can_multiply = True
        elif instruction == "don't()":
            can_multiply = False
        elif can_multiply:
            valid_instructions.append(instruction)

    multiplications = [x.strip("mul(").strip(")") for x in valid_instructions]
    
    results = [int(x.split(",")[0]) * int(x.split(",")[1]) for x in multiplications]
    print(sum(results))
