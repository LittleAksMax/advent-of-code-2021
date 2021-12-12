import re

data = None
with open("input.txt", "r") as f:
    data = f.read().splitlines()

brks = re.compile(r"(\[\]|\(\)|{}|<>)")  # Match the good bracket pairs
illegal_bkts = re.compile(r"(\[}|\[\)|\[>|"   # Match bad bracket pairs
                          r"{\]|{\)|{>|"
                          r"\(\]|\(}|\(>|"
                          r"<\]|<\)|<})")
COSTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
CORRECTION_COST = {"(": 1, "[": 2, "{": 3, "<": 4}  # reversed from puzzle to make replacement easier

running_cost = 0
replacement_scores = []

for i, modified_line in enumerate(data):
    keep_iterating = True
    incomplete_line = True
    while keep_iterating:
        m = illegal_bkts.search(modified_line)
        if m:
            (openb, closeb) = list(m.group(1))
            running_cost += COSTS[closeb]
            keep_iterating = False
            incomplete_line = False
        else:
            # Trim out the matching brackets until none are remaining
            (modified_line, subsmade) = brks.subn("", modified_line)
            if subsmade == 0:
                keep_iterating = False
    # Part 2
    if len(modified_line) > 0 and incomplete_line:  # incomplete line
        brks_to_add = reversed(list(modified_line))  # add in reverse order
        fix_score = 0
        for addition in brks_to_add:
            fix_score *= 5
            fix_score += CORRECTION_COST[addition]
        replacement_scores.append(fix_score)

print(running_cost)
print(replacement_scores[len(replacement_scores)//2])