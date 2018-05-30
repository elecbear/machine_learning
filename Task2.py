"""
Intro to Python Lab 1, Task 2

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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message: 
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.". 

HINT: Build a dictionary with telephone numbers as keys, and their
total time spent on the phone as the values. You might find it useful
to write a function that takes a key and a value and modifies a 
dictionary. If the key is already in the dictionary, add the value to
the key's existing value. If the key does not already appear in the
dictionary, add it and set its value to be the given value.
"""

#iterate through the call list and check each line for the call time
#not only call from but also call to could be taken into consider


def update_dict(call_item, _call_dict):
    if call_item[0] in _call_dict:
        _call_dict[call_item[0]] = _call_dict[call_item[0]] + int(call_item[3])
    elif call_item[0] not in _call_dict:
        _call_dict[call_item[0]] = int(call_item[3])

    if call_item[1] in _call_dict:
        _call_dict[call_item[1]] = _call_dict[call_item[1]] + int(call_item[3])
    elif call_item[1] not in _call_dict:
        _call_dict[call_item[1]] = int(call_item[3])

    return _call_dict


call_dict = {}


for call in calls:
    call_dict = update_dict(call, call_dict)

max_key = max(call_dict, key=lambda i: call_dict[i])

print(str(max_key) + " spent the longest time, " + str(call_dict.get(max_key)) +
      " seconds, on the phone during September 2016")
