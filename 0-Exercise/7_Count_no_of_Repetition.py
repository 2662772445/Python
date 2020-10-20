
a = [1, 2, 3, 4, 5, 6, 10, 2, 5, 8, 9, 12, 11, 3]

dc = dict()

for no in a:
    if no in dc:
        dc[no] = dc[no] + 1
    else:
        dc[no] = 1

print(dc)
