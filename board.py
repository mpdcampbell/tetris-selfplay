import copy, random
from tetromino import *
from direction import *
from rotation import *

class Board:
    _lineScores = (0, 1, 3, 5, 8)

    def emptyGrid(self):
        self.grid = {}
        self.emptyRow = []
        for x in range(self.width):
            self.emptyRow.append(0)
        for rowCount in range(self.height):
            gridRow = {rowCount : copy.copy(self.emptyRow)}
            self.grid.update(gridRow)

    def __init__(self, colour = "Gray"):
        self.colour = colour
        self.width = 10
        self.height = 21
        self.heldPiece = None
        self.startInterval = 1000
        self.score = 0
        self.linesCleared = 0
        self.level = 1
        self.levelScore = 0 
        self.emptyGrid()
        self.holeCount = None
        self.pieceList = []

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
        tetromino.centre[0] = tetromino.centre[0] + (self.width/2) - 2
        for coord in tetromino.vertexCoords:
            coord[0] += (self.width/2) - 2
        for coord in tetromino.blockCoords:
            coord[0] += (self.width/2) - 2 
        
    def generatePiece(self):
        if (len(self.pieceList) == 0):
            self.pieceList = list(Tetromino._allShapes.keys())
            random.shuffle(self.pieceList)
        tetromino = Tetromino(self.pieceList.pop())
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

    def moveOrLockPiece(self, tetromino, direction, count = 1):
        x = direction.value[0]
        y = direction.value[1]
        for i in range(count):
            tetromino.incrementCoords(x, y)
            if (self.isOutOfBounds(tetromino) or self.isGridBlocked(tetromino)):
                tetromino.incrementCoords(-x,-y)
                if (y > 0):
                    self.lockPieceOnGrid(tetromino)
                    clearedRowCount = self.clearFullRows()
                    self.updateScores(clearedRowCount)
                    return True
        return False

    def updateScores(self, clearedRowCount):
        self.linesCleared += clearedRowCount
        self.score += (self._lineScores[clearedRowCount] * self.level)
        if (self.level < 15):
            self.level = (self.linesCleared // 10) + 1

    def getDropInterval(self):
        scale = pow(0.8, self.level)
        dropInterval = int(self.startInterval * scale)
        return dropInterval

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
        return fullRowCount
         
    def rotatePiece(self, tetromino, rotation = None, count = 1):
        for i in range(count):
            tetromino.rotateCoords(rotation)
            if (self.isOutOfBounds(tetromino) or self.isGridBlocked(tetromino)):
                tetromino.rotateCoords(-rotation)
                break

    def newPieceOrGameOver(self, tetromino):
        if (tetromino.xOffset == 0) and (tetromino.yOffset == 0):
            return None
        else:
            tetromino = self.generatePiece()
            return tetromino
    
    def dropAndLockPiece(self, tetromino):
        isLocked = False
        while (not isLocked):
            isLocked = self.moveOrLockPiece(tetromino,Direction.DOWN)

    def dropPieceWithoutLock(self, tetromino):
            while not ((self.isOutOfBounds(tetromino) or self.isGridBlocked(tetromino))):
                tetromino.incrementCoords(0, 1)
            tetromino.incrementCoords(0, -1)
    
    def moveLeftAndLockPiece(self, tetromino, count):
        self.moveOrLockPiece(tetromino, Direction.LEFT, count)
        self.dropAndLockPiece(tetromino)