import pygame, copy
from tetromino import *
from display import *
from board import *

isOpen = True
newGame = True
gameOver = False
paused = False
locked = False
window = Window()
draw = Draw(window)
draw.createScreen()
clock = pygame.time.Clock()

while isOpen:
    #Draw new Frame
    pygame.display.update()
    #Clear screen
    draw.screen.fill("White")

    #reset board
    if newGame:
        board = Board()
        tetromino = board.generatePiece()
        timeCount = 0
        draw.drawStartScreen(board)
    #newGame screen loop
        while newGame:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    newGame = False
                    isOpen = False
                keyInput = pygame.key.get_pressed()
                if keyInput[pygame.K_SPACE]:
                    newGame = False

    #Pause / Start screen loop
    while paused:
        draw.drawPauseScreen(board)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False 
                isOpen = False
            keyInput = pygame.key.get_pressed()
            if keyInput[pygame.K_p]:
                paused = False

    #Draw game elements to screen
    draw.drawBackground(board)
    draw.drawGridPieces(board)
    draw.drawTetromino(tetromino)
    draw.drawScores(board)
    if not (board.isHeldPieceEmpty()):
        draw.drawHeldPiece(board)

    #Step game forward
    timeCount += clock.get_rawtime()
    clock.tick()
    if (timeCount >= board.getDropInterval()):
        timeCount = 0
        locked = board.moveOrLockPiece(tetromino, "down")
        if (locked):
            tetromino = board.newPieceOrGameOver(tetromino)
            if tetromino == None:
                gameOver = True

    #Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            isOpen = False
        keyInput = pygame.key.get_pressed()
        if keyInput[pygame.K_p]:
            paused = True
        if keyInput[pygame.K_SPACE]:
            newGame = True
        if keyInput[pygame.K_LSHIFT] or keyInput[pygame.K_RSHIFT]:
            board.rotatePiece(tetromino, "anticlockwise")
        if keyInput[pygame.K_UP]:
            board.rotatePiece(tetromino, "clockwise")
        if keyInput[pygame.K_RIGHT]:
            board.moveOrLockPiece(tetromino, "right")
        if keyInput[pygame.K_LEFT]:
            board.moveOrLockPiece(tetromino, "left")
        if keyInput[pygame.K_DOWN]:
            board.moveOrLockPiece(tetromino, "down")
        if keyInput[pygame.K_CAPSLOCK]:
            board.fastDropPiece(tetromino)
            tetromino = board.newPieceOrGameOver(tetromino)
            if tetromino == None:
                gameOver = True
        if keyInput[pygame.K_LCTRL] or keyInput[pygame.K_RCTRL]:
            if (board.isHeldPieceEmpty()):
                board.setHeldPiece(tetromino)
                tetromino = board.generatePiece()
            else:
                tetromino = board.swapWithHeldPiece(tetromino)

    #Game over screen loop
    while gameOver:
        draw.drawGameOver(board)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                gameOver = False
                isOpen = False
            keyInput = pygame.key.get_pressed()
            if keyInput[pygame.K_SPACE]:
                newGame = True
                gameOver = False
           