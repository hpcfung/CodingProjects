import sys

if __name__ == "__main__":
    """
    assume pages not preceded by space
    1. Change input_filename
    2. Add _PAGE before pages
    """
    input_filename = 'tmp'
    input_file = open(input_filename + '.txt', 'r')
    read_lines = input_file.readlines()
    written_lines = []

    line_is_title = True
    num_pages = 0
    for i, line in enumerate(read_lines):
        print(repr(line))
        if line == '\n':
            print('NO LINE')
            continue
        if line.startswith('_PAGE'):
            line_is_title = False
            continue

        if line_is_title:
            written_lines.append(line)
        else: # is page
            if line.endswith('\n'):
                line = line[:-1]
            written_lines[num_pages] = written_lines[num_pages][:-1] + ' ' + line + '\n'
            print(repr(written_lines[num_pages]))
            num_pages += 1

    input_file.close()
    if num_pages != len(written_lines):
        print(f'Warning: num pages ({num_pages}) fewer than num titles {len(written_lines)}')
        sys.exit()
    else:
        print(f'{num_pages} titles added pages')

    output_file = open(input_filename + '_PAGE_ADDED.txt', 'w')
    output_file.writelines(written_lines)
    output_file.close()


