import sys, re, pickle, scraping, statistics
from thefuzz import fuzz


# these functions: most likely need to be modified depending on book
# functions in scraping.py: basically stable
def is_title(results, idx, text, conf, x, y):
    """
    From the text and position of the word, deduce if the word is the beginning of a title
    Works if the row is eg 1.2.3 NAME OF SECTION
    """
    conditions = [re.search(r'[a-zA-Z0-9]+\.[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*', text),
                  y > 75,  # not header
                  idx == 0 or results["text"][idx - 1] != 'Figure']  # only evaluate 2nd con if idx != 0?
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
    return True # all(conditions)


def not_title(title):
    main, space, page = title.rpartition(' ')
    return page.isdigit()  # content page: section title ends in page number

class ScanPage:
    """
    Stores text, positions, and height of lines on the page
    """

    def __init__(self, k):
        self.page_num = str(k)
        with open('dict/' + bookname + self.page_num + '.pkl', 'rb') as f:
            self.results = pickle.load(f)  # structure of results: see docstring of scraping.page_info_dump

        self.lines = [] # elements: text, leftmost x, y, font size
        self.ub = -10 # upper bound
        self.lb = -5
        for i in range(0, len(self.results["text"])):
            text, conf, x, y = scraping.get_word_attributes(results=self.results, idx=i)
            width = self.results['width'][i]
            height = self.results['height'][i]
            if re.fullmatch(r'( )*', text) or conf < 0:  # not a proper word
                continue
            font_size = self.get_font_size(text, width, height)
            if self.lines == []: # first word
                self.initialize_newline(text,x,y,font_size)
                continue
            if y < self.lb or y > self.ub: # too far to be in same line
                self.finalize_line()
                self.initialize_newline(text,x,y,font_size)
                continue
            # same line
            self.lines[-1][0] = self.lines[-1][0] + ' ' + text
            # assume OCR goes from left to right so no need to update leftmost x
            self.lines[-1][2].append(y)
            self.update_bounds(y)
            self.lines[-1][3].append(font_size)
        if self.lines != []:
            self.finalize_line()

    def initialize_newline(self,text,x,y,font_size):
        self.lines.append([text, x, [y], [font_size]])
        self.update_bounds(y)

    def update_bounds(self,y):
        self.ub = y + line_space
        self.lb = y - line_space

    def finalize_line(self):
        # set averages
        self.lines[-1][2] = statistics.fmean(self.lines[-1][2])
        self.lines[-1][3] = statistics.fmean(self.lines[-1][3])
        if debug:
            print(self.lines[-1])
        if not self.is_line():
            self.lines.pop()

    def is_line(self):
        return self.lines[-1][3] > 28 # 30

    def get_font_size(self,text,width,height):
        """
        Get font size from max height or avg height: both unreliable
        """
        weighted_width = 1.4*len(re.findall(r'[A-Z234567890]',text))\
                         +len(re.findall(r'[^A-Z234567890]',text))
        vert_spread = 0.5
        if re.search(r'[A-Z0-9bdfhklt]', text):
            vert_spread += 0.5
        if re.search(r'[gjpqy]', text):
            vert_spread += 0.5

        # print(text,width,height,width/weighted_width+height/vert_spread)
        # print(weighted_width,vert_spread, width/weighted_width, height/vert_spread)
        # len(text)
        return width/weighted_width+height/vert_spread

