import copy
from tetromino import *

class Board:

    def emptyGrid(self):
        self.grid = {}
        for rowCount in range(self.height):
            gridRow = {rowCount : [0,0,0,0,0,0,0,0,0,0]}
            self.grid.update(gridRow)

    def __init__(self, colour = [190, 190, 190]):
        self.colour = colour
        self.width = 10
        self.height = 20
        self.heldPiece = None
        self.emptyGrid()

    def setHeldPiece(self, tetromino):
        self.heldPiece = Tetromino(tetromino.shape, tetromino.rotations, tetromino.colour)

    def isHeldPieceEmpty(self):
        return (self.heldPiece == None)

    def swapWithHeldPiece(self, tetromino):
        copyTetromino = copy.deepcopy(tetromino)
        tetromino = copy.deepcopy(self.heldPiece)
        self.centrePiece(tetromino)
        tetromino.incrementCoords(copyTetromino.xOffset, copyTetromino.yOffset)
        self.setHeldPiece(copyTetromino)
        return (tetromino)

    def centrePiece(self, tetromino):
        tetromino.centre[0] = tetromino.centre[0] + (self.width/2)
        for coord in tetromino.vertexCoords:
            coord[0] = coord[0] + (self.width/2)
        for coord in tetromino.blockCoords:
            coord[0] = coord[0] + (self.width/2)
        
    def generatePiece(self):
        tetromino = Tetromino()
        self.centrePiece(tetromino)
        return (tetromino)

    def isOutOfBounds(self, tetromino):
        minX = tetromino.getMinXCoord()
        maxX = tetromino.getMaxXCoord()
        minY = tetromino.getMinYCoord()
        maxY = tetromino.getMaxYCoord()
        if (minX < 0) | (minY < 0) | (maxX > self.width) | (maxY > self.height):
            return True
        else:
            return False

    def moveOrLockPiece(self, tetromino, direction):
        x = 0
        y = 0
        if direction == "right":
            x = 1
        elif direction == "left":
            x = -1
        elif direction == "down":
            y = 1
        tetromino.incrementCoords(x,y)
        if (self.isOutOfBounds(tetromino)):
            tetromino.incrementCoords(-x, -y)
            if (y != 0):
                self.lockPieceOnGrid(tetromino)
                return (True)
        return (False)

    def lockPieceOnGrid(self, tetromino):
        for coord in tetromino.blockCoords:
            y = int(coord[1])
            x = int(coord[0])
            self.grid[y][x] = copy.copy(tetromino.colour)
    
    def rotatePiece(self, tetromino, direction = None):
        if direction == "clockwise":
            rotation = 1
        elif direction == "anticlockwise":
            rotation = -1
        tetromino.rotateCoords(rotation)
        if self.isOutOfBounds(tetromino):
            tetromino.rotateCoords(-rotation)