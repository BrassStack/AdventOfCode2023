# The engine schematic (your puzzle input) consists of a visual representation of the engine. 
# There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, 
# is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)
# What is the sum of all of the part numbers in the engine schematic?
import re

file = open('input03.txt','r')
data = file.readlines()
file.close()

symbolPattern = r'[^0-9\.\n]'
symbols = []

lineNum = 0
for line in data:
    matches = re.finditer(symbolPattern, line)
    symbols.append([])
    for m in matches:
        symbols[lineNum].append(m.start())
    
    lineNum += 1

# symbols is now a 2-D array of all symbols:  symbols[row][col]

def IsPartNumber(lineNum, match):
    global symbols
    (begin, end) = m.span()
    
    # check previous line
    if lineNum > 0:
        # print("Checking previous line...")
        for idx in symbols[lineNum-1]:
            if begin - 1 <= idx and idx <= end:
                return (lineNum-1,idx)
        
    # check same line
    for idx in symbols[lineNum]:
        if begin - 1 <= idx and idx <= end:
            return (lineNum,idx)

    # check following line
    if lineNum + 1 < len(symbols):
        # print("Checking following line...")
        for idx in symbols[lineNum+1]:
            if begin - 1 <= idx and idx <= end:
                return (lineNum+1,idx)

    return False

usedSymbols = {}
symbolValues = {}
result1 = 0
lineNum = 0
for line in data:
    log = "Line " + str(lineNum+1)
    matches = re.finditer(r'\d+', line)
    for m in matches:
        symbolLoc = IsPartNumber(lineNum, m)
        if symbolLoc:
            result1 += int(m.group())
            log += " yes"

            usedSymbols[symbolLoc] = usedSymbols.setdefault(symbolLoc, 0) + 1
            symbolValues[symbolLoc] = symbolValues.setdefault(symbolLoc, 1) * int(m.group())
        else:
            log += " no "
    print(log)        
    lineNum += 1 

ratioSum = 0
for k in usedSymbols.keys():
    if usedSymbols[k] == 2:
        ratioSum += symbolValues[k]

print("Result 1: " + str(result1))
print("Result 2: " + str(ratioSum))
