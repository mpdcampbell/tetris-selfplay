import pygame, copy
from tetromino import *
pygame.init()

class Window:

    def setDefaultDimensions(self):
        displayWidth = pygame.display.Info().current_w
        displayHeight = pygame.display.Info().current_h
        if displayHeight <= displayWidth:
            self.blockSize = displayHeight // 30
        else:
            self.blockSize = displayWidth // 30
        self.width = 20 * self.blockSize
        self.height = 21 * self.blockSize

    def __init__(self, blockSize = None):
        if (blockSize is not None):
            if isinstance(blockSize, int):
                if blockSize < 6:
                    print("blockSize minimum is 6 because of smallest window limitations")
                    self.blockSize = 6
                else:
                    self.blockSize = blockSize
                self.width = 20 * self.blockSize
                self.height = 21 * self.blockSize
            else:
                print("blockSize value provided is not an int, using default value")
        else:
            self.setDefaultDimensions()

class Draw:

    def __init__(self, window = Window()):
        self.window = window
        self.boardWidth = 10 
        self.heldWidth = 4
        self.boardXOffset = 2
        self.heldXOffset = self.boardWidth + (self.boardXOffset*2)
        self.heldYOffset = 1
        self.boardOutline = (self.window.blockSize // 15) if (self.window.blockSize >= 15) else 1
        self.pieceOutline = (self.window.blockSize // 15) if (self.window.blockSize >= 15) else 1
        self.boardRect = pygame.Rect(self.boardXOffset*self.window.blockSize, 0, (self.boardWidth*self.window.blockSize) + self.boardOutline, self.window.height)
        self.heldRect = pygame.Rect(self.heldXOffset*self.window.blockSize, self.heldYOffset*self.window.blockSize, self.heldWidth*self.window.blockSize, self.heldWidth*self.window.blockSize)
        self.fontColour = (125, 125, 125)
        self.fontPath = "font/Fairfax.ttf"

    def createScreen(self):
        self.screen = pygame.display.set_mode((self.window.width, self.window.height))
        pygame.display.set_caption("")

    def getScaledCoords(self, vertexCoords):
        copyCoords = copy.deepcopy(vertexCoords)
        for coord in copyCoords:
            coord[0] = (coord[0] + 2)*self.window.blockSize
            coord[1] = coord[1]*self.window.blockSize
        return copyCoords

    def drawBackground(self, board):
        self.drawBoard(board)
        self.drawHeldSquare(board)

    def drawHeldSquare(self, board):
        pygame.draw.rect(self.screen, board.colour, self.heldRect, self.boardOutline)

    def drawBoard(self, board):
        pygame.draw.rect(self.screen, board.colour, self.boardRect, 0)
        for x in range(self.boardXOffset*self.window.blockSize, (self.boardWidth + self.boardXOffset)*self.window.blockSize, self.window.blockSize):
            for y in range(0, self.window.height, self.window.blockSize):
                square = pygame.Rect(x + self.boardOutline, y + self.boardOutline, self.window.blockSize - self.boardOutline, self.window.blockSize - self.boardOutline)
                pygame.draw.rect(self.screen, "WHITE", square, 0)

    def drawGridPieces(self, board):
        blockSize = self.window.blockSize
        for y in range(int(board.height)):
            for x in range(int(board.width)):
                if board.grid[y][x] != 0:
                    pygame.draw.rect(self.screen, board.grid[y][x], ((x+self.boardXOffset)*blockSize, y*blockSize, blockSize, blockSize))

    def drawHeldPiece(self, board):
        shape = board.heldPiece.shape
        tempPiece = Tetromino(board.heldPiece.shape, 0, board.heldPiece.colour)
        if shape in ("S","Z","I"):
            centreCorrection = 0.5
        elif shape in ("L","J","T"):
            centreCorrection = -0.5
        else:
            centreCorrection = 0
        xOffset = self.heldXOffset - tempPiece.centre[0]
        yOffset = self.heldYOffset + (self.heldWidth/2) + centreCorrection - tempPiece.centre[1]
        tempPiece.incrementCoords(xOffset, yOffset)
        self.drawTetromino(tempPiece)
        
    def drawTetromino(self, tetromino):
        pygame.draw.polygon(self.screen, tetromino.colour, self.getScaledCoords(tetromino.vertexCoords))
        pygame.draw.polygon(self.screen, "Black", self.getScaledCoords(tetromino.vertexCoords), self.pieceOutline)

    def updateDisplay(self, board, tetromino):
        self.board = board
        self.tetromino = tetromino
        pygame.display.update()

    def drawScores(self, board):
        fontSize = int(1.5 * self.window.blockSize)
        gameFont = pygame.font.Font(self.fontPath, fontSize)
        scoreNum = gameFont.render(str(board.score), True, self.fontColour)
        scoreText = gameFont.render("Score", True, self.fontColour)
        lineNum = gameFont.render(str(board.linesCleared), True, self.fontColour)
        lineText = gameFont.render("Lines", True, self.fontColour)
        levelNum = gameFont.render(str(board.level), True, self.fontColour)
        levelText = gameFont.render("Level", True, self.fontColour)
        scoreYPos = int(board.height*0.33)
        lineYPos = scoreYPos + 3
        levelYPos = lineYPos + 3
        self.screen.blit(scoreNum, (self.heldXOffset*self.window.blockSize, (scoreYPos+1)*self.window.blockSize))
        self.screen.blit(scoreText, (self.heldXOffset*self.window.blockSize, (scoreYPos)*self.window.blockSize))
        self.screen.blit(lineText, (self.heldXOffset*self.window.blockSize, lineYPos*self.window.blockSize))
        self.screen.blit(lineNum, (self.heldXOffset*self.window.blockSize, (lineYPos+1)*self.window.blockSize))
        self.screen.blit(levelText, (self.heldXOffset*self.window.blockSize, levelYPos*self.window.blockSize))
        self.screen.blit(levelNum, (self.heldXOffset*self.window.blockSize, (levelYPos+1)*self.window.blockSize))

    def drawGameOver(self, board):
        fontSize = int(2.5 * self.window.blockSize)
        gameFont = pygame.font.Font(self.fontPath, fontSize)
        gameOverText = gameFont.render("GAME OVER", True, self.fontColour)
        self.screen.blit(gameOverText, (self.window.blockSize, ((board.height/2)-1)*self.window.blockSize))

    def drawStartScreen(self, board):
        fontSize = int(2.5 * self.window.blockSize)
        gameFont = pygame.font.Font("font/Fairfax.ttf", fontSize)
        startText = gameFont.render("PRESS SPACE TO", True, self.fontColour)
        startText2 = gameFont.render("START", True, self.fontColour)
        self.screen.blit(startText, (self.window.blockSize, ((board.height/2)-1)*self.window.blockSize))
        self.screen.blit(startText2, (7*self.window.blockSize, ((board.height/2)+1)*self.window.blockSize))

    def drawPauseScreen(self, board):
        fontSize = int(3 * self.window.blockSize)
        gameFont = pygame.font.Font(self.fontPath, fontSize)
        pauseText = gameFont.render("PAUSED", True, self.fontColour)
        self.screen.blit(pauseText, (5*self.window.blockSize, ((board.height/2)-1)*self.window.blockSize))