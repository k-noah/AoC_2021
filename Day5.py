
from collections import Counter

# Day 5 Part 1

# https://stackoverflow.com/questions/14048728/generate-list-of-range-tuples-with-given-boundaries-in-python
def gen_range_x(x1, x2, y):
    return [(i, y) for i in range(x1, x2 + 1)]

def gen_range_y(x, y1, y2):
    return [(x, i) for i in range(y1, y2 + 1)]

def gen_range_xy(x1, x2, y1, y2):
    if x1 > x2:
        a = -1
    else:
        a = 1
    if y1 > y2:
        b = -1
    else:
        b = 1
    return [(i, j) for i, j in zip(range(x1, x2+a, a), range(y1, y2+b, b))]


with open('input_5.txt', 'r') as f:
# with open('test_input.txt', 'r') as f:
    vents = [i.split(' -> ') for i in f]

# 1 parse file
for i in range(len(vents)):
    vents[i] = [tuple(map(int, i.split(','))) for i in vents[i]]

lines1 = []
lines2 = []
for vent in vents:
    # 2: if x's or y's of the tuple is the same, then create range
    if vent[0][0] == vent[1][0]:
        y1 = min(vent[0][1], vent[1][1])
        y2 = max(vent[0][1], vent[1][1])
        r_vent = gen_range_y(vent[0][0], y1, y2)
        # 3: append all values of range to a dictionary with a count per
        lines1.extend(r_vent)
        lines2.extend(r_vent)
    elif vent[0][1] == vent[1][1]:
        x1 = min(vent[0][0], vent[1][0])
        x2 = max(vent[0][0], vent[1][0])
        r_vent = gen_range_x(x1, x2, vent[0][1])
        lines1.extend(r_vent)
        lines2.extend(r_vent)
    # This part is for part 2, dealing with diagonals
    else:
        r_vent = gen_range_xy(vent[0][0], vent[1][0], vent[0][1], vent[1][1])
        lines2.extend(r_vent)

lines1_overlap = Counter(lines1)
print("Final answer for part 1 is:", sum(value > 1 for value in lines1_overlap.values()))

lines2_overlap = Counter(lines2)
print("Final answer for part 2 is:", sum(value > 1 for value in lines2_overlap.values()))







