
# Day 1 Part 1

import pandas as pd

df = pd.read_csv('input_1.txt', header=None, sep='\t')
# df = pd.read_csv('test_input.txt', header=None, sep='\t')

incr = 0

for i, row in df.iterrows():
    if i>0:
        if row[0] >= df[0][i-1]:
            incr += 1

print(incr)

# Day 1 Part 2

incr = 0
window = []
prev_total = 0

for i, row in df.iterrows():
    window.append(row[0])
    if 2 <= i <= len(df)-2:
        total = sum(window)
        if total > prev_total:
            incr += 1
        prev_total = total
        window.pop(0)

print(incr)