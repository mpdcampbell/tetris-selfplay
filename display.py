import copy
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
        self.width = 21 * self.blockSize
        self.height = 20 * self.blockSize

    def __init__(self, blockSize = None):
        if (blockSize is not None):
            if isinstance(blockSize, int):
                if blockSize < 6:
                    print("blockSize minimum is 6 because of smallest window limitations")
                    self.blockSize = 6
                else:
                    self.blockSize = blockSize
                self.width = 21 * self.blockSize
                self.height = 20 * self.blockSize
            else:
                print("blockSize value provided is not an int, using default value")
        else:
            self.setDefaultDimensions()

class Draw:

    def __init__(self, window = Window()):
        self.window = window
        self.boardRect = pygame.Rect(2*self.window.blockSize, 0, 10*window.blockSize, window.height)
        self.heldRect = pygame.Rect(14*self.window.blockSize, self.window.blockSize, 5*self.window.blockSize, 4*self.window.blockSize)

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
        self.screen.fill("White")
        pygame.draw.rect(self.screen, board.colour, self.boardRect, 3)
        pygame.draw.rect(self.screen, board.colour, self.heldRect, 3)

    def drawGrid(self, board):
        b = self.window.blockSize
        for y in range(int(board.height)):
            for x in range(int(board.width)):
                if board.grid[y][x] != 0:
                    pygame.draw.rect(self.screen, board.grid[y][x], ((x+2)*b, y*b, b, b))

    def drawHeldPiece(self, board):
        #This needs updated so the X axis offset depends on the piece shape
        #so it can be centred in the block
        shape = board.heldPiece.shape
        zeroCoords = board.heldPiece._allShapes[shape][0]
        copyCoords = copy.deepcopy(zeroCoords)
        for coord in copyCoords:
            coord[0] = (coord[0] + 14.5)*self.window.blockSize
            coord[1] = (coord[1] + 2)*self.window.blockSize
        pygame.draw.polygon(self.screen, board.heldPiece.colour, copyCoords)
        pygame.draw.polygon(self.screen, "Black",copyCoords, 2)

    def drawTetromino(self, tetromino):
        pygame.draw.polygon(self.screen, tetromino.colour, self.getScaledCoords(tetromino.vertexCoords))
        pygame.draw.polygon(self.screen, "Black", self.getScaledCoords(tetromino.vertexCoords), 2)

    def updateDisplay(self, board, tetromino):
        self.board = board
        self.tetromino = tetromino
        pygame.display.update()
        

  

