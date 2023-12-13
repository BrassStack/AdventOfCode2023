# which of the numbers you have appear in the list of winning numbers. 
# The first match makes the card worth one point and each match after the 
# first doubles the point value of that card.

import re

file = open('input04.txt','r')
data = file.readlines()
file.close()

# 10 winning numbers | 25 my numbers
pattern = r'Card +\d+: +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +\| +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+) +(\d+)'

score = 0
lineNum = 1
for line in data:
    matches = re.search(pattern, line)
    if matches:
        winners = []
        mine = []
        for idx in range(35):
            if idx < 10:
                winners.append(matches.group(idx+1))
            else:
                mine.append(matches.group(idx+1))
                
        numberOfMatches = 0
        for n in mine:
            numberOfMatches += winners.count(n)
            
        if numberOfMatches > 0:
            score += 2 ** (numberOfMatches - 1)
            print( "Card " + str(lineNum) + " matches: " + str(numberOfMatches) )
            print( "New score: " + str(score) )
    lineNum += 1

print( "Result 1: " + str(score) )
