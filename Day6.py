
import ast

# with open('test_input.txt', 'r') as f:
with open('input_6.txt', 'r') as f:
    fish = list(ast.literal_eval(f.read()))

days = 80
day = 1
while day <= days:
    for i in range(len(fish)):
        if fish[i] == 0:
            fish.append(8)
            fish[i] = 6
        else:
            fish[i] -= 1
    day += 1

print("Final answer is:", len(fish))

# Part 2
# keep track of all the fish & their birthdays
# if today is 9 days after birth, then add new fish
# elif today is 9 days + multiple of 7 days after birth, then add new fish

# with open('test_input.txt', 'r') as f:
with open('input_6.txt', 'r') as f:
    fish = list(ast.literal_eval(f.read()))

days = 256
day = 1
fish_ct = dict.fromkeys(range(-8, days+1), 0)

for i in range(len(fish)):
    fish_ct[fish[i]-8] += 1

while day <= days:
    for fish in fish_ct:
        if (day - fish == 9) & (fish_ct[fish] > 0):
            fish_ct[day] += fish_ct[fish]
        elif day - fish > 9:
            if ((day - fish - 9) % 7 == 0) & (fish_ct[fish] > 0):
                fish_ct[day] += fish_ct[fish]
    day += 1


print("Final answer is:", sum(fish_ct.values()))