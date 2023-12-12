
# Online Python - IDE, Editor, Compiler, Interpreter

import re

file = open('input01.txt','r')
data = file.readlines()
file.close()
total = 0

trans = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

pattern = '(?=(\d'

for key in trans.keys():
    pattern += '|' + key
    
pattern += '))'

for line in data:
    digits = re.findall(pattern, line)
    first = digits[0] if len(digits[0]) == 1 else trans[digits[0]]
    last = digits[-1] if len(digits[-1]) == 1 else trans[digits[-1]]
    total += int(first + last)

print('Total: ' + str(total))
