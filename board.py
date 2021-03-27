import copy
from tetromino import *

class Board:

    def emptyGrid(self):
        self.grid = {}
        for rowCount in range(self.height + 1):
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
        tetromino.incrementBlockCoords(copyTetromino.xOffset, copyTetromino.yOffset)
        self.setHeldPiece(copyTetromino)
        return (tetromino)

    def centrePiece(self, tetromino):
        tetromino.centre[0] = tetromino.centre[0] + (self.width/2)
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
        origCoords = copy.deepcopy(tetromino.blockCoords)
        if direction == "right":
            tetromino.incrementBlockCoords(1,0)
        elif direction == "left":
            tetromino.incrementBlockCoords(-1,0)
        elif direction == "down":
            tetromino.incrementBlockCoords(0,1)
        if (self.isOutOfBounds(tetromino)):
            tetromino.blockCoords = origCoords
            self.lockPieceOnGrid(tetromino)
            return (True)
        else:
            return (False)
#this function is broken because blockCoords is actualy the vertexCoords
    def lockPieceOnGrid(self, tetromino):
        for coord in tetromino.blockCoords:
            y = int(coord[1])
            x = int(coord[0])
            self.grid[y][x] = copy.copy(tetromino.colour)
    
    def rotatePiece(self, tetromino, direction = None):
        origCoords = copy.deepcopy(tetromino.blockCoords)
        tetromino.rotateBlockCoords(direction)
        if self.isOutOfBounds(tetromino):
            tetromino.blockCoords = origCoords