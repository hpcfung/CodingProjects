import sys

if __name__ == "__main__":
    """
    Purpose: OCR content page, title and page number on separate entries; merge them
    
    
    assume all title before page number; no title already contains page number
    1. Change input_filename
    2. Add _PAGE before pages
    """
    input_filename = 'Euclid1'
    input_file = open(input_filename + '.txt', 'r')
    read_lines = input_file.readlines()

    write_lines = []
    write_idx = 0
    for i, line in enumerate(read_lines):
        print(repr(line))

        if line == '\n':
            print('NO LINE')
            continue
        page = line.rpartition(' ')[-1]
        if page[-1] == '\n':
            page = page[:-1]

        if page.isdecimal():
            write_lines[write_idx] = write_lines[write_idx][:-1] + f' {page}\n'
            print(repr('Edit: ' + write_lines[write_idx]))
            write_idx += 1
        else:
            write_lines.append(line)

    input_file.close()
    if write_idx != len(write_lines):
        print(f'Warning: num pages ({write_idx}) fewer than num titles {len(write_lines)}')
        sys.exit()
    else:
        print(f'{write_idx} titles added pages')

    output_file = open(input_filename + '_MERGED.txt', 'w')
    output_file.writelines(write_lines)
    output_file.close()


