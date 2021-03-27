import random
import pygame
import copy

class Tetromino():
    _allColours = {
        "red" : (255,0,0),
        "orange" : (255,163,47),
        "yellow" : (255,236,33),
        "green" : (147,240,59),
        "blue" : (55,138,255),
        "pink" : (255,119,253),
        "purple" : (149,82,234)
    }

    _allShapes = {
        #Every shape is 2 element list where the first element is list of vertices and 2nd is centre position
        "O" : [ [[0,0],[2,0],[2,2],[0,2]], [1,1] ],
        "I" : [ [[0,0],[4,0],[4,1],[0,1]], [2,1] ],
        "S" : [ [[1,0],[3,0],[3,1],[2,1],[2,2],[0,2],[0,1],[1,1]], [1.5,1.5] ],
        "Z" : [ [[0,0],[2,0],[2,1],[3,1],[3,2],[1,2],[1,1],[0,1]], [1.5,1.5] ],
        "J" : [ [[0,0],[3,0],[3,2],[2,2],[2,1],[0,1]], [1.5,0.5] ],
        "L" : [ [[0,0],[3,0],[3,1],[1,1],[1,2],[0,2]], [1.5,0.5] ],
        "T" : [ [[0,0],[3,0],[3,1],[2,1],[2,2],[1,2],[1,1],[0,1]], [1.5,0.5] ]
    }

    def __init__(self, shape = None, rotations = 0, colour = None):
        self.rotations = 0
        self.xOffset = 0
        self.yOffset = 0
        if self._allShapes.get(shape) is not None:
            self.shape = shape
        else:
            self.shape = random.choice(list(self._allShapes.keys()))        
        self.blockCoords = copy.deepcopy(self._allShapes[self.shape][0])
        self.centre = copy.copy(self._allShapes[self.shape][1])
        if self._allColours.get(colour) is not None:
            self.colour = _allColours[colour]
        elif colour in self._allColours.values():
            self.colour = colour
        else:
            self.colour = random.choice(list(self._allColours.values()))

    def getMinXCoord(self):
        x = 40600
        for coord in self.blockCoords:
            if coord[0] < x:
                x = coord[0]
        return x
    
    def getMaxXCoord(self):
        x = 0
        for coord in self.blockCoords:
            if coord[0] > x:
                x = coord[0]
        return x
    
    def getMinYCoord(self):
        y = 9999
        for coord in self.blockCoords:
            if coord[1] < y:
                y = coord[1]
        return y

    def getMaxYCoord(self):
        y = 0
        for coord in self.blockCoords:
            if coord[1] > y:
                y = coord[1]
        return y

    # def isOutOfBounds(self):
    #     minX = self.getMinXCoord()
    #     maxX = self.getMaxXCoord()
    #     minY = self.getMinYCoord()
    #     maxY = self.getMaxYCoord()
    #     if (minX < 0) | (minY < 0) | (maxX > 10) | (maxY > 20):
    #         return True
    #     else:
    #         return False

    def incrementBlockCoords(self, x = 0 , y = 0):
        self.xOffset += x
        self.yOffset += y
        self.centre[0] += x
        self.centre[1] += y
        for coord in self.blockCoords:
            coord[0] = coord[0] + x
            coord[1] = coord[1] + y

    # def step(self, direction):
    #     x = y = 0
    #     if direction == "right":
    #         if (self.getMaxXCoord() < 10):
    #             x = 1
    #     elif direction == "left":
    #         if (self.getMinXCoord() > 0):
    #             x = -1
    #     elif direction == "down":
    #         if (self.getMaxYCoord() < 20):
    #             y = 1
    #     self.centre[0] = self.centre[0] + x
    #     self.centre[1] = self.centre[1] + y
    #     for coord in self.blockCoords:
    #         coord[0] = coord[0] + x
    #         coord[1] = coord[1] + y

    # def printRGBColour(self):
    #     print(self.colour)

    def rotateBlockCoords(self, direction = None):
        for coord in self.blockCoords:
            x = coord[0] - self.centre[0]
            y = coord[1] - self.centre[1]
            if direction == "clockwise":
                rotations = 1
                coord[1] = x + self.centre[1]
                coord[0] = -y + self.centre[0]
            elif direction == "anticlockwise":
                rotations = -1
                coord[1] = -x + self.centre[1]
                coord[0] = y + self.centre[0]
        self.rotations = self.rotations + rotations
    
    
