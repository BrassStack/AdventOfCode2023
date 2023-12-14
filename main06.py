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

def FindWins( times, dists ):
    result1 = 1

    for raceNumber in range( len( times ) ):

        print( "Race #" + str( raceNumber ) )
        raceTime = times[raceNumber]
        winCount = 0

        for tHeld in range( raceTime + 1 ):
            d = Distance( tHeld, raceTime )
            # print( d )
            if d > dists[raceNumber]:
                winCount += 1

        result1 *= winCount
        print( "Wins: " + str( winCount ) )
        print()

    return result1

def FindWins2( times, dists ):
    result1 = 1

    for raceNumber in range( len( times ) ):

        print( "Race #" + str( raceNumber ) )
        raceTime = times[raceNumber]
        lossCount = 0

        for tHeld in range( raceTime + 1 ):
            d = Distance( tHeld, raceTime )
            # print( d )
            if d <= dists[raceNumber]:
                lossCount += 1
            else:
                break

        winCount = raceTime + 1 - lossCount * 2
        result1 *= winCount
        print( "Wins: " + str( winCount ) )
        print()

    return result1


print( "Part 1: " + str( FindWins( times, dists ) ) )
print()
print( "Part 1: " + str( FindWins2( times, dists ) ) )
print()

# Example
# times = [71530]
# dists = [940200]

times = [45988373]
dists = [295173412781210]

print( "Part 2: " + str( FindWins2( times, dists ) ) )
