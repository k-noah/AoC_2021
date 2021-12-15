
import ast
import numpy as np

# Day 7 Part 1

# with open('test_input.txt', 'r') as f:
with open('input_7.txt', 'r') as f:
    subs = list(ast.literal_eval(f.read()))

fuel = np.median(subs)
total_fuel = 0

for sub in subs:
    total_fuel += abs(fuel-sub)

print('Final answer is:', int(total_fuel))


# Day 7 Part 2

fuel = round(np.mean(subs))
total_fuel = 0

fuel_start = fuel-25
fuel_end = fuel+25

target = 91257681

for fuel in range(fuel_start, fuel_end):
    total_fuel = 0

    for sub in subs:
        fuel_added = sum(range(1, abs(fuel-sub)+1))
        total_fuel += fuel_added

    if total_fuel < target:
        target = total_fuel

print('Final answer is:', int(target))
# 91257681 is too high

# 91257582 was the answer, using an average of 464, not 465
