import pygame, copy
from tetromino import *
from display import *
from board import *

isOpen = True
started = False
gameOver = False
paused = False
locked = False
window = Window()
board = Board([0, 0, 0])
tetromino = board.generatePiece()
draw = Draw(window)
draw.createScreen()
clock = pygame.time.Clock()
timeCount = 0

while isOpen:
    #Clear screen
    draw.screen.fill("Gray")
    
    #Pause / Start screen loop
    while paused or (not started):
        if paused:
            draw.drawPauseScreen(board)
        else:
            draw.drawStartScreen(board)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameStarted = True
                paused = False 
                isOpen = False
            keyInput = pygame.key.get_pressed()
            if keyInput[pygame.K_SPACE]:
                started = True
            if keyInput[pygame.K_p]:
                paused = False

    #Draw game elements to screen
    timeCount += clock.get_rawtime()
    clock.tick()
    draw.drawGrid(board)
    draw.drawTetromino(tetromino)
    draw.drawBackground(board)
    draw.drawScore(board)
    if not (board.isHeldPieceEmpty()):
        draw.drawHeldPiece(board)

    #Main Game loop
    if (timeCount >= 500):
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
        if keyInput[pygame.K_LCTRL]:
            if (board.isHeldPieceEmpty()):
                board.setHeldPiece(tetromino)
                tetromino = board.generatePiece()
            else:
                tetromino = board.swapWithHeldPiece(tetromino)
        if keyInput[pygame.K_LSHIFT]:
            board.rotatePiece(tetromino, "anticlockwise")
        if keyInput[pygame.K_UP]:
            board.rotatePiece(tetromino, "clockwise")
        if keyInput[pygame.K_RIGHT]:
            board.moveOrLockPiece(tetromino, "right")
        if keyInput[pygame.K_LEFT]:
            board.moveOrLockPiece(tetromino, "left")
        if keyInput[pygame.K_DOWN]:
            board.fastDropPiece(tetromino)
            tetromino = board.newPieceOrGameOver(tetromino)
            if tetromino == None:
                gameOver = True
        if keyInput[pygame.K_p]:
            paused = True

    #Game over screen loop
    while gameOver:
        draw.drawGameOver(board)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                gameOver = False
                isOpen = False

    pygame.display.update()    
           