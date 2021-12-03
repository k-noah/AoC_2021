
import pandas as pd

# Day 3 Part 1

df = pd.read_csv('input_3.txt', header=None, dtype='str')
# df = pd.read_csv('test_input.txt', header=None, dtype='str')

df = df[0].apply(lambda x: pd.Series(list(str(x))))

gamma = []
epsilon = []
for i in range(len(df.columns)):
    g = df[i].mode()[0]
    gamma.append(g)
    if g == '1':
        epsilon.append('0')
    else:
        epsilon.append('1')

gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)

print('Final answer is:', gamma*epsilon)

# Day 3 Part 2

# Oxygen rating
oxygen = ''
df_temp = df.copy()
for i in range(len(df.columns)):
    if oxygen == '':
        o = df_temp[i].mode()[0]
        if len(df_temp[df_temp[i] == o]) == len(df_temp[df_temp[i] == str(1-int(o))]):
            o = '1'
        df_temp = df_temp[df_temp[i] == o]
        if len(df_temp) == 1:
            oxygen = [str(x) for x in df_temp.iloc[0,:]]
            oxygen = int(''.join(oxygen), 2)
            print(oxygen)

# CO2 rating
co2 = ''
df_temp = df.copy()
for i in range(len(df.columns)):
    if co2 == '':
        o = df_temp[i].mode()[0]
        if o == '1':
            c = '0'
        else:
            c = '1'
        if len(df_temp[df_temp[i] == c]) == len(df_temp[df_temp[i] == str(1-int(c))]):
            c = '0'
        df_temp = df_temp[df_temp[i] == c]
        if len(df_temp) == 1:
            co2 = [str(x) for x in df_temp.iloc[0,:]]
            co2 = int(''.join(co2), 2)
            print(co2)

print('Final answer is:', oxygen*co2)
