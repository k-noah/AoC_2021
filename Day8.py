
import ast
import numpy as np

# Day 7 Part 1

# with open('test_input.txt', 'r') as f:
with open('input_8.txt', 'r') as f:
    signals = f.read().splitlines()


def det_signals_init(signal):
    if len(signal) == 2:
        sig = 1
    elif len(signal) == 3:
        sig = 7
    elif len(signal) == 4:
        sig = 4
    elif len(signal) == 5:
        sig = 235
    elif len(signal) == 6:
        sig = 609
    elif len(signal) == 7:
        sig = 8
    sig0 = ['a', 'b', 'c', 'e', 'f', 'g']
    sig1 = ['c', 'f']
    sig2 = ['a', 'c', 'd', 'e', 'g']
    sig3 = ['a', 'c', 'd', 'f', 'g']
    sig4 = ['b', 'c', 'd', 'f']
    sig5 = ['a', 'b', 'd', 'f', 'g']
    sig6 = ['a', 'b', 'd', 'e', 'f', 'g']
    sig7 = ['a', 'c', 'f']
    sig8 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    sig9 = ['a', 'b', 'c', 'd', 'f', 'g']
    return sig

ct_sigs = 0

for signal in signals:
    sig_in = (signal.split(' | ')[0]).split(' ')
    sig_out = (signal.split(' | ')[1]).split(' ')
    for s in sig_out:
        s_det = det_signals_init(s)
        if s_det < 10:
            ct_sigs += 1

print("Final answer is:", ct_sigs)

# Day 8 Part 2


def signal_235(known_code, possibilities):
    while len(possibilities) > 0:
        for p in possibilities:
            if len(set(known_code[1]).intersection(p)) == 2:
                known_code[3] = p
                possibilities.remove(p)
            elif len(set(known_code[4]).intersection(p)) == 3:
                known_code[5] = p
                possibilities.remove(p)
            elif len(set(known_code[4]).intersection(p)) == 2:
                known_code[2] = p
                possibilities.remove(p)
    return known_code


def signal_609(known_code, possibilities):
    while len(possibilities) > 0:
        for p in possibilities:
            if len(set(known_code[5]).intersection(p)) == 5:
                if len(set(known_code[1]).intersection(p)) == 2:
                    known_code[9] = p
                    possibilities.remove(p)
                else:
                    known_code[6] = p
                    possibilities.remove(p)
            else:
                known_code[0] = p
                possibilities.remove(p)
    return known_code


values_sum = 0
for signal in signals:
    # create code to reference later
    code = dict.fromkeys(range(0, 10), '')
    # house #s 0, 9, 6, 3, 2, 5
    tbd = {235: [], 609: []}
    # input signals
    sig_in = sorted((signal.split(' | ')[0]).split(' '), key=len)
    # output signals
    sig_out = (signal.split(' | ')[1]).split(' ')
    # go through individual signs in input signal
    for s in sig_in:
        # see if we can determine if it's 7, 1, 4, 8 or unknown
        s_det = det_signals_init(s)
        if s_det < 10:
            code[s_det] = sorted(s)
        else:
            tbd[s_det].append(sorted(s))
    code = signal_235(code, tbd[235])
    code2 = signal_609(code, tbd[609])
    # print(code2)

    # find matching ones in output
    value = ''
    for s in sig_out:
        for i in code:
            if code[i] == sorted(s):
                value += str(i)
    values_sum += int(value)


print("Final answer is:", values_sum)
