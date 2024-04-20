# use flag; 13 lines
for row_idx in range(len(matrix)):
    widths = []
    counting = False
    for i, num in enumerate(matrix[row_idx]):
        if counting:
            if num == '0':
                counting = False
                widths.append((l_lim, i-1))
        elif num == '1':
            counting = True
            l_lim = i
    if counting:
        widths.append((l_lim, i))

# remember last num; 10 lines
# no additional code after loop
# no need to reset flag after condition (need to reset last in each loop though)
# access arr[i-1] instead of memorizing; slower?
for row_idx in range(len(matrix)):
    widths = []
    last = '0'
    for i, num in enumerate(matrix[row_idx]):
        if last == '0':
            if num == '1':
                l_lim = i
        elif num == '0':
            widths.append((l_lim, i-1))
        last = num
