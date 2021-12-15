
# Day 14 Part 1

# with open('test_input.txt', 'r') as f:
with open('input_14.txt', 'r') as f:
    instructions = f.read().splitlines()

template = instructions[0]
inserts = instructions[2:]

d_insert = {}
d_rules = {}
for insert in inserts:
    pair = insert.split(' -> ')[0]
    element = insert.split(' -> ')[-1]
    new_pairs = [pair[0]+element, element+pair[1]]
    d_insert[pair] = 0
    d_rules[pair] = new_pairs

# template
for t in range(len(template)-1):
    # read pair
    pair = template[t:t+2]
    d_insert[pair] += 1

# iterate through steps
# Part 1 use 10, Part 2 use 40
steps = 40
for i in range(steps):
    new_d_insert = dict.fromkeys(d_insert, 0)
    for item in d_insert:
        if d_insert[item] > 0:
            rule = d_rules[item]
            for r in rule:
                new_d_insert[r] += d_insert[item]
    d_insert = new_d_insert.copy()


# count amounts:
# separate the pairs, and add the #s. Add 1 to the first & last # to start, then divide the totals by 2

counts = {}
for k in d_insert.keys():
    if k[0] in counts.keys():
        counts[k[0]] += d_insert[k]
    else:
        counts[k[0]] = d_insert[k]
    if k[1] in counts.keys():
        counts[k[1]] += d_insert[k]
    else:
        counts[k[1]] = d_insert[k]


counts[template[0]] += 1
counts[template[-1]] += 1

for c in counts:
    counts[c] = counts[c]/2

print("Final answer is:", int(max(counts.values()) - min(counts.values())))
