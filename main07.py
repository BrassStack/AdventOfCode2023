# Strengths:
# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a cThird label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456

# Load data
file = open('sample07.txt','r')
data = file.readlines()
file.close()

# Sort functions
import sys
sys.setrecursionlimit(1000)

def MergeSort( strings, left, right ):
    if left < right:
        mid = left + (right - left) // 2
        strings = MergeSort( strings, left, mid )
        strings = MergeSort( strings, mid + 1, right )
        strings = Merge( strings, left, mid, right )
    return strings

def Merge( strings, left, mid, right ):
    n1 = mid - left + 1
    n2 = right - mid

    L = []
    R = []

    for i in range( n1 ):
        L.append( strings[left + i] )

    for i in range( n2 ):
        R.append( strings[mid + 1 + i] )

    i = 0; j = 0; k = left;
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            strings[k] = L[i]
            k += 1
            i += 1
        else:
            strings[k] = R[j]
            k += 1
            j += 1

    while i < n1:
        strings[k] = L [i]
        k += 1
        i += 1

    while j < n2:
        strings[k] = R[j]
        k += 1
        j += 1

    return strings

# Replace face cards with sortable characters
translation = str.maketrans( "AKQJT", "EDCBA", "\n" )
lines = "|".join( data )
lines = lines.translate( translation )
data  = lines.split( "|" )

# Compute strength of a hand (ascii 50 through 69 plus specials)
def GetStrength( hand ):
    cards  = MergeSort( list( hand ), 0, 4 ) # Sort cards in hand, low to high
    first  = cards[0]
    last   = cards[4]
    cFirst = cards.count( first )
    cThird = cards.count( cards[2] )
    cLast  = cards.count( last )

    # Five of a kind
    if first == last:
        return "75"
    # Four of a kind
    if cFirst == 4 or cLast == 4:
        return "74"
    # Full house
    if cFirst + cLast == 5:
        return "73"
    # Three of a kind
    if cThird == 3:
        return "72"
    # Two pair
    if cFirst + cThird + cLast == 5:
        return "71"
    # One pair
    if cFirst == 2 or cThird == 2 or cLast == 2:
        return "70"
    # High card
    return str( ord( cards[4] ) )

# Prepend strengths, zero-padded for comparison
for i in range( len( data ) ):
    data[i] = GetStrength( data[i][:5] ) + " " + data[i]

# Sort hands by strength
data = MergeSort( data, 0, len( data ) - 1 )

# Replace sortable characters with face cards
translation = str.maketrans( "ABCDE", "TJQKA" )
lines = "|".join( data )
lines = lines.translate( translation )
data  = lines.split( "|" )

# Calculate winnings based on rank
result1 = 0
for rank in range( 1, len( data ) + 1 ):
    print( data[rank - 1] )
    print( "  Rank: " + str( rank ) )

    bet = int( data[rank - 1].split( " " )[2] )
    print( "   Bet: " + str( bet ) )

    result1 += bet * rank
    print( "   Tot: " + str( result1 ) )
    print()

print( "Total winnings: " + str( result1 ) )