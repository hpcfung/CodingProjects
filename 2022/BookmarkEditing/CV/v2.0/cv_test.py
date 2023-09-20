# https://pyimagesearch.com/2020/05/25/tesseract-ocr-text-localization-and-detection/
import sys, re, pickle, scraping

# these functions: most likely need to be modified depending on book
# functions in scraping.py: basically stable
def is_title(results,idx,text,conf,x,y):
    """
    From the text and position of the word, deduce if the word is the beginning of a title
    Works if the row is eg 1.2.3 NAME OF SECTION
    is title only if satisfies all conditions
    """
    conditions = [re.search(r'[a-zA-Z0-9]+\.[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*', text),
                  y > 75, # not header
                  idx == 0 or results["text"][idx-1] != 'Figure'] # only evaluate 2nd con if idx != 0?
    # re.search(r'[0-9]+\.[0-9]+(\.[0-9]+)*', text) # 1.2, 1.2.3, etc; even 10.10?
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

def not_title(title):
    main, space, page = title.rpartition(' ')
    return page.isdigit() # content page: section title ends in page number

def scan_page(k):
    """
    Given page number k, adds all titles found on page k to add_titles

    Strategy: quick check is_title once, then double_check_is_title using line spacing
    No need to filter every false positive (though useful if many of the same case, such that easy to filter)
    Important part: just make sure no actual section is missing

    alternate strat: split all text one one page into rows
    ignore A.B.C entirely
    """
    global all_titles

    page_num = str(k)
    with open('dict/'+bookname+page_num+'.pkl', 'rb') as f:
        results = pickle.load(f) # structure of results: see docstring of scraping.page_info_dump

    if debug:
        scraping.page_info_dump(results)
        sys.exit()

    last_line = -100
    for i in range(0, len(results["text"])):
        text, conf, x, y = scraping.get_word_attributes(results=results,idx=i)
        if re.fullmatch(r'( )*', text) or conf < 0:
            continue

        # Check if chapter; y = 45; not start or end w/ digits; 56 to 304
        if y < 85:
            ub = y + line_space  # upper bound
            lb = y - line_space
            if lb < last_line and last_line < ub: # this line has been processed
                continue
            last_line = y

            title = scraping.remove_end_dot(text)
            if scraping.double_check_is_title(results=results, i=i, lb=lb, ub=ub):
                print('is title\n')
                print('%' * 30)
                print('Remainder of title:')
            else:
                print('not_title')
                continue

            j = i + 1
            while j < len(results["text"]):  # repeat until last word
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
            main, space, page = title.rpartition(' ')
            if page.isdigit():
                continue
            main, space, rest = title.partition(' ')
            if main.isdigit():
                continue
            all_titles.append(title + ' ' + page_num + '\n')
            continue

        if is_title(results=results,idx=i,text=text,conf=conf,x=x,y=y): # 2nd word in same row: is_title is False
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
            if not_title(title):
                continue
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
    3. after: play with settings for one page, then one ch until 
    
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

    line_space = 15 # narrow = better? this controls bounds around a line, should be (much) smaller than line spacing

    min_page = 29 # 31
    max_page = 1155

    debug = False

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
