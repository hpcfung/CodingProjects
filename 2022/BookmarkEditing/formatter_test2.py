import sys

def calc_depth(in_string):
    in_depth = 0
    for I in range(len(in_string)):
        if in_string[I] == '\t':
            in_depth += 1
        else:
            break

    if with_parts:
        if in_part:
            in_depth -= 1

    return in_depth


def calc_prefix(depth1,depth2,line,address):
    new_line = 'init value'

    new_address = []
    print(f"depth1 = {depth1}, depth2 = {depth2}")
    print(f"old address = {address}")
    for i in range(depth2+1):
        if i > depth1:
            new_address.append(0)
        else:
            new_address.append(address[i])
    new_address[depth2] += 1
    print(f"address = {new_address}")

    if add_ch and depth2 == 0:
        new_line = 'Ch.'+str(new_address[0])+' '+line
        if with_parts and in_part:
            new_line = '\t' + 'Ch.'+str(new_address[0])+' ' + line.replace('\t','')
    else:
        prefix = ''
        for j in range(depth2+1): # grow prefix recursively on both left and right
            # (tabs and . for sections)
            if j == 0:
                prefix = str(new_address[j])
            else:
                prefix = '\t'+prefix + '.' + str(new_address[j])
        if with_parts and in_part:
            depth2 += 1
            prefix = '\t'+prefix
        new_line = prefix + ' ' + line[depth2:]

    return new_line,new_address

def check_if_skip(line):
    global in_part
    avoid_these = ['Some thoughts about this book',
                   'Contents',
                   'Index']
    if with_parts:
        avoid_these = avoid_these + part_titles
        if part_titles[0] in line:
            in_part = True
        if 'Appendix: Resources for TQFTs' in line:
            in_part = False


    flag = False
    for candidate in avoid_these:
        if candidate in line:
            flag = True
            break
    return flag


if __name__ == "__main__":
    '''
    Purpose: adds section number to existing bookmarks
    
    1. Change input_filename
    2. Toggle omit_deep_index (if too nested, eg 1.2.3.1, decide add prefix or not)
       Default False can detect unexpectedly deep sections
       
       
       if with_parts = True:
    3. avoid these?
    
    How it works
    eg Section 12.1.3 has address [12, 1, 3]
    the new address is computed by comparing old depth and current depth
    eg depth1 = 2, depth2 = 2 -> new address = [12, 1, 3] 
    (this is a new subsection, so increment by 1)
    '''
    input_filename = 'chem'
    file1 = open(input_filename+'.txt', 'r')
    Lines = file1.readlines()
    Lines2 = Lines.copy()

    omit_deep_index = False
    with_parts = False
    add_ch = False

    part_titles = ['I Anyons and Topological Quantum Field Theories',
                   'II Anyon Basics',
                   'III Anyon Diagrammatics (in detail)',
                   'IV Some Examples: Planar Diagrams and Anyon Theories',
                   'V Toric Code Basics',
                   'VI More General Loop Gas and String Net Models',
                   'VII Symmetries and Entanglement',
                   'VIII Introduction to Quantum Hall Effects']
    in_part = False

    skip_all = False
    depth = 0
    address = [0]
    for i,line in enumerate(Lines):
        old_depth = depth
        print(line)
        # if 'Index/571' in line:
        #     skip_all = True
        if skip_all:
            new_line = line
        else:
            if check_if_skip(line=line):
                print('Skip this line')
                continue
            depth = calc_depth(line)
            if depth > 3:
                if omit_deep_index:
                    depth = old_depth
                    print(f'Depth = {depth}, do nothing')
                    continue
                else:
                    print(f"error: depth = {depth}")
                    sys.exit()
            new_line, address = calc_prefix(old_depth, depth, line=line,
                                            address=address)
        # new_line = new_line.replace(',open,',',closed,')
        print(new_line)
        Lines2[i] = new_line

    file1.close()

    file2 = open(input_filename+'_NUMBERED.txt', 'w')
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