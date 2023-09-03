from pytesseract import Output
import pytesseract, cv2, sys, pickle, os, time
from multiprocessing import Pool


def visualize(image,results,k):
    min_conf = 10
    bookname = 'nand'
    print_to_terminal = False

    # loop over each of the individual text localizations
    for i in range(0, len(results["text"])):
        # extract the bounding box coordinates of the text region from
        # the current result
        x = results["left"][i]
        y = results["top"][i]
        w = results["width"][i]
        h = results["height"][i]
        # extract the OCR text itself along with the confidence of the
        # text localization
        text = results["text"][i]
        conf = int(results["conf"][i])

        # filter out weak confidence text localizations
        if conf > min_conf:
            if print_to_terminal:
                # display the confidence and text to our terminal
                print("Confidence: {}".format(conf))
                print("Text: {}".format(text))
                print(f"{(x, y)}")
                print("")

        # strip out non-ASCII text so we can draw the text on the image
        # using OpenCV, then draw a bounding box around the text along
        # with the text itself
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 2)  # fontScale = 1.2, thickness = 3

    # show the output image
    # cv2.imshow("Image", image)
    cv2.imwrite('annotated/output_image'+str(k)+'.jpg', image)
    cv2.waitKey(0)

    with open('dict/'+bookname+str(k)+'.pkl', 'wb') as f:
        pickle.dump(results, f)

def scan_page(k):
    prename = 'Tom Hayes_ Paul Horowitz - Learning the Art of Electronics_ A Hands-On Lab Course-Cambridge University Press (2016)' # breaks if moved to main
    print(f"page {k}")
    page_num = str(k).zfill(4)
    img_path = 'ilovepdf_pages-to-jpg/'+prename+'_page-'+page_num+'.jpg'
    # page_num = str(k-1) # for the 2nd conversion software, zero-based?
    # img_path = 'ilovepdf_pages-to-jpg/' + prename + '-' + page_num + '.jpg' # which conversion software is this?

    # debugging
    # print(img_path)
    # return

    image = cv2.imread(img_path)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pytesseract.image_to_data(rgb, output_type=Output.DICT)
    # print(results)

    visualize(image=image,results=results,k=k)

if __name__ == "__main__":
    """
    Behavior: Given a book of jpgs, runs OCR, stores words and their positions in {bookname}.pkl files in dict
    
    1. Clear annotated, dict directories
    2. Change prename in scan_page
    3. Change img_path in scan_page depending on the conversion software?
    4. Set min_page, max_page for the range of pages to be scanned
       - literal page number, not zero-based
       - as many as possible? it's ok to cover more than is needed in the next step (no need to go back and forth)
    5. Change bookname in visualize to a shortened version of the name of the book
       - same name to be fed into prepos
    
    
    Change name into sth shorter before feeding into i love pdf?
    process_time does not work (only counts time for each task/process?)
    CPU 100% but still kind of slow: maybe IO bound not compute bound? possibility for further optimization
    
    in any pdf reader, all pages basically visible instantaneously
    try: Java Apache PDFBox?
    """
    start = time.process_time()

    min_page = 29
    max_page = 1155

    with Pool() as p:
        p.map(scan_page, list(range(min_page,max_page+1)))

    print(f'init scan completed   time = {time.process_time()-start}')
