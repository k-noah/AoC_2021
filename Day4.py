
import pandas as pd

# Day 4 Part 1

f = open('input_4.txt', 'r')
# f = open('test_input.txt', 'r')
lines = f.read().splitlines()

# https://www.geeksforgeeks.org/find-location-of-an-element-in-pandas-dataframe-in-python/
# This function will return a list of
# positions where element exists
# in the dataframe.


def getIndexes(dfObj, value):

    # isin() method will return a dataframe with
    # boolean values, True at the positions
    # where element exists
    listOfPos = []
    result = dfObj.isin([value])

    # any() method will return
    # a boolean series
    seriesObj = result.any()

    # Get list of column names where
    # element exists
    columnNames = list(seriesObj[seriesObj == True].index)

    # Iterate over the list of columns and
    # extract the row index where element exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)

        for row in rows:
            listOfPos = [row, col]

    # This list contains a list tuples with
    # the index of element in the dataframe
    return listOfPos


# 1) read in first line -> this is the list to check against
bingo_list = lines[0].split(',')

# 2) create variable that holds the earliest # that causes a finished card, and all un-called #s, and the most recent #
#   called
bingo_winner_loc = len(bingo_list)
bingo_winner = -1
unmarked = []
unmarked_temp = []
marked_col = dict.fromkeys(range(5), 0)
marked_row = dict.fromkeys(range(5), 0)
# 3) create "bingo card" for lines 3-7 (?)
ct_lines = 0
bingo_card = {}
for i in range(2, len(lines)):
    line = [x for x in lines[i].split() if x]
    if lines[i] == '':
        ct_lines = 0
        unmarked_temp = []
        bingo_card = {}
        marked_col = dict.fromkeys(range(5), 0)
        marked_row = dict.fromkeys(range(5), 0)
    elif ct_lines < 4:
        bingo_card[ct_lines] = line
        unmarked_temp.extend(line)
        ct_lines += 1
    else:
        bingo_card[ct_lines] = line
        unmarked_temp.extend(line)
        df_bingo = pd.DataFrame(data=bingo_card)
        # 4) iterate through # list
        for b in range(len(bingo_list)):
            number = bingo_list[b]
            # 5) check off # in bingo list
            location = getIndexes(df_bingo, number)
            if len(location) == 2 and 5 not in marked_row.values() and 5 not in marked_col.values():
                marked_row[location[0]] += 1
                marked_col[location[1]] += 1
                unmarked_temp.remove(number)
            # 6) see if whole row or column is checked off (can start checking at item 4 in list)
            if 5 in marked_row.values() or 5 in marked_col.values():
                # 7) if lower than the variable, then save variable, un-called #s, most recent # called
                if b < bingo_winner_loc:
                    bingo_winner_loc = b
                    bingo_winner = number
                    unmarked = unmarked_temp

unmarked = [int(x) for x in unmarked]
unmarked_sum = sum(unmarked)

print("Final answer is:", int(bingo_winner) * unmarked_sum)

# Day 2 Part 2

# DO THE SAME SHIT BUT LOOK FOR THE LAST ONE TO WIN
# 2) create variable that holds the earliest # that causes a finished card, and all un-called #s, and the most recent #
#   called
bingo_winner_loc = 0
bingo_winner = -1
unmarked = []
unmarked_temp = []
marked_col = dict.fromkeys(range(5), 0)
marked_row = dict.fromkeys(range(5), 0)
# put in boolean value so that the 'last winning' bingo card won't be checked continuously
check = True
# 3) create "bingo card" for lines 3-7 (?)
ct_lines = 0
bingo_card = {}
for i in range(2, len(lines)):
    line = [x for x in lines[i].split() if x]
    if lines[i] == '':
        ct_lines = 0
        unmarked_temp = []
        bingo_card = {}
        marked_col = dict.fromkeys(range(5), 0)
        marked_row = dict.fromkeys(range(5), 0)
        check = True
    elif ct_lines < 4:
        bingo_card[ct_lines] = line
        unmarked_temp.extend(line)
        ct_lines += 1
    else:
        bingo_card[ct_lines] = line
        unmarked_temp.extend(line)
        df_bingo = pd.DataFrame(data=bingo_card)
        # 4) iterate through # list
        for b in range(len(bingo_list)):
            number = bingo_list[b]
            # 5) check off # in bingo list
            location = getIndexes(df_bingo, number)
            if len(location) == 2 and 5 not in marked_row.values() and 5 not in marked_col.values():
                marked_row[location[0]] += 1
                marked_col[location[1]] += 1
                unmarked_temp.remove(number)
            # 6) see if whole row or column is checked off (can start checking at item 4 in list)
            if (5 in marked_row.values() or 5 in marked_col.values()) and check == True:
                check = False
                # 7) if lower than the variable, then save variable, un-called #s, most recent # called
                if b > bingo_winner_loc:
                    bingo_winner_loc = b
                    bingo_winner = number
                    unmarked = unmarked_temp


unmarked = [int(x) for x in unmarked]
unmarked_sum = sum(unmarked)

print("Final answer is:", int(bingo_winner)*unmarked_sum)
