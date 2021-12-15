
# Day 13 Part 1
import pandas as pd

# with open('test_input.txt', 'r') as f:
with open('input_13.txt', 'r') as f:
    manual = f.read().splitlines()

# determine dots vs folding
dots = []
folds = []
for m in manual:
    if m.startswith('f'):
        folds.append(m)
    elif len(m) > 0:
        dots.append(tuple(map(int, m.split(','))))

# determine df size
cols = max(dots)[0]
rows = max(dots[1])
print(cols, rows)

df = pd.DataFrame(columns=list(range(cols)), index=list(range(rows)))
for dot in dots:
    df.at[dot[1], dot[0]] = 1


def fold_paper(instr, df):
    instr = instr.split(' ')[-1]
    axis = instr.split('=')[0]
    loc = int(instr.split('=')[-1])
    if axis == 'x':
        df_new = df.iloc[:, 0:loc].copy()
        df_old = df.iloc[:, loc+1:].copy()
        coords = df_old[df_old == 1].stack().index.tolist()
        for coord in coords:
            new_y = coord[1] - 2*(coord[1] - loc)
            df_new.at[coord[0], new_y] = 1
    elif axis == 'y':
        df_new = df.iloc[0:loc, :].copy()
        df_old = df.iloc[loc+1:, :].copy()
        coords = df_old[df_old == 1].stack().index.tolist()
        for coord in coords:
            new_x = coord[0] - 2*(coord[0] - loc)
            df_new.at[new_x, coord[1]] = 1
    return df_new

# just get # of dots in the first one
for fold in folds[0:1]:
    df = fold_paper(fold, df)

print("Final answer is:", sum(df[df == 1].count()))

# Day 13 Part 2

for fold in folds[1:]:
    df = fold_paper(fold, df)

pd.set_option("display.max_rows", None, "display.max_columns", None)

print("Final answer is:", df)