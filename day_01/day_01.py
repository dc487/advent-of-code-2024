import pathlib
from collections import Counter

def load_input():
    return pathlib.Path("./input.txt").read_text().strip("\n").splitlines()

if __name__ == "__main__":
    input = load_input()

    left_list = [int(x.split("   ")[0]) for x in input]
    right_list = [int(x.split("   ")[1]) for x in input]

    left_list.sort()
    right_list.sort()

    differences = sum([abs(left_list[x] - right_list[x]) for x in range(0, len(left_list))])

    print(differences)

    counts = Counter(right_list)
    similarity_score = sum([counts[x] * x for x in left_list])

    print(similarity_score)
