import numpy as np
import pandas as pd

# Day 11 Part 1
# 1) load in as dataframe, each # gets a different position

# df = pd.read_csv('test_input.txt', header=None, dtype='str')
df = pd.read_csv('input_11.txt', header=None, dtype='str')

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


def add_one(x):
    return x + 1


def flash(coor, df):
    y = coor[0]
    x = coor[1]
    all_x = list(range(max(x-1, 0), min(x+2, len(df.columns))))
    all_y = list(range(max(y-1, 0), min(y+2, len(df))))
    for new_x in all_x:
        for new_y in all_y:
            if new_x == x and new_y == y:
                df[x][y] = 0
            else:
                df[new_x][new_y] += 1
    return df

# iterate through 10 steps


n_flash = 0
for step in range(100):
    df = df.apply(add_one)
    flashed = []
    while df.to_numpy().max() >= 10:
        coords = df[df >= 10].stack().index.tolist()
        flashed.extend(coords)
        for coor in coords:
            df = flash(coor, df)
    for coor in flashed:
        df.at[coor[0], coor[1]] = 0
    n_flash += len(flashed)

print("Final answer is:", n_flash)



# Day 11 Part 2

# reload in df
# df = pd.read_csv('test_input.txt', header=None, dtype='str')
df = pd.read_csv('input_11.txt', header=None, dtype='str')

n_cols = len(df[0][0])
df.rename(columns={0: 'initial'}, inplace=True)
df = split_digits(df)[range(n_cols)]

n_flash = 0
steps = 0
while n_flash < 100:
    steps += 1
    df = df.apply(add_one)
    flashed = []
    while df.to_numpy().max() >= 10:
        coords = df[df >= 10].stack().index.tolist()
        flashed.extend(coords)
        for coor in coords:
            df = flash(coor, df)
    flashed = list(set(flashed))
    for coor in flashed:
        df.at[coor[0], coor[1]] = 0
    n_flash = len(flashed)

print("Final answer is:", steps)
