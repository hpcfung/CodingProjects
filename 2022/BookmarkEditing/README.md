# Usage
- Put the `.txt` file generated by https://sourceforge.net/projects/jpdfbookmarks/ into the same folder as `formatter_test.py`
- The script generates a new `.txt` file with the chapter/section numbers added
- Note: for best effects, one should modify the code to suit the particular pdf
  - eg to avoid adding section numbers to "Preface", add it to `avoid_these`
  - also the script ignores all bookmarks after "Bibliography"
- Toggle `omit_deep_index` and `if depth > 3:`
- note: `Index` might show up in a section title, so use eg `Index/571` in `skip_all`
# text to bk
- skips empty lines automatically (ie `\n`)

# computer vision
https://pyimagesearch.com/2020/05/25/tesseract-ocr-text-localization-and-detection/

order of results = lexicographical order (x first, then y)

class: feature engineering

each book: choose which features to use
