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
