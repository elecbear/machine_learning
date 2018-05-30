"""
Intro to Python Project 1, Task 1

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Project Preparation page.
"""


"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1: 
How many different telephone numbers are there in the records? 
Print a message: 
"There are <count> different telephone numbers in the records."
"""

#first need to abstract numbers and put them into a list
#then need to create set from the text/call numbers' list

text_set_1 = set([text[0] for text in texts])
text_set_2 = set([text[1] for text in texts])

call_set_1 = set([call[0] for call in calls])
call_set_2 = set([call[1] for call in calls])

#then union these sets
ulti_set = text_set_1.union(text_set_2).union(call_set_1).union(call_set_2)

print("There are "+ str(len(ulti_set) + " different telephone numbers in the records."))



