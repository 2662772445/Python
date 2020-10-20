# To count repetition number in list using dictionary

a1 = [1, 2, 2, 3, 4, 10, 9, 11, 8, 7, 6, 3, 11, 9, 3, 1, 3]

dc = dict()

for no in a1:
    if no in dc:
        dc[no] = dc[no] + 1
    else:
        dc[no] = 1
print(dc)
