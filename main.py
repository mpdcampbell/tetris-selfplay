import pygame, copy
from tetromino import *
from display import *
from board import *

gameOn = True
window = Window()
board = Board([0, 0, 0])
testTet = board.generatePiece()
draw = Draw(window)
draw.createScreen()

#time = (pygame.time.get_ticks())/1000


while gameOn:
    #pygame.time.set_timer(testTet.step("down"), 2000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            gameOn = False

        draw.screen.fill("Gray")
        draw.drawTetromino(testTet)
        draw.drawGrid(board)
        draw.drawBackground(board)
        if not (board.isHeldPieceEmpty()):
            draw.drawHeldPiece(board)

        #Listen out for all the possible user keyInputs
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
            locked = board.moveOrLockPiece(testTet, "down")
            if (locked):
                print("Score:", board.score)
                testTet = board.generatePiece()
        #This is to help testing, push capslock to show the hidden block coords
        if keyInput[pygame.K_CAPSLOCK]:
            for coord in draw.getScaledCoords(testTet.blockCoords):
                pygame.draw.rect(draw.screen, "Red", (coord[0], coord[1], draw.window.blockSize, draw.window.blockSize))

        pygame.display.update()
           