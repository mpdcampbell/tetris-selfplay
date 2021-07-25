import random, pygame, copy

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
        #Every shape is 3 element list where the first element is list of vertices, 
        #2nd is a list of constituent block coords and 3rd is the centre of rotation
        "O" : [ [[0,0],[2,0],[2,2],[0,2]], [[0,0],[1,0],[0,1],[1,1]], [1,1] ],
        "I" : [ [[0,0],[4,0],[4,1],[0,1]], [[0,0],[1,0],[2,0],[3,0]], [2,1] ], 
        "S" : [ [[1,0],[3,0],[3,1],[2,1],[2,2],[0,2],[0,1],[1,1]], [[1,0],[2,0],[0,1],[1,1]], [1.5,1.5] ],
        "Z" : [ [[0,0],[2,0],[2,1],[3,1],[3,2],[1,2],[1,1],[0,1]], [[0,0],[1,0],[1,1],[2,1]], [1.5,1.5] ],
        "J" : [ [[0,0],[3,0],[3,2],[2,2],[2,1],[0,1]], [[0,0],[1,0],[2,0],[2,1]], [1.5,0.5] ],
        "L" : [ [[0,0],[3,0],[3,1],[1,1],[1,2],[0,2]], [[0,0],[1,0],[2,0],[0,1]], [1.5,0.5] ],
        "T" : [ [[0,0],[3,0],[3,1],[2,1],[2,2],[1,2],[1,1],[0,1]], [[0,0],[1,0],[2,0],[1,1]], [1.5,0.5] ]
    }

    def __init__(self, shape = None, rotations = 0, colour = None):
        self.rotations = 0
        self.xOffset = 0
        self.yOffset = 0
        if self._allShapes.get(shape) is not None:
            self.shape = shape
        else:
            self.shape = random.choice(list(self._allShapes.keys()))
        self.vertexCoords = copy.deepcopy(self._allShapes[self.shape][0])
        self.blockCoords = copy.deepcopy(self._allShapes[self.shape][1])
        self.centre = copy.copy(self._allShapes[self.shape][2])
        if self._allColours.get(colour) is not None:
            self.colour = self._allColours[colour]
        elif colour in self._allColours.values():
            self.colour = colour
        else:
            self.colour = random.choice(list(self._allColours.values()))

    def getMinXCoord(self):
        x = 38400
        for coord in self.vertexCoords:
            if coord[0] < x:
                x = coord[0]
        return x
    
    def getMaxXCoord(self):
        x = 0
        for coord in self.vertexCoords:
            if coord[0] > x:
                x = coord[0]
        return x
    
    def getMinYCoord(self):
        y = 21600
        for coord in self.vertexCoords:
            if coord[1] < y:
                y = coord[1]
        return y

    def getMaxYCoord(self):
        y = 0
        for coord in self.vertexCoords:
            if coord[1] > y:
                y = coord[1]
        return y

    def incrementCoords(self, x = 0 , y = 0):
        self.xOffset += x
        self.yOffset += y
        self.centre[0] += x
        self.centre[1] += y
        for coord in self.vertexCoords:
            coord[0] += x
            coord[1] += y
        for coord in self.blockCoords:
            coord[0] += x
            coord[1] += y

    def rotateCoords(self, rotation = 0):
        if rotation != 0:
            self.rotations += rotation
            direction = rotation / abs(rotation)
            for i in range(abs(rotation)):
                for coord in self.vertexCoords:
                    x = coord[0] - self.centre[0]
                    y = coord[1] - self.centre[1]
                    coord[1] = self.centre[1] + (direction * x)
                    coord[0] = self.centre[0] - (direction * y)
                for coord in self.blockCoords:
                    x = coord[0] - self.centre[0]
                    y = coord[1] - self.centre[1]
                    coord[1] = self.centre[1] + (direction * x)
                    coord[0] = self.centre[0] - (direction * y)
                    #This line is needed to adjust so the block coord is always top left coord of "block"
                    coord[int((1 - direction)/2)] += -1