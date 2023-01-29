# https://pyimagesearch.com/2020/05/25/tesseract-ocr-text-localization-and-detection/
from pytesseract import Output
import pytesseract, cv2, sys, re, pickle


def scan_page(k):
    global all_titles

    page_num = str(k)
    with open('dict/Wen'+page_num+'.pkl', 'rb') as f:
        results = pickle.load(f)

    for i in range(0, len(results["text"])):
        text = results["text"][i]
        if re.search(r'[0-9]+\.[0-9]+(\.[0-9]+)*', text):
            conf = int(results["conf"][i])
            x = results["left"][i]
            y = results["top"][i]
            print("Confidence: {}".format(conf))
            print("Text: {}".format(text))
            print(f"{(x, y)}")
            print("")

            if '(' in text or ')' in text:
                print('not title: contains ( or )')
                continue

            title = text

            j = i + 1
            ub = y + line_space  # upper bound
            lb = y - line_space

            h = i - 1
            not_title = False
            # combo = 0
            while h >= 0:
                y = results["top"][h]
                print(f"current y = {y}, lb = {lb}, ub = {ub}") #
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
                if lb < y and y < ub:
                    not_title = True
                break # we know is title or not by looking at first non empty word

            if not_title:
                print('not_title\n')
                continue
            else:
                print('is title')

            while True:
                if j == len(results["text"]):
                    break

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
                    all_titles.append(title+' '+page_num+'\n')
                    break

                j += 1

if __name__ == "__main__":
    """
    
    known issues: page number = pdf page number
    also, usually only give sec and subsec, need to merge w/ ch.
    """

    min_conf = 50
    line_space = 10
    bookname = 'Wen'
    min_page = 16
    max_page = 511

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