def get_title(original_target_title):
    Exceptions = ['Reactions to This Positive Story 39\n',
                  'Personal Mini-Experiments: What You Want to Experience 45\n',
                  'Chapter 2 Eastern and Western Perspectives on Positive Psychology: How “ME + WE = US” Might Bridge the Gap\n',
                  'Personal Mini-Experiments: Getting and Giving Help 83\n',
                  'Chapter 6 The Principles of Pleasure: Understanding Positive Affect, Positive Emotions, Happiness, and Well-Being 219\n',
                  'Chapter 7 Making the Most of Emotional Experiences: Emotion-Focused Coping, Emotional Intelligence, Socioemotional Selectivity, and Emotional Storytelling 267\n',
                  'Living With Mindfulness: The Women’s Heart Foundation 440\n',
                  'Appendix A: Effective Secondary Preventions (Psychotherapies) for Adult Problems\n',
                  'Chapter 15 Positive Schooling and Good Work: The Psychology of Gainful Employment and the Education That Gets Us There 657\n',
                  'Part VIII Finding Strengths in Others: Embodying Strengths in Everyday Life 732\n']

    global current_pointer
    target_title = original_target_title.strip('\t\n') # leading \t and trailing \n
    print(f"target: {repr(target_title)}")
    max_sim = -1
    max_title = ''
    max_pointer = current_pointer
    for pointer, possible_title in enumerate(all_titles):
        if pointer < current_pointer:
            continue
        if target_title in possible_title:
            current_pointer = pointer + 1
            print(current_pointer)
            print(f"match: {repr(possible_title)}")
            return reconstruct_title(original_target_title,possible_title)
        if target_title.startswith('Personal Mini-Experiments') and 'Personal Mini-Experiments' in possible_title:
            current_pointer = pointer + 1
            print(current_pointer)
            print(f"Personal Mini-Experiments match: {repr(possible_title)}")
            return reconstruct_title(original_target_title, possible_title)
        for exc in Exceptions:
            if target_title in exc:
                print(f"Exception: {repr(exc)}")
                return exc
        similar = fuzz.ratio(target_title, possible_title)
        if verbose:
            print(repr(possible_title), similar)
        if similar > max_sim:
            max_sim = similar
            max_title = possible_title
            max_pointer = pointer
    print(f'Sim score only: {repr(max_title)} score {max_sim}')
    if max_sim < 70: # possible: no matches, need to put in Exceptions
        print(f"Warning: {repr(target_title)}")
        sys.exit()
    current_pointer = max_pointer + 1
    return reconstruct_title(original_target_title,max_title)

def reconstruct_title(title_name, OCR_title):
    page_num = OCR_title.rpartition(" ")[2]
    return title_name.strip('\n') + ' ' + page_num


if __name__ == "__main__":
    """
    New:
    data centric: eventually end up with a list of lines
    other lists (same length): leftmost x position, height (proxy for font), etc
    
    Algo: fix line_space, go to next word, decide if new line
    
    therefore, code (constructor) moves pointer between words
    
    Problem: OCR content page
    if pdf already has OCR text, copy content page?
    use this OCR to automatically tab?
    
    Implement multiline parsing? into one title
    
    Whatever solution: will need to deal with exceptions, modify code, case by case
    
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


    """
    bookname = 'pos'

    line_space = 13  # narrow = better? this controls bounds around a line, should be (much) smaller than line spacing

    min_page = 21 # 21
    max_page = 1089 # 1089

    debug = False
    save_page_num = True
    verbose = True

    all_titles = []
    for k in range(min_page, max_page + 1):
        print(f"page {k}")
        page = ScanPage(k)
        for line in page.lines:
            if verbose:
                print(line)
            line_text, x, y = line[0], line[1], line[2]
            # if x < 135 or y > 1255:
            #     continue
            # for j in range(round((x-165)/50)):
            #     line_text = '\t' + line_text
            if save_page_num:
                line_text = line_text + ' ' + str(k)
            all_titles.append(line_text+'\n')

    file1 = open(bookname + '.txt', 'w', encoding="utf8")
    file1.writelines(all_titles)
    file1.close()

    file2 = open('copy_content' + '.txt', 'r', encoding="utf8")
    actual_titles = file2.readlines()
    file2.close()

    print()
    current_pointer = 0
    final_titles = []
    # for i in range(10):
    #     current_title = get_title(target_title=actual_titles[i])
    #     print(f"final: {repr(current_title)}")
    #     print()
    #     final_titles.append(current_title)
    for target_title in actual_titles:
        current_title = get_title(target_title)
        print(f"final: {repr(current_title)}")
        print()
        final_titles.append(current_title)

    file3 = open('parsed_titles.txt', 'w', encoding="utf8")
    file3.writelines(final_titles)
    file3.close()




