import pygame, sys
from pygame.locals import *

# Number of frames per second
FPS = 10

# Sets size of grid
WINDOWMULTIPLIER = 5 # Modify this number to change size of grid
WINDOWSIZE = 81
WINDOWWIDTH = WINDOWSIZE * WINDOWMULTIPLIER
WINDOWHEIGHT = WINDOWSIZE * WINDOWMULTIPLIER
SQUARESIZE = (WINDOWSIZE * WINDOWMULTIPLIER) / 3 # size of a 3x3 square
CELLSIZE = SQUARESIZE / 3 # Size of a cell
NUMBERSIZE = CELLSIZE /3  # Position of unsolved number

# Set up the colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)


def drawGrid():
    ### Draw Minor Lines
    for x in range(0, WINDOWWIDTH, int(CELLSIZE)):  # draw vertical lines
        pygame.draw.line(DISPLAYSURF, GRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, int(CELLSIZE)):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, GRAY, (0, y), (WINDOWWIDTH, y))

    ### Draw Major Lines
    for x in range(0, WINDOWWIDTH, int(SQUARESIZE)):  # draw vertical lines
        pygame.draw.line(DISPLAYSURF, BLACK, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, int(SQUARESIZE)):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, BLACK, (0, y), (WINDOWWIDTH, y))

    return None


def initiateCells():
    currentGrid = {}
    fullCell = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for xCoord in range(0, 9):
        for yCoord in range(0, 9):
            currentGrid[xCoord, yCoord] = list(fullCell)  # Copies List
    return currentGrid


# Takes the remaining numbers and displays them in the cells.
def displayCells(currentGrid):
    # Create offset factors to display numbers in right location in cells.
    xFactor = 0
    yFactor = 0
    for item in currentGrid:  # item is x,y co-ordinate from 0 -8
        cellData = currentGrid[item]  # isolates the numbers still available for that cell
        for number in cellData:  # iterates through each number
            if number != ' ':  # ignores those already dismissed
                xFactor = ((number - 1) % 3)  # 1/4/7 = 0 2/5/8 = 1 3/6/9 =2
                if number <= 3:
                    yFactor = 0
                elif number <= 6:
                    yFactor = 1
                else:
                    yFactor = 2
                # (item[0] * CELLSIZE) Positions in the right Cell
                # (xFactor*NUMBERSIZE) Offsets to position number
                populateCells(number, (item[0] * CELLSIZE) + (xFactor * NUMBERSIZE),
                              (item[1] * CELLSIZE) + (yFactor * NUMBERSIZE))
    return None


# writes cellData at given x, y co-ordinates
def populateCells(cellData, x, y):
    cellSurf = BASICFONT.render('%s' % (cellData), True, GRAY)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = (x, y)
    DISPLAYSURF.blit(cellSurf, cellRect)

def drawBox(mousex, mousey):
    boxx = ((mousex*27) / WINDOWWIDTH) * (NUMBERSIZE)
    boxy = ((mousey*27) / WINDOWHEIGHT) * (NUMBERSIZE)
    pygame.draw.rect(DISPLAYSURF, BLUE, (boxx, boxy, NUMBERSIZE, NUMBERSIZE), 1)

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    mouseClicked = False
    mousex = 0
    mousey = 0
    pygame.display.set_caption('Sudoku Solver')

    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 15
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    currentGrid = initiateCells() # sets all cells to have number 1-9

    # repaints screen
    DISPLAYSURF.fill(WHITE)
    displayCells(currentGrid)
    drawGrid()

    while True:  # main game loop
        mouseClicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos

            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        if mouseClicked == True:
            print ( mousex )
            print ( mousey )

        # repaints screen
        DISPLAYSURF.fill(WHITE)
        displayCells(currentGrid)
        drawGrid()
        # call function to draw box
        drawBox (mousex, mousey)



        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()