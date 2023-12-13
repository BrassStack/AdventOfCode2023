# find the lowest location number that corresponds to any of the initial seeds. 
# To do this, you'll need to convert each seed number through other categories 
# until you can find its corresponding location number.

file = open('input05.txt','r')
data = file.readlines()
file.close()

seeds = data[0].rstrip().split(" ")
seeds.pop(0)

class Map:
    def __init__(self):
        # Each one is (offset, source-start, source-end)
        self.ranges = []

    # Input is (destination, source, length)
    def AddRange(self, r):
        # Offset converts source to destination
        self.ranges.append((int(r[0]) - int(r[1]), int(r[1]), int(r[1]) + int(r[2])))

    def MapValue(self, v):
        for r in self.ranges:
            if r[1] <= v <= r[2]:
                return v + r[0]

        return v


allMaps = []
newMap = False
for i in range(len(data)):
    if i == 0:
        continue
    
    if data[i].endswith(":\n"):
        print( "New map found: " + data[i].rstrip() )
        newMap = True
        continue

    if newMap:
        allMaps.append( Map() )
        newMap = False

    if len( data[i] ) > 2:
        allMaps[len(allMaps) - 1].AddRange( data[i].rstrip().split(" ") )

locations = []
for s in seeds:
    value = int(s)
    for m in allMaps:
        value = m.MapValue( value )

    locations.append( value )
    print( "Seed " + s + " results in location " + str(value) )

print( "Result 1: " + str(min(locations)) )
