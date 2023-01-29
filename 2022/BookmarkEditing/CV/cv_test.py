# https://pyimagesearch.com/2020/05/25/tesseract-ocr-text-localization-and-detection/
from pytesseract import Output
import pytesseract, cv2, sys, re, pickle

def page_info_dump(results):
    print(results)

    for i in range(0, len(results["text"])):
        text = results["text"][i]
        conf = int(results["conf"][i])
        x = results["left"][i]
        y = results["top"][i]
        print("Confidence: {}".format(conf))
        print("Text: {}".format(text))
        print(f"{(x, y)}")
        print("")

def double_check_if_title(results,i,lb,ub):
    h = i - 1
    is_title = True
    # combo = 0
    # go back in words until reach previous line
    while h >= 0:
        y = results["top"][h]
        print(f"current y = {y}, lb = {lb}, ub = {ub}")  #
        word = results["text"][h]
        conf = results["conf"][h]
        print("Confidence: {}".format(conf))
        print(repr(word))
        print(f"h = {h}")
        h -= 1
        if word == '':
            continue
        # elif conf < min_conf:
        #     combo += 1
        #     if combo > 0: # probably an equation # 2
        #         not_title = True
        #         break
        #     continue
        if lb < y and y < ub: # first non trivial word is in same line; ie initial word not leftmost of line
            is_title = False
        else:
            if 'figure' in word:
                is_title = False
                print('not title: figure X.Y cut in half in line split')
        break  # we know is title or not by looking at first non empty word

    return is_title

def remove_dots(text):
    if text[-1] == '.':
        return text[0:-1]
    else:
        return text

def scan_page(k):
    global all_titles

    page_num = str(k)
    with open('dict/'+bookname+page_num+'.pkl', 'rb') as f:
        results = pickle.load(f)

    # page_info_dump(results)

    for i in range(0, len(results["text"])):

        text = results["text"][i]
        if re.search(r'[0-9]+\.[0-9]+(\.[0-9]+)*', text):  # 1.2, 1.2.3, etc
            print('-' * 50)
            conf = int(results["conf"][i])
            x = results["left"][i]
            y = results["top"][i]
            print("Confidence: {}".format(conf))
            print("Title candidate: {}".format(text))
            print(f"{(x, y)}")
            print("")

            # For Wen: Figure also of the form Fig X.Y
            # if '(' in text or ')' in text:
            #     print('not title: contains ( or )')
            #     continue

            title = remove_dots(text)

            ub = y + line_space  # upper bound
            lb = y - line_space

            if double_check_if_title(results=results,i=i,lb=lb,ub=ub):
                print('is title\n')
                print('%' * 30)
                print('Remainder of title:')
            else:
                print('not_title')
                continue

            j = i + 1
            while j < len(results["text"]): # repeat until last word
                text = results["text"][j]
                x = results["left"][j]
                y = results["top"][j]
                if lb < y and y < ub:
                    conf = int(results["conf"][i])
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
    
    known issues: page number = pdf page number
    also, usually only give sec and subsec, need to merge w/ ch.
    """

    min_conf = 5
    line_space = 10 # narrow = better?
    bookname = 'nand'
    min_page = 92
    max_page = 92
    # Ch.1: 33, 58
    # full book: 33, 409
    # 92

    # print(pytesseract)

    # img_path = 'ilovepdf_pages-to-jpg/book_page-0029.jpg'
    # 'otest.png' # 'output/29.jpg' # '500_1.jpg' # 'ilovepdf_pages-to-jpg/book_page-0029.jpg'

    # scan_page(25)
    #
    # sys.exit()
    all_titles = []
    for k in range(min_page,max_page+1): # 16,100
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
