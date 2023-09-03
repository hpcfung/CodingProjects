# https://pyimagesearch.com/2020/05/25/tesseract-ocr-text-localization-and-detection/
import sys, re, pickle, scraping

def is_title(text,conf,x,y):
    """
    From the text and position of the word, deduce if the word is the beginning of a title
    Works if the row is eg 1.2.3 NAME OF SECTION
    """
    conditions = [re.search(r'[0-9]+\.[0-9]+(\.[0-9]+)*', text), # 1.2, 1.2.3, etc; what about 10.10?
                  y > 75]
    # if re.search(r'[AB0-9]+\.[0-9]+(\.[0-9]+)*', text):  # 1.2, 1.2.3, etc; appendix

    # For nano
    # if 180 < y and y < 195:
    #     print('not_title: is header')
    #     continue

    # For Wen: Figure also of the form Fig X.Y
    # if '(' in text or ')' in text:
    #     print('not title: contains ( or )')
    #     continue
    return all(conditions)

def scan_page(k):
    """
    Given page number k, adds all titles found on page k to add_titles

    Strategy: quick check is_title once, then double_check_is_title using line spacing
    """
    global all_titles

    page_num = str(k)
    with open('dict/'+bookname+page_num+'.pkl', 'rb') as f:
        results = pickle.load(f) # structure of results: see docstring of scraping.page_info_dump

    if debug:
        scraping.page_info_dump(results)
        sys.exit()

    for i in range(0, len(results["text"])):
        text, conf, x, y = scraping.get_word_attributes(results=results,idx=i)

        # TODO: check if chapter
        if is_title(text=text,conf=conf,x=x,y=y):
            print('-' * 50)
            print("Confidence: {}".format(conf))
            print("Title candidate: {}".format(text))
            print(f"{(x, y)}")
            print("")

            title = scraping.remove_end_dot(text)

            ub = y + line_space  # upper bound
            lb = y - line_space

            if scraping.double_check_is_title(results=results,i=i,lb=lb,ub=ub):
                print('is title\n')
                print('%' * 30)
                print('Remainder of title:')
            else:
                print('not_title')
                continue

            j = i + 1
            while j < len(results["text"]): # repeat until last word
                text, conf, x, y = scraping.get_word_attributes(results=results, idx=j)

                if lb < y and y < ub:
                    print("Confidence: {}".format(conf))
                    print("Text: {}".format(text))
                    print(f"{(x, y)}")
                    print("")
                    title = title + ' ' + text
                else:
                    break
                j += 1

            all_titles.append(title + ' ' + page_num + '\n')

if __name__ == "__main__":
    """
    Note: all pages exact, not zero based
    1. Change bookname to the one used in init_scan_parallel.py
    
    Setup
    1. Set debug to True
    2. one page, page_info_dump; min_page, max_page to one page
    - get header pos (if any)
    - get line spacing
    
    Test
    1. Set debug to False
    2. Change conditions in is_title
    3. after: play with settings for one ch until 
    
    Run for entire book
    
    
    Organize into better software architecture: meaningful groupings into classes, functions
    
    NEXT time
    change 180-190 rule
    change reg ex
    
    known issues: page number = pdf page number
    also, usually only give sec and subsec, need to merge w/ ch.
    bad with equations
    
    
    Use ChatGPT for postprocessing? eg consistent OCR errors, 1S becomes 18
    
    """
    bookname = 'nand'

    line_space = 20 # narrow = better? this controls bounds around a line, should be (much) smaller than line spacing

    min_page = 32
    max_page = 32

    debug = True

    all_titles = []
    for k in range(min_page,max_page+1):
        print(f"page {k}")
        scan_page(k)

    file = open(bookname + '.txt', 'w')
    file.writelines(all_titles)
    file.close()




# strategy: just use OCR, regex X.Y.Z
# x pos left most? bcuz eq label right most
# but some eq ref also left
# then, regex, no brakets?
# save results to file (takes most time?), fine tune parsing in subsequent testing

# or, go back one word before title, see if belong to same line

# protcol: test code on 1 ch first, if works well, then whole book

# incidentally, also skips eg Exercise 2.3, as it should