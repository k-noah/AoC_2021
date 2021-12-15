
import pandas as pd

df = pd.read_csv('input_2.txt', header=None, sep=' ')

d = 0
h = 0
for i, row in df.iterrows():
    if row[0] == 'forward':
        h += row[1]
    elif row[0] == 'down':
        d += row[1]
    elif row[0] == 'up':
        d -= row[1]

print("Part 1 answer is:", d*h)


d = 0
h = 0
a = 0
for i, row in df.iterrows():
    if row[0] == 'forward':
        h += row[1]
        d += a*row[1]
    elif row[0] == 'down':
        a += row[1]
    elif row[0] == 'up':
        a -= row[1]

print("Part 1 answer is:", d*h)