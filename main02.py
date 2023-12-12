# Determine which games would have been possible if the bag had been loaded with only 
# 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

import re

file = open('input02.txt','r')
data = file.readlines()
file.close()

# Game 5: 6 blue, 4 green; 8 blue, 7 green; 1 red, 10 blue
gamePattern   = r'^Game (\d+): (.*)$'
colorsPattern = r'(\d+) (red|green|blue)'

def CheckSets(sets):
    cubes = {
        "red"   : 0,
        "green" : 0,
        "blue"  : 0
    }
    
    colors = re.findall(colorsPattern, sets)
    for color in colors:
        if cubes[color[1]] < int(color[0]):
            cubes[color[1]] = int(color[0])
    
    print(cubes)
    return cubes

result1 = 0
result2 = 0
for line in data:
    gameMatches = re.findall(gamePattern, line)
    gameId = gameMatches[0][0]
    print(gameId)
    
    sets  = gameMatches[0][1].replace('; ', ', ')
    cubes = CheckSets(sets)
    
    if sum(cubes.values()) <= 39 and cubes["red"] <= 12 and cubes["green"] <= 13 and cubes["blue"] <= 14:
        print("possible")
        # Part 1 answer
        result1 += int(gameId)
    else:
        print("impossible")
        
    # Part 2 answer
    result2 += cubes["red"] * cubes["green"] * cubes["blue"]
    
print('Result 1: ' + str(result1))
print('Result 2: ' + str(result2))
