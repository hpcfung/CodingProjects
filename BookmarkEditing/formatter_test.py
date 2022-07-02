import sys

def calc_depth(in_string):
    in_depth = 1
    for I in range(len(in_string)):
        if in_string[I] == '\t':
            in_depth += 1
        else:
            break
    return in_depth

def calc_prefix(depth1,depth2,line,ch,sec,subsec):
    new_line = 'init value'
    if depth2 == 1: # new chapter
        ch += 1
        sec,subsec = 0,0
        new_line = 'Ch.'+str(ch)+' '+line
    elif depth2 == 2: # new section
        sec += 1 # sec goes from 0 to 1, or sec goes from n to n + 1
        prefix = '\t'+str(ch)+'.'+str(sec)+' '
        new_line = prefix+line[1:]
        if depth1 == 3:
            subsec = 0
    elif depth2 == 3: # new subsection
        subsec += 1
        prefix = '\t\t'+str(ch)+'.'+str(sec)+'.'+str(subsec)+' '
        new_line = prefix + line[2:]
    else:
        # print(f'error: depth is {depth2}')
        # sys.exit()
        new_line = line
    return new_line,ch,sec,subsec

def check_if_skip(line):
    avoid_these = ['Foreword',
                   'Preface',
                   'Acknowledgments',
                   'List of symbols',
                   'Index']
    flag = False
    for candidate in avoid_these:
        if candidate in line:
            flag = True
            break
    return flag


if __name__ == "__main__":
    file1 = open('QIP_implement.txt', 'r')
    Lines = file1.readlines()
    Lines2 = Lines.copy()

    skip_all = False
    ch,sec,subsec,depth = 0,0,0,0
    for i,line in enumerate(Lines):
        old_depth = depth
        print(line)
        if 'Bibliography' in line:
            skip_all = True
        if skip_all:
            new_line = line
        else:
            depth = calc_depth(line)
            if depth > 3:
                print(f"error: depth = {depth}")
                sys.exit()
            if check_if_skip(line=line):
                continue
            new_line, ch, sec, subsec = calc_prefix(old_depth, depth, line=line,
                                                    ch=ch, sec=sec, subsec=subsec)
        # new_line = new_line.replace(',open,',',closed,')
        print(new_line)
        Lines2[i] = new_line

    file1.close()

    file2 = open('Implement_EDITED.txt', 'w')
    file2.writelines(Lines2)
    file2.close()



# cases: can go up any level, but can only go down one level
# ch to next ch
# ch to next sec
# sec to next ch
# sec to next sec
# sec to next subsec
# subsec to next ch
# subsec to next sec
# subsec to next subsec

# as far as structure of prefix is concerned, only depth2 matters
# ch to next ch
# sec to next ch
# subsec to next ch
# ch to next sec
# sec to next sec
# subsec to next sec
# sec to next subsec
# subsec to next subsec




# for i,line in enumerate(Lines):
#     old_depth = depth
#     print(line,line[0])
#     if line[0] == '\t':
#         if line[1] == '\t':
#             print('2 tabs')
#         else:
#             print('1 tab')
#     else:
#         depth = 1
#
#     Lines2[i] = '\t'+Lines2[i]
#
# print(type(Lines))

# if i == 21:
#     print(line)
#     print(line == '\tBibliographical and Historical Notes')
#     sys.exit()
