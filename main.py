import pygame, copy
from tetromino import *
from display import *
from board import *

gameOver = False
window = Window()
board = Board([0, 0, 0])
testTet = board.generatePiece()
draw = Draw(window)
draw.createScreen()
clock = pygame.time.Clock()
timeCount = 0


while not gameOver:
    
    gameOver = board.isGameOver()
    timeCount += clock.get_rawtime()
    clock.tick()
    draw.screen.fill("Gray")
    draw.drawGrid(board)
    draw.drawTetromino(testTet)
    draw.drawBackground(board)
    draw.drawScore(board)
    if not (board.isHeldPieceEmpty()):
        draw.drawHeldPiece(board)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            gameOn = False
        keyInput = pygame.key.get_pressed()
        if keyInput[pygame.K_TAB]:
            testTet = board.generatePiece()
        if keyInput[pygame.K_LCTRL]:
            if (board.isHeldPieceEmpty()):
                board.setHeldPiece(testTet)
                testTet = board.generatePiece()
            else:
                testTet = board.swapWithHeldPiece(testTet)
        if keyInput[pygame.K_LSHIFT]:
            board.rotatePiece(testTet, "anticlockwise")
        if keyInput[pygame.K_UP]:
            board.rotatePiece(testTet, "clockwise")
        if keyInput[pygame.K_RIGHT]:
            board.moveOrLockPiece(testTet, "right")
        if keyInput[pygame.K_LEFT]:
            board.moveOrLockPiece(testTet, "left")
        if keyInput[pygame.K_DOWN]:
            board.fastDropPiece(testTet)
            testTet = board.generatePiece()

        #This is to help testing, push capslock to show the hidden block coords
        if keyInput[pygame.K_CAPSLOCK]:
            for coord in draw.getScaledCoords(testTet.blockCoords):
                pygame.draw.rect(draw.screen, "Red", (coord[0], coord[1], draw.window.blockSize, draw.window.blockSize))

    if (timeCount >= 500):
        timeCount = 0
        locked = board.moveOrLockPiece(testTet, "down")
        if (locked):
            testTet = board.generatePiece()

    pygame.display.update()    
           