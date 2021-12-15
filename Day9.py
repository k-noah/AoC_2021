
import numpy as np
import pandas as pd

# Day 9 Part 1
# 1) load in as dataframe, each # gets a different position

# df = pd.read_csv('test_input.txt', header=None, dtype=str)
df = pd.read_csv('input_9.txt', header=None)

n_cols = len(df[0][0])
df.rename(columns={0: 'initial'}, inplace=True)

def split_digits(df):
    # get data as numpy array
    df = df['initial'].apply(lambda x: pd.Series(list(x)))
    # extract digits
    df = df.astype(int)
    # build and return new data frame
    return df

df = split_digits(df)[range(n_cols)]


# iterate through items, get one before, after, up, down if possible
# if not smaller than all things beside it, then move one
# else return the # +1

n_rows = len(df)

def check_right(dataframe, x, y, cols):
    check = False
    if x < cols - 1:
        if dataframe[x][y] >= dataframe[x+1][y]:
            check = True
    return check

def check_left(dataframe, x, y):
    check = False
    if x > 0:
        if dataframe[x][y] >= dataframe[x-1][y]:
            check = True
    return check

def check_down(dataframe, x, y, rows):
    check = False
    if y < rows - 1:
        if dataframe[x][y] >= dataframe[x][y+1]:
            check = True
    return check

def check_up(dataframe, x, y):
    check = False
    if y > 0:
        if dataframe[x][y] >= dataframe[x][y-1]:
            check = True
    return check

def check_all(dataframe, x, y, cols, rows):
    check = False
    if check_up(dataframe, x, y) or check_down(dataframe, x, y, rows) or check_left(dataframe, x, y) or check_right(dataframe, x, y, cols):
        check = True
    return check

answer = 0
basins = {}
for i, row in df.iterrows():
    gt = False
    # check right
    for j in range(n_cols):
        if check_all(df, j, i, n_cols, n_rows) == False:
            # print(j, i, df[j][i])
            answer += 1 + df[j][i]
            basins[(j, i)] = [(j, i)]

print("Final answer is:", answer)

# Day 9 Part 2

import math
# convert to binary matrix
df2 = df.replace(range(9), 1)
df2.replace(9, 0, inplace=True)

# go through dataframe, find locations of the lowest points - these are the start of the basins
for basin in basins:
    df2.at[basin[1], basin[0]] = 0

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

# while the max in the dataframe is still 1, continue the loop
ct = 0
while df2.to_numpy().max() == 1:
    print(ct)
    ct += 1
    for i, row in df2.iterrows():
        for j in range(len(df2.columns)):
            if df2[j][i] == 1:
                for b in basins:
                    # print(distance(b, (j, i)))
                    if distance(b, (j, i)) < 50:
                        for x in basins[b]:
                            # if the mininum distance between two points is 1(?), then add it to that group, change to
                            if distance(x, (j, i)) == 1:
                               basins[b].append((j, i))
                               df2.at[i, j] = 0

# go through dictionary, find 3 longest lists
l_basins = []
for b in basins:
    l_basins.append(len(set(basins[b])))

l_basins.sort(reverse=True)
print(l_basins[:3])
print("Final answer is:", l_basins[0]*l_basins[1]*l_basins[2])

