min_conf = 1

def page_info_dump(results):
    """
    For debugging: given a .pkl file, prints each word and its location

    results: dictionary
    - keys: for our purposes, we only need: 'text', 'conf', 'left', 'top'
    - values: array, each element = attribute of a word
    """
    print(results)
    # print(results.keys())

    for i in range(0, len(results["text"])):
        text = results["text"][i] # text of ith word
        conf = int(results["conf"][i])
        x = results["left"][i]
        y = results["top"][i]
        if conf > min_conf:
            print("Confidence: {}".format(conf))
            print("Text: {}".format(text))
            print(f"{(x, y)}")
            print("")

def double_check_is_title(results,i,lb,ub):
    """

    Has access to all words, not just current word, as in is_title (function in cv_test.py)
    """
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
            clash_words = ['figure', 'Figure']
            if any(clash_word in word for clash_word in clash_words):
                is_title = False
                print('not title: figure X.Y cut in half in line split')
        break  # we know is title or not by looking at first non empty word

    return is_title

def get_word_attributes(results,idx):
    """
    text, conf, x, y
    """
    return results["text"][idx], int(results["conf"][idx]), results["left"][idx], results["top"][idx]

def remove_end_dot(text):
    """
    OCR has a tendency: 1N.1.3 becomes 1N.1.3., so we need to remove the dot
    """
    if text[-1] == '.':
        return text[0:-1]
    else:
        return text