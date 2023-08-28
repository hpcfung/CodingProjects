import sys, re


if __name__ == "__main__":
    """
    TO DO: add feature - check page number is numeric (so that X need to run format2 and find error there then go back here)
    
    Purpose: preprocess text from content page (add Ch., p.)
    
    1. change input_filename
    2. Toggle add_ch and remove_dots
       - If add_ch: change items to skip over inside "if add_ch:" (ie don't add Ch. to these)
          - note that automatically skips eg A.2 even without explicitly skip these
       - remove_dots: adjust regex (eg .... vs . . . .)
    3. Toggle skip_after_word; if set to true, also change skip_word
       - Stops adding Ch. after skip_word
       
    Known issues: cannot deal with microsoft fancy '
    
    Assumptions
    - assumes eg 1.1 Spontaneously broken symmetry 1, section name and page number separated by one space
    - automatically adds Ch. to every row unless specified not to
    """
    add_ch = False
    remove_dots = False
    skip_after_word = False
    skip_word = 'Appendices'

    input_filename = 'Zargham'
    file1 = open(input_filename + '.txt', 'r')
    Lines = file1.readlines()
    Lines_write = []

    no_more_ch = False

    for i, line in enumerate(Lines):
        print(repr(line))
        if line == '\n':
            print('NO LINE')
        else:
            newline = line
            if remove_dots:
                # newline = re.sub(r'\s*\.\.+\s*', r' ', newline) # ' .... '
                newline = re.sub(r'\s*\.\s(\.\s)+\s*', r' ', newline) # '. . . '

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

    file2 = open(input_filename+'_prepos.txt', 'w')
    file2.writelines(Lines_write)
    file2.close()
