import sys, re

def preprocessing(line):
    if remove_dots:
        # line = re.sub(r'\s*\.\.+\s*', r' ', line) # ' .... '
        line = re.sub(r'\s*\.\s(\.\s)+\s*', r' ', line)  # '. . . '

    return line.replace('\u2003', ' ').replace('\u2002', ' ')

def line_is_incomplete(line):
    if line.startswith('CHAPTER'): # in some books, CHAPTER and chapter title are always on different lines
        return True

    main, space, page = line.rpartition(' ')
    if page.endswith('\n'):
        page = page[:-1]  # eg if page is '123\n'
    if not page.isdigit(): # if not only a page num
        return True
    return False


if __name__ == "__main__":
    """
    TO DO: add feature - check page number is numeric (so that X need to run format2 and find error there then go back here)
    
    Purpose: preprocess text from content page (add Ch., p.)
    
    1. Change input_filename
    2. Toggle add_ch and remove_dots
       - If add_ch: change items to skip over inside "if add_ch:" (ie don't add Ch. to these)
          - note that automatically skips eg A.2 even without explicitly skip these
       - remove_dots: adjust regex (eg .... vs . . . .)
    3. Toggle skip_after_word; if set to true, also change skip_word
       - Stops adding Ch. after skip_word
    4. Change 'CHAPTER' in if line.startswith('CHAPTER')
    5. Change preprocessing if necessary
       
    Known issues: cannot deal with microsoft fancy '
    
    Assumptions
    - assumes eg 1.1 Spontaneously broken symmetry 1, section name and page number separated by one space
    - automatically adds Ch. to every row unless specified not to
    - sometimes, one title is split into several lines; automatically joins them 
    """
    add_ch = False
    remove_dots = False
    skip_after_word = False
    skip_word = 'Appendices'

    input_filename = 'org'
    file1 = open(input_filename + '.txt', 'r', encoding="utf8")
    Lines = file1.readlines()
    Lines_write = []

    no_more_ch = False
    last_line = ''

    for i, line in enumerate(Lines):
        print(repr(line))
        if line == '\n':
            print('NO LINE')
            continue

        newline = preprocessing(line)

        if line_is_incomplete(line=newline):
            if last_line == '':
                last_line = newline[:-1]
            else:
                last_line = last_line + ' ' + newline[:-1]
            continue
        else:
            if last_line != '':
                newline = last_line + ' ' + newline
                last_line = ''

        main, space, page = newline.rpartition(' ') # split the string at the last occurrence of ' '
        newline = main+space+'p.'+page
        if page.endswith('\n'):
            page = page[:-1] # eg if page is '123\n'
        if not page.isdigit():
            print(f"Warning, incorrect page number in: {newline}")
            sys.exit()

        if add_ch:
            ch, space, rest = newline.partition(' ')
            skip = False
            # don't add Ch. to these; note: should only be one word (no space)
            # otherwise removed in partition
            if skip_after_word and (skip_word in ch):
                no_more_ch = True
            if no_more_ch:
                skip = True
            if ch in ['Problems','References','Index','Summary','Problem']: # 'Acronyms', 'Glossary',  first word before space
                skip = True
            if ch.count('.') == 0 and not skip:
                newline = 'Ch.'+newline

        Lines_write.append(newline)
        print(repr(newline))

    file1.close()

    file2 = open(input_filename+'_prepos.txt', 'w', encoding="utf8")
    file2.writelines(Lines_write)
    file2.close()
