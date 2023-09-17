from PyPDF2 import PdfReader
import re

def is_near(x,y, margins=5):
    return abs(x-y) < margins

def preprocessing(text):
    return text.replace('\u2003', ' ').replace('\u2002', ' ')
    # if text == '  ':
    #     text = ' '

def visitor_body(text, cm, tm, fontDict, fontSize):
    global is_even
    global tmp_line
    global Lines_write
    y = tm[5]
    x = tm[4]
    text = preprocessing(text)
    # if text != '\n' and len(parts) > 3 and 'Chapter' not in parts[-4]:
    #     if is_even:
    #         one_tab_x_pos = 158.4
    #         two_tab_x_pos = 175
    #     else:
    #         one_tab_x_pos = 236.4
    #         two_tab_x_pos = 253
    #     if is_near(x,one_tab_x_pos):
    #         text = '_TAB'+ text
    #     if is_near(x,two_tab_x_pos):
    #         text = '_TAB_TAB' + text

    if save_all_text:
        parts.append(text)
    print(tm, repr(text), fontSize) # debug info
    # print(fontDict, fontSize)

    # if y > 50 and y < 720:
    #     parts.append(text)
    # if fontSize > 12.0:
    #     tmp_line = text + tmp_line
    # elif tmp_line != '':
    #     Lines_write.append(tmp_line + ' ' + str(page_num))
    #     tmp_line = ''
    if re.search(r'^[0-9]+\.[0-9]+(\.[0-9]+)*', text): # fontSize > 12.0 # r'[a-zA-Z0-9]+\.[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*'
        if text.endswith('\n'):
            tmp_line = tmp_line + text[:-1]
        else:
            Lines_write.append(text + ' ' + str(page_num) + '\n')
    elif tmp_line != '':
        if not text.endswith('\n'): # section title 3 or more lines?
            Lines_write.append(tmp_line + ' ' + text + ' ' + str(page_num) + '\n')
            tmp_line = ''




def scan_page(page_num):
    page = reader.pages[page_num-1]  # zero based, so page num - 1;
    # print(page.extract_text())

    # print('ORIGINAL EXTRACT')
    # print(page.extract_text(visitor_text=visitor_body))
    global is_even
    global tmp_line
    tmp_line = ''
    if page_num % 2 == 0:
        is_even = True
    else:
        is_even = False
    page.extract_text(visitor_text=visitor_body)

if __name__ == "__main__":
    """
    Given a PDF with text, extracts titles (eg content page or main text)
    1. Change input_filename
    
    Find pos/font size on 1 page
    1. Set min_page and max_page to that page
    2. Toggle save_all_text, true when scraping content page
    - if x, y pos are not consistent, then it is not possible to proceed
    
    3. Even and odd pages might have different positions
    
    """
    input_filename = 'manu'
    min_page = 18 # actual page num
    max_page = 587 # 587
    save_all_text = False

    reader = PdfReader(input_filename+".pdf")

    Lines_write = []
    parts = []
    is_even = None
    tmp_line = None
    for page_num in range(min_page,max_page+1):
        scan_page(page_num)
    text_body = "".join(parts)

    print('PROCESSED TEXT')
    print(text_body)

    if save_all_text:
        file1 = open(input_filename+'.txt', 'w', encoding="utf8")
        file1.writelines(text_body)
        file1.close()
    else:
        file2 = open(input_filename + '.txt', 'w', encoding="utf8")
        file2.writelines(Lines_write)
        file2.close()

# https://pypdf2.readthedocs.io/en/3.0.0/user/extract-text.html

# import PyPDF2
# print(PyPDF2.__version__)
