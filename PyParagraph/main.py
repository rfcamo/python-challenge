# Imports here
import os
import re
import string


# Files to load and output
fileload = "raw_data/paragraph_1.txt"

# Open and read the txt file
with open(fileload) as txtfile:
    paragraph_txt = txtfile.read()

count_word = len(re.findall(r'\w+', paragraph_txt))

sen_count = len(re.findall(r'\.', paragraph_txt))

letters = string.ascii_letters + " "        

para_list = paragraph_txt.split()

letter_total = 0
for word in para_list:
    letter_total += len(word)

count_word = len(para_list)
avg_letter_count = letter_total/count_word
words_per_sentence = count_word/sen_count

output = (
		f"Paragraph Analysis\n"
		f"------------------\n"
		f"Approximate Word Count: {count_word}\n"
		f"Approximate Sentence Count: {sen_count}\n"
		f"Average Letter Count: {round(avg_letter_count, 1)}\n"
		f"Average Sentence Length: {words_per_sentence}")
print(output)

