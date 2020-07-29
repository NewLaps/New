
# **This is the README.md file**

This is C++ program to play a game of rock, paper,
spock.

```python
import random

class rndList:
    def __init__(self, itemNum, x, y):
        self.itemNum = itemNum
        self.x = x
        self.y = y

rndLineArray = []
rndCoordArray = []
randL1 = rndList
for i in range():
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
  ...
```

## Example

- This was written on [VSCODE]

---
Using a docker container to run code.

    FROM gcc:latest

    # These commands copy your files into the specified directory in the image
    # and set that as the working location
    COPY . /usr/src/myapp
    WORKDIR /usr/src/myapp

    # This command compiles your app using GCC, adjust for your source code
    RUN g++ -o myapp rockPaperSpock.cpp
    ...

| Symbols   | Are   | Number|
|:--------- |:-----:| -----:|
| Rock      | ✊     | 1    |
| Paper     | ✋     | 2    |
| Spock     | ✌️     | 3    |
|

Like *rock, paper, scissors.*

1. The program asks for the user to enter 1, 2 or 3 to choose a corrisponding symbol.
2. Then produces a random choice of it's own to compare.
