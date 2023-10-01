



LLM cannot output `.docx` directly?

### TODO
1. Understand `.docx` format
2. Figure out how to read/write `.docx` with code

### Strategies
#### 1
End to end LLM chatbot

#### 2
For each set of questions from an author, strip it of formats (eg copy from word, paste at ChatGPT), then use ChatGPT to convert it to the template format. Finally format everything manually in Word.

#### 3
Same as 2 but the formatting is done by code (generate `.docx` from some sort of markdown/latex like language).

Identify where a Q begins and end by LLM, code, or manually.

Note that the Qs as given are not numbered?

eg manually insert sth like _2153 token at page end or at end of MCQ, program automatically splits into segments

feeds each segment into LLM; clean typos, then insert latex like macros

#### 4
Do the whole thing in regex

Some sort of beautify code operation.
