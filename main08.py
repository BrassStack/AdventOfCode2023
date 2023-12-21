# Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?

# Load data
file = open('input08.txt','r')
data = file.readlines()
file.close()

instructions = list( data[0].replace( "\n", "" ) )

import re
pattern = re.compile( r'\w{3}' )

maps = {}
for i in range( 2, len( data ) ):
    (node, left, right) = pattern.findall( data[i] ) 
    maps[node] = { "L": left, "R": right }

idx   = 0
steps = 1
node  = "AAA"
while True:
    action = instructions[idx]
    next = maps[node][action]
    print( node + " > " + action + " : " + next )
    node = next

    if node == "ZZZ":
        break
    
    # Prep next iteration
    steps += 1
    idx   += 1
    if idx == len( instructions ):
        idx = 0
    if steps > 10000: # Safety check
        break
    
print( str( steps ) + " steps to ZZZ." )