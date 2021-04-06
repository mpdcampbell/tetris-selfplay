import copy
from tetromino import *

class Board:
    _lineScores = (0, 40, 100, 300, 1200)

    def emptyGrid(self):
        self.grid = {}
        self.emptyRow = []
        for x in range(self.width):
            self.emptyRow.append(0)
        for rowCount in range(self.height):
            gridRow = {rowCount : copy.copy(self.emptyRow)}
            self.grid.update(gridRow)

    def __init__(self, colour = [190, 190, 190]):
        self.colour = colour
        self.width = 10
        self.height = 20
        self.heldPiece = None
        self.score = 0
        self.linesCleared = 0
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
        tetromino.centre[0] = tetromino.centre[0] + (self.width/2) - 1
        for coord in tetromino.vertexCoords:
            coord[0] += (self.width/2) - 1
        for coord in tetromino.blockCoords:
            coord[0] += (self.width/2) - 1 
        
    def generatePiece(self):
        tetromino = Tetromino()
        self.centrePiece(tetromino)
        return (tetromino)

    def isOutOfBounds(self, tetromino):
        minX = tetromino.getMinXCoord()
        maxX = tetromino.getMaxXCoord()
        minY = tetromino.getMinYCoord()
        maxY = tetromino.getMaxYCoord()
        if (minX < 0) or (minY < 0) or (maxX > self.width) or (maxY > self.height):
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

        if (self.isOutOfBounds(tetromino) or self.isGridBlocked(tetromino)):
            tetromino.incrementCoords(-x,-y)
            if (y != 0):
                self.lockPieceOnGrid(tetromino)
                clearedRowCount = self.clearFullRows()
                self.linesCleared += clearedRowCount
                self.score += self._lineScores[clearedRowCount]
            return True
        return False

    def isGridBlocked(self, tetromino):
        for coord in tetromino.blockCoords:
            y = int(coord[1])
            x = int(coord[0])
            if self.grid[y][x] != 0:
                return True
        return False

    def lockPieceOnGrid(self, tetromino):
        for coord in tetromino.blockCoords:
            y = int(coord[1])
            x = int(coord[0])
            self.grid[y][x] = copy.copy(tetromino.colour)
    
    def clearFullRows(self):
        fullRowCount = 0
        y = self.height - 1
        while (y > 0):
            emptyBlocks = 0
            for x in range(self.width):
                if self.grid[y][x] == 0:
                    emptyBlocks +=1
            if emptyBlocks == self.width:
                return fullRowCount
            elif emptyBlocks == 0:
                fullRowCount += 1
                self.grid[y] = copy.copy(self.emptyRow)
                for i in range (y, 1, -1):
                    self.grid[i] = copy.deepcopy(self.grid[i-1])
                y += 1
            y-=1
        #This would occur if none of rows are empty or filled
        return fullRowCount
         
    def rotatePiece(self, tetromino, direction = None):
        if direction == "clockwise":
            rotation = 1
        elif direction == "anticlockwise":
            rotation = -1
        tetromino.rotateCoords(rotation)
        if (self.isOutOfBounds(tetromino) or self.isGridBlocked(tetromino)):
            tetromino.rotateCoords(-rotation)

    def newPieceOrGameOver(self, tetromino):
        if (tetromino.xOffset == 0) and (tetromino.yOffset == 0):
            return None
        else:
            tetromino = self.generatePiece()
            return tetromino
    
    def fastDropPiece(self, tetromino):
        isLocked = False
        while (not isLocked):
            isLocked = self.moveOrLockPiece(tetromino,"down")
