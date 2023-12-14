# find the lowest location number that corresponds to any of the initial seeds. 
# To do this, you'll need to convert each seed number through other categories 
# until you can find its corresponding location number.

# Example
# times = [7,15,30]
# dists = [9,40,200]

times = [45,98,83,73]
dists = [295,1734,1278,1210]

def Distance( tHeld, tTotal ):
    return max( 0, tHeld * (tTotal - tHeld) )

result1 = 1

for raceNumber in range( len( times ) ):

    print( "Race #" + str( raceNumber ) )
    raceTime = times[raceNumber]
    winCount = 0

    for tHeld in range( raceTime + 1 ):
        if Distance( tHeld, raceTime ) > dists[raceNumber]:
            winCount += 1

    result1 *= winCount
    print( "Wins: " + str( winCount ) )
    print()

print( "Part 1: " + str( result1 ) )
