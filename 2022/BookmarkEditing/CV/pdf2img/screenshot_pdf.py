import pyautogui, time, sys

def get_scr_region(x1,y1,x2,y2):
    """
    Given top left and bottom right corner of the region
    Returns left, top, width, and height
    As used in region argument of pyautogui.screenshot
    """
    return x1, y1, x2-x1, y2-y1

def take_page_image(page_num):
    """

    .jpg img quality too bad? bad for OCR?
    """
    pyautogui.screenshot('imgs/'+str(page_num)+'.png',
                              region=get_scr_region(x1, y1, x2, y2))
    pyautogui.press('right')


if __name__ == "__main__":
    """
    Create imgs folder
    Set chrome tab to pdf
    Select Fit to page
    Make sure pdf scrolled to the top
    Use mouse_pos.py to find x1,y1,x2,y2
    
    Rotate counterclockwise
    """
    min_page = 1
    max_page = 10

    (x1,y1) = (266, 112)
    (x2,y2) = (1620, 1072)

    # pyautogui.moveTo(520, 1041)
    pyautogui.click(520, 1041)
    pyautogui.press('f11')
    time.sleep(6) # going to full scr takes time 0.1; 6s for exit full scr to disappear
    start_time = time.time()
    for page_num in range(min_page,max_page+1):
        take_page_image(page_num)
    end_time = time.time()
    print(f"Total time elapsed: {end_time - start_time}")
    print(f"Average time per page: {(end_time-start_time)/(max_page-min_page+1)}")