from cs50 import get_string

words = 1
letters = 0
sentences = 0

text = get_string("Text: ")

for i in range(len(text)):
    if text[i] == "." or text[i] == "!" or text[i] == "?" or text[i] == ":":
        sentences += 1
    
    if text[i-1] == " " and text[i].isalpha():
        words += 1
    
    if text[i].isalpha():
        letters += 1
        
index = round(0.0588 * (letters * 100 / words) - 0.296 * (sentences * 100 / words) - 15.8)

if index < 1:
    print("Before Grade 1")
    
elif index > 16:
    print("Grade 16+")
    
else:
    print(f"Grade {index}")
