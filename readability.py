import re
from nltk.tokenize import sent_tokenize
txt = input("Please add text for analyzing:")


non_letters = set(':;,.!?-" \'')

letters = len([letter for letter in txt if letter not in non_letters])

words = len([len(x) for x in txt.split()])

sentence = len(sent_tokenize(txt))


index = 0.0588 * (letters / words * 100) - 0.296 * (sentence / words * 100) - 15.8
print (round(index))

