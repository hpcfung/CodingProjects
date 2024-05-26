import re

if __name__ == "__main__":
    """
    https://www.onlineocr.net/
    """
    input_filename = 'finance'
    file1 = open(input_filename + '.txt', 'r', encoding="utf8")
    Lines = file1.readlines()
    Lines_write = []

    for i, line in enumerate(Lines):
        print(repr(line))
        if line == '\n':
            print('NO LINE')
            continue

        newline = re.sub(r'\s([0-9](\.[0-9])+)', r'\n\1', line)

        Lines_write.append(newline)
        print(repr(newline))

    file1.close()

    file2 = open(input_filename+'_pre.txt', 'w', encoding="utf8")
    file2.writelines(Lines_write)
    file2.close()