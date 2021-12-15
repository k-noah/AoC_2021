
# Day 10 Part 1
import numpy as np

# with open('test_input.txt', 'r') as f:
with open('input_10.txt', 'r') as f:
    chunks = f.read().splitlines()

def det_char(c):
    # if open character, then return list with added character
    # if close character, then check to see if same as last open one
    # if y, then remove the last char from the list
    # if n, then return last char from the list
    if c in ('([{<'):
        char_type = 'open'
    elif c in (')}]>'):
        char_type = 'close'
    return char_type


def end_char(c):
    # print(c)
    if c == '(':
        match = ')'
    elif c == '{':
        match = '}'
    elif c == '[':
        match = ']'
    elif c == '<':
        match = '>'
    return match

def char_score(c):
    if c == ')':
        score = 3
    elif c == ']':
        score = 57
    elif c == '}':
        score = 1197
    elif c == '>':
        score = 25137
    return score



total_score = 0

for chunk in chunks:
    ok_chunk = []
    corrupted = False
    for i in chunk:
        if not corrupted:
            if det_char(i) == 'open':
                ok_chunk.append(i)
            elif det_char(i) == 'close':
                last_i = ok_chunk[-1]
                if i == end_char(last_i):
                    ok_chunk.pop()
                else:
                    total_score += char_score(i)
                    corrupted = True

print("Final answer is:", total_score)


# Day 10 Part 2

all_scores = []

def new_score(c, score):
    if c == ')':
        val = 1
    elif c == ']':
        val = 2
    elif c == '}':
        val = 3
    elif c == '>':
        val = 4
    return score*5 + val

# remove corrupted lines
for chunk in chunks:
    ok_chunk = []
    corrupted = False
    for i in chunk:
        if not corrupted:
            if det_char(i) == 'open':
                ok_chunk.append(i)
            elif det_char(i) == 'close':
                last_i = ok_chunk[-1]
                if i == end_char(last_i):
                    ok_chunk.pop()
                else:
                    corrupted = True
    if not corrupted:
        needed_c = []
        for c in reversed(ok_chunk):
            needed_c.append(end_char(c))
        score = 0
        for c in needed_c:
            score = new_score(c, score)
        all_scores.append(score)
        # print(chunk, all_scores, needed_c)

all_scores.sort()
print("Final answer is:", int(np.median(all_scores)))
