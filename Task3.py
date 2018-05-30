"""
Intro to Python Lab 1, Task 3

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Lab Preparation page.
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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore. 
Fixed line numbers include parentheses, so Bangalore numbers 
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. 
 - Fixed lines start with an area code enclosed in brackets. The area 
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


#iterate through the list and finds out all the items which have callers as Bangalore people
#Put all the receiver number's prefix into a set
#put the set into a list, then sort and print it

bangalore_prefix = "(080)"

call_receiver_set = set()

for item in calls:
    if item[0].find(bangalore_prefix) > -1:
        if item[1][0] == "(":
            call_receiver_set.add(item[1][:item[1].find(")")+1])
        elif item[1][0] == "7" or item[1][0] == "8" or item[1][0] == "9":
            call_receiver_set.add(item[1][:4])
        elif item[1][0:3] == "140":
            call_receiver_set.add("140")

print("The numbers called by people in Bangalore have codes:" + "\n" + "\n".join(sorted(list(call_receiver_set), key=str)))


all_call_counter = 0

call_to_bangalore_counter = 0

for item in calls:
    if item[0].find(bangalore_prefix) > -1:
        all_call_counter += 1
        if item[1].find(bangalore_prefix) > -1:
            call_to_bangalore_counter += 1

print(str("%.2f" % (call_to_bangalore_counter/all_call_counter)) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


