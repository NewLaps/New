import random

class rndList:
    def __init__(self, itemNum, x, y):
        self.itemNum = itemNum
        self.x = x
        self.y = y

rndLineArray = []
rndCoordArray = []
randL1 = rndList
for i in range(5):
    rndCoordArray = []
    randX = random.randint(1,10)
    randY = random.randint(1,10)
    randL1 = rndList(i, randX, randY)
    print("Coord {2} - (x = {0}) (y = {1})".format(randL1.x,randL1.y,randL1.itemNum))
    rndCoordArray.append(randX)
    rndCoordArray.append(randY)
    rndLineArray.append(rndCoordArray)
print("Coord ", rndLineArray)
print("Test", rndLineArray[4])

for i in rndLineArray:
    print(i